import { NAV_ITEMS } from '../../constants/navigation.js';
import { APP_INFO } from '../../constants/appInfo.js';
import { Logo } from '../brand/Logo.jsx';
import { Button } from './Button.jsx';
import { Container } from './Container.jsx';

export function Navbar({ currentRoute }) {
  return (
    <header className="site-header">
      <Container className="site-header-inner">
        <a className="brand-link" href="#/" aria-label={`${APP_INFO.name} home`}>
          <Logo />
        </a>

        <nav className="site-nav" aria-label="Primary">
          {NAV_ITEMS.map((item) => {
            const isActive = currentRoute === item.href.replace('#', '');
            return (
              <a key={item.href} href={item.href} className={`site-nav-link ${isActive ? 'active' : ''}`}>
                {item.label}
              </a>
            );
          })}
        </nav>

        <div className="site-actions">
          <Button as="a" href="#/generate" variant="primary">
            Launch Studio
          </Button>
        </div>
      </Container>
    </header>
  );
}
