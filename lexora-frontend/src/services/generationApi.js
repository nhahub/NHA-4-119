import { apiRequest } from './apiClient.js';

function removeEmptyValues(payload) {
  return Object.fromEntries(
    Object.entries(payload).filter(([, value]) => value !== '' && value !== null && value !== undefined),
  );
}

export function createGenerationJob(formData) {
  const payload = removeEmptyValues({
    topic: formData.topic.trim(),
    content_type: formData.content_type,
    tone: formData.tone,
    audience: formData.audience.trim(),
    brief: formData.brief.trim(),
    reference_text: formData.reference_text.trim(),
    max_tokens: formData.max_tokens,
  });

  return apiRequest('/api/v1/generate', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}

export function getJobStatus(jobId) {
  return apiRequest(`/api/v1/jobs/${jobId}`);
}

export function getJobResult(jobId) {
  return apiRequest(`/api/v1/jobs/${jobId}/result`);
}
