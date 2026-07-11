import { APP_INFO } from '../../constants/appInfo.js';
import { NAV_ITEMS } from '../../constants/navigation.js';
import { Logo } from '../brand/Logo.jsx';
import { Container } from './Container.jsx';

export function Footer() {
  return (
    <footer className="site-footer">
      <Container className="site-footer-grid">
        <div className="footer-brand-block">
          <Logo />
          <p>{APP_INFO.description}</p>
        </div>

        <div>
          <h4>Navigation</h4>
          <ul className="footer-list">
            {NAV_ITEMS.map((item) => (
              <li key={item.href}>
                <a href={item.href}>{item.label}</a>
              </li>
            ))}
          </ul>
        </div>

        <div>
          <h4>Project Highlights</h4>
          <ul className="footer-list">
            <li>Five content formats</li>
            <li>FastAPI integration</li>
            <li>Job progress tracking</li>
            <li>Copy and download output</li>
          </ul>
        </div>
      </Container>

      <Container className="site-footer-bottom">
        <span>© 2026 {APP_INFO.name}. AI Content Generation Platform.</span>
      </Container>
    </footer>
  );
}
