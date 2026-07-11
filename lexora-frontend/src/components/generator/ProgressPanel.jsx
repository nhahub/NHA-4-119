import { Card } from '../common/Card.jsx';
import { LoadingDots } from '../common/LoadingDots.jsx';
import { formatStatusLabel } from '../../utils/formatters.js';

const workflowSteps = [
  'Outline Agent',
  'Research Agent',
  'Routing Agent',
  'Writer Agent',
  'Critique Agent',
  'Final Result',
];

export function ProgressPanel({
  status,
  progress,
  message,
  error,
  isWorking,
}) {
  const activeCount =
    status === 'completed'
      ? workflowSteps.length
      : Math.min(
          workflowSteps.length - 1,
          Math.max(0, Math.ceil((progress || 0) / 20)),
        );

  return (

    <Card className="progress-card">
      <div className="panel-heading-row">
        <div>
          <span className="eyebrow">Job progress</span>
          <h3>{formatStatusLabel(status)}</h3>
        </div>
        {isWorking ? <LoadingDots /> : null}
      </div>

      <div className="progress-track-shell" aria-hidden="true">
        <div className="progress-track-fill" style={{ width: `${progress || 0}%` }} />
      </div>

      <p className={`status-message ${error ? 'error-text' : ''}`}>{error || message}</p>

      <ul className="workflow-mini-list">
        {workflowSteps.map((step, index) => (
          <li key={step} className={index < activeCount ? 'active' : ''}>
            <span className="workflow-mini-dot" />
            <span>{step}</span>
          </li>
        ))}
      </ul>
    </Card>
  );
}
