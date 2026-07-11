import { Badge } from '../components/common/Badge.jsx';
import { Card } from '../components/common/Card.jsx';
import { Container } from '../components/common/Container.jsx';
import { TEAM_MEMBERS } from '../constants/team.js';

export function TeamPage() {
  return (
    <Container className="page-shell">
      <div className="section-heading">
        <Badge>Project team</Badge>
        <h1>Built by the LEXORA team</h1>
        <p>Team members, roles, and responsibilities can be customized based on your final project structure.</p>
      </div>

      <div className="team-grid">
        {TEAM_MEMBERS.map((member, index) => (
          <Card key={member.name} className="team-card">
            <div className="team-avatar">{String(index + 1).padStart(2, '0')}</div>
            <h3>{member.name}</h3>
            <p className="team-role">{member.role}</p>
            <p>{member.note}</p>
          </Card>
        ))}
      </div>
    </Container>
  );
}
