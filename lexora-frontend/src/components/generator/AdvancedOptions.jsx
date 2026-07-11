import { TOKEN_OPTIONS } from '../../constants/contentOptions.js';

export function AdvancedOptions({ formData, errors, onChange }) {
  return (
    <details className="advanced-panel">
      <summary>
        <span>Advanced options</span>
        <small>Add more context for stronger output quality</small>
      </summary>

      <div className="advanced-panel-body">
        <div className="form-grid two-columns">
          <label className="field">
            <span>Audience</span>
            <input
              type="text"
              name="audience"
              value={formData.audience}
              onChange={onChange}
              placeholder="Example: startup founders, marketers, students"
              maxLength={200}
            />
            <small className={errors.audience ? 'field-error' : ''}>
              {errors.audience || `${formData.audience.length}/200 characters`}
            </small>
          </label>

          <label className="field">
            <span>Max tokens</span>
            <select name="max_tokens" value={formData.max_tokens} onChange={onChange}>
              {TOKEN_OPTIONS.map((option) => (
                <option key={option.label} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
            <small>None lets the backend choose its default generation length.</small>
          </label>
        </div>

        <label className="field">
          <span>Brief / instructions</span>
          <textarea
            name="brief"
            value={formData.brief}
            onChange={onChange}
            placeholder="Example: Make it practical, concise, and suitable for a professional audience."
            rows="5"
            maxLength={2000}
          />
          <small className={errors.brief ? 'field-error' : ''}>
            {errors.brief || `${formData.brief.length}/2000 characters`}
          </small>
        </label>

        <label className="field">
          <span>Reference text</span>
          <textarea
            name="reference_text"
            value={formData.reference_text}
            onChange={onChange}
            placeholder="Paste any supporting text, notes, bullet points, or context that should influence the output."
            rows="7"
            maxLength={5000}
          />
          <small className={errors.reference_text ? 'field-error' : ''}>
            {errors.reference_text || `${formData.reference_text.length}/5000 characters`}
          </small>
        </label>
      </div>
    </details>
  );
}
