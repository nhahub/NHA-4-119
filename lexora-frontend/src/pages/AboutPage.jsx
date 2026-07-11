import { Badge } from '../components/common/Badge.jsx';
import { Card } from '../components/common/Card.jsx';
import { Container } from '../components/common/Container.jsx';

const workflowSteps = [
  {
    title: 'Outline Agent',
    text: 'Creates a clear structure so the content starts with a plan instead of random text.',
  },
  {
    title: 'Search Agent',
    text: 'Adds useful supporting context when the workflow needs more information.',
  },
  {
    title: 'Router Agent',
    text: 'Chooses the correct writing path based on the selected content type.',
  },
  {
    title: 'Writer Agent',
    text: 'Generates the draft using the topic, content type, tone, audience, brief, and reference text.',
  },
  {
    title: 'Critique Agent',
    text: 'Reviews the draft and improves it before the final answer is returned.',
  },
];

export function AboutPage() {
  return (
    <Container className="page-shell workflow-page">
      <div className="section-heading">
        <Badge>How LEXORA works</Badge>
        <h1>A structured AI workflow behind a simple interface.</h1>
        <p>
          The interface collects the user request, the backend manages the generation job, and the agent
          workflow returns the final polished content.
        </p>
      </div>

      <div className="workflow-timeline">
        {workflowSteps.map((step, index) => (
          <Card key={step.title} className="workflow-row-card">
            <span className="workflow-number">{String(index + 1).padStart(2, '0')}</span>
            <div>
              <h3>{step.title}</h3>
              <p>{step.text}</p>
            </div>
          </Card>
        ))}
      </div>

      <Card className="api-flow-card">
        <Badge>Process flow</Badge>
        <h2>Job-based generation</h2>
        <p>
          The user submits a request, LEXORA creates a generation job, tracks its progress, and displays the
          final content when the workflow is complete.
        </p>
      </Card>
    </Container>
  );
}
