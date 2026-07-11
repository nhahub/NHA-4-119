import { Button } from '../components/common/Button.jsx';
import { Container } from '../components/common/Container.jsx';

export function NotFoundPage() {
  return (
    <Container className="not-found-page">
      <div className="not-found-card">
        <span className="eyebrow">404</span>
        <h1>Page not found</h1>
        <p>The route you requested does not exist in the current frontend build.</p>
        <Button as="a" href="#/" variant="primary">
          Back to Home
        </Button>
      </div>
    </Container>
  );
}
