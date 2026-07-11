import { Badge } from '../components/common/Badge.jsx';
import { Container } from '../components/common/Container.jsx';
import { GenerateForm } from '../components/generator/GenerateForm.jsx';
import { ProgressPanel } from '../components/generator/ProgressPanel.jsx';
import { ResultPanel } from '../components/generator/ResultPanel.jsx';
import { useGenerationJob } from '../hooks/useGenerationJob.js';

export function GeneratePage() {
  const generation = useGenerationJob();

  return (
    <Container className="studio-page">
      <div className="section-heading left aligned-heading">
        <Badge>AI Studio</Badge>
        <h1>Generate content in a cleaner, smarter workspace</h1>
        <p>
          Configure the essentials, add optional context, then monitor the backend job while LEXORA builds
          your output.
        </p>
      </div>

      <div className="studio-grid">
        <div className="studio-left-column">
          <GenerateForm isWorking={generation.isWorking} onGenerate={generation.startGeneration} />
          <ProgressPanel
            status={generation.status}
            progress={generation.progress}
            message={generation.message}
            error={generation.error}
            isWorking={generation.isWorking}
          />
        </div>

        <div className="studio-right-column">
          <ResultPanel result={generation.result} onClear={generation.resetJob} />
        </div>
      </div>
    </Container>
  );
}
