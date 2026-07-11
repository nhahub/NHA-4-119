import { APP_INFO } from '../constants/appInfo.js';
import { FEATURE_CARDS } from '../constants/contentOptions.js';
import { Badge } from '../components/common/Badge.jsx';
import { Button } from '../components/common/Button.jsx';
import { Card } from '../components/common/Card.jsx';
import { Container } from '../components/common/Container.jsx';

const stats = [
  { value: '5', label: 'content formats' },
  { value: '6', label: 'tone options' },
  { value: 'Live', label: 'job tracking' },
];

const prompts = [
  'How AI will change digital marketing in 2026',
  'A LinkedIn post about learning FastAPI and React',
  'A short story about a robot discovering creativity',
];

export function HomePage() {
  return (
    <>
      <section className="hero-section">
        <Container className="hero-grid">
          <div className="hero-copy">
            <Badge>Premium AI Content Platform</Badge>
            <h1>Generate elegant content from one focused idea.</h1>
            <p>
              {APP_INFO.description} A clean interface, clear workflow, and polished output experience built
              for a professional project demo.
            </p>

            <div className="hero-actions">
              <Button as="a" href="#/generate">
                Start creating
              </Button>
              <Button as="a" href="#/about" variant="secondary">
                View workflow
              </Button>
            </div>

            <div className="hero-stats">
              {stats.map((stat) => (
                <div key={stat.label} className="stat-card">
                  <strong>{stat.value}</strong>
                  <span>{stat.label}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="hero-preview-card">
            <div className="preview-window-header">
              <div className="window-controls">
                <span />
                <span />
                <span />
              </div>
              <strong>LEXORA Studio</strong>
              <small>Live Preview</small>
            </div>

            <div className="preview-main-card">
              <span>Topic</span>
              <h3>The future of AI in creative work</h3>
              <p>Generate a professional LinkedIn post with a strong hook and a clear CTA.</p>
            </div>

            <div className="preview-grid">
              <div>
                <span>Content Type</span>
                <strong>LinkedIn Post</strong>
              </div>
              <div>
                <span>Tone</span>
                <strong>Professional</strong>
              </div>
            </div>

            <div className="preview-progress">
              <div className="preview-progress-top">
                <strong>Agent workflow</strong>
                <span>82%</span>
              </div>
              <div className="preview-bar"><span /></div>
              <div className="preview-lines">
                <i />
                <i />
                <i />
              </div>
            </div>
          </div>
        </Container>
      </section>

      <section className="section-block">
        <Container>
          <div className="section-heading">
            <Badge>Content formats</Badge>
            <h2>Built for real writing scenarios</h2>
            <p>Each content type has a focused purpose so the generated output feels more useful.</p>
          </div>

          <div className="feature-grid">
            {FEATURE_CARDS.map((feature) => (
              <Card key={feature.title} className="feature-card">
                <div className="feature-icon">{feature.icon}</div>
                <h3>{feature.title}</h3>
                <p>{feature.text}</p>
              </Card>
            ))}
          </div>
        </Container>
      </section>

      <section className="section-block final-cta-section">
        <Container className="cta-grid">
          <Card className="prompt-card">
            <Badge>Prompt examples</Badge>
            <h2>Start from an idea, then refine with tone and context.</h2>
            <div className="prompt-list">
              {prompts.map((prompt) => (
                <span key={prompt}>{prompt}</span>
              ))}
            </div>
          </Card>

          <Card className="cta-card">
            <Badge>Frontend ready</Badge>
            <h2>Clean API flow, loading states, copy, download, and responsive layout.</h2>
            <Button as="a" href="#/generate">
              Open generator
            </Button>
          </Card>
        </Container>
      </section>
    </>
  );
}
