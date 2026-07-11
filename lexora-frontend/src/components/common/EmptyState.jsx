import { Logo } from '../brand/Logo.jsx';

export function EmptyState() {
  return (
    <div className="empty-state">
      <div className="empty-state-mark">
        <Logo compact />
      </div>
      <h3>Your result will appear here</h3>
      <p>
        Start with a topic, select the content type, and let LEXORA generate a polished output using the
        multi-agent workflow.
      </p>
    </div>
  );
}
