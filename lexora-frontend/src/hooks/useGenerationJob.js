import { useCallback, useEffect, useRef, useState } from 'react';
import { createGenerationJob, getJobResult, getJobStatus } from '../services/generationApi.js';

const POLLING_INTERVAL_MS = 1500;
const MAX_POLLING_ATTEMPTS = 600;

const initialState = {
  jobId: null,
  status: 'idle',
  progress: 0,
  message: 'Ready to generate your content.',
  result: null,
  error: null,
};

export function useGenerationJob() {
  const [state, setState] = useState(initialState);
  const pollingTimeoutRef = useRef(null);
  const pollingAttemptsRef = useRef(0);

  const stopPolling = useCallback(() => {
    if (pollingTimeoutRef.current) {
      clearTimeout(pollingTimeoutRef.current);
      pollingTimeoutRef.current = null;
    }
  }, []);

  const resetJob = useCallback(() => {
    stopPolling();
    pollingAttemptsRef.current = 0;
    setState(initialState);
  }, [stopPolling]);

  const pollJob = useCallback(
    async (jobId) => {
      try {
        pollingAttemptsRef.current += 1;

        if (pollingAttemptsRef.current > MAX_POLLING_ATTEMPTS) {
          throw new Error('Generation is taking longer than expected. Please try again.');
        }

        const statusData = await getJobStatus(jobId);

        setState((previous) => ({
          ...previous,
          jobId,
          status: statusData.status,
          progress: statusData.progress,
          message: statusData.message,
          error: statusData.error || null,
        }));

        if (statusData.status === 'completed') {
          const resultData = await getJobResult(jobId);
          setState((previous) => ({
            ...previous,
            status: 'completed',
            progress: 100,
            message: 'Generation completed successfully.',
            result: resultData,
          }));
          stopPolling();
          return;
        }

        if (statusData.status === 'failed') {
          throw new Error(statusData.error || 'Generation failed.');
        }

        pollingTimeoutRef.current = setTimeout(() => pollJob(jobId), POLLING_INTERVAL_MS);
      } catch (error) {
        stopPolling();
        setState((previous) => ({
          ...previous,
          status: 'failed',
          progress: previous.progress,
          message: 'Generation failed.',
          error: error.message,
        }));
      }
    },
    [stopPolling],
  );

  const startGeneration = useCallback(
    async (formData) => {
      stopPolling();
      pollingAttemptsRef.current = 0;
      setState({
        ...initialState,
        status: 'queued',
        message: 'Sending your request to LEXORA...',
      });

      try {
        const queuedJob = await createGenerationJob(formData);
        setState((previous) => ({
          ...previous,
          jobId: queuedJob.job_id,
          status: queuedJob.status,
          message: 'Job queued. Preparing the agent workflow...',
        }));
        pollJob(queuedJob.job_id);
      } catch (error) {
        setState((previous) => ({
          ...previous,
          status: 'failed',
          progress: 0,
          message: 'Could not start generation.',
          error: error.message,
        }));
      }
    },
    [pollJob, stopPolling],
  );

  useEffect(() => stopPolling, [stopPolling]);

  return {
    ...state,
    isWorking: ['queued', 'running'].includes(state.status),
    startGeneration,
    resetJob,
  };
}
