import { useEffect, useState } from 'react';
import { Footer } from './components/common/Footer.jsx';
import { Navbar } from './components/common/Navbar.jsx';
import { AboutPage } from './pages/AboutPage.jsx';
import { GeneratePage } from './pages/GeneratePage.jsx';
import { HomePage } from './pages/HomePage.jsx';
import { NotFoundPage } from './pages/NotFoundPage.jsx';
import { TeamPage } from './pages/TeamPage.jsx';

function getRouteFromHash() {
  const hash = window.location.hash.replace('#', '') || '/';
  return hash.startsWith('/') ? hash : `/${hash}`;
}

export default function App() {
  const [route, setRoute] = useState(getRouteFromHash());

  useEffect(() => {
    const handleHashChange = () => setRoute(getRouteFromHash());
    window.addEventListener('hashchange', handleHashChange);
    return () => window.removeEventListener('hashchange', handleHashChange);
  }, []);

  const renderPage = () => {
    switch (route) {
      case '/':
        return <HomePage />;
      case '/generate':
        return <GeneratePage />;
      case '/about':
        return <AboutPage />;
      case '/team':
        return <TeamPage />;
      default:
        return <NotFoundPage />;
    }
  };

  return (
    <div className="app-shell">
      <Navbar currentRoute={route} />
      <main>{renderPage()}</main>
      <Footer />
    </div>
  );
}
