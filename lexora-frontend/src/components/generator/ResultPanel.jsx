import { useState } from 'react';
import { Button } from '../common/Button.jsx';
import { Card } from '../common/Card.jsx';
import { EmptyState } from '../common/EmptyState.jsx';
import { downloadTextFile } from '../../utils/downloadText.js';
import { getContentTypeLabel, getReadingTime, getWordCount } from '../../utils/formatters.js';

export function ResultPanel({ result, onClear }) {
  const [copyLabel, setCopyLabel] = useState('Copy');

  if (!result?.content) {
    return (
      <Card className="result-card empty-result-card">
        <EmptyState />
      </Card>
    );
  }

  const title = getContentTypeLabel(result.content_type);
  const wordCount = getWordCount(result.content);
  const readingTime = getReadingTime(result.content);

  async function handleCopy() {
    await navigator.clipboard.writeText(result.content);
    setCopyLabel('Copied');
    setTimeout(() => setCopyLabel('Copy'), 1500);
  }

  function handleDownload() {
    downloadTextFile({
      content: result.content,
      filename: `lexora-${result.content_type || 'content'}.txt`,
    });
  }

  return (
    <Card className="result-card generated-result-card">
      <div className="result-topbar">
        <div>
          <span className="eyebrow">Output</span>
          <h2>{title}</h2>
          <p>
            {wordCount} words · {readingTime}
            {result.revision_count ? ` · ${result.revision_count} revision(s)` : ''}
          </p>
        </div>

        <div className="result-toolbar">
          <Button type="button" variant="secondary" onClick={handleCopy}>
            {copyLabel}
          </Button>
          <Button type="button" variant="secondary" onClick={handleDownload}>
            Download
          </Button>
          <Button type="button" variant="ghost" onClick={onClear}>
            Clear
          </Button>
        </div>
      </div>

      <article className="generated-content">{result.content}</article>
    </Card>
  );
}
