import { useMemo, useState } from 'react';
import { Button } from '../common/Button.jsx';
import { Badge } from '../common/Badge.jsx';
import { AdvancedOptions } from './AdvancedOptions.jsx';
import { CONTENT_TYPES, TONE_OPTIONS } from '../../constants/contentOptions.js';
import { hasValidationErrors, validateGenerationForm } from '../../utils/validation.js';

const initialFormData = {
  topic: '',
  content_type: '',
  tone: '',
  audience: '',
  brief: '',
  reference_text: '',
  max_tokens: '',
};

export function GenerateForm({ isWorking, onGenerate }) {
  const [formData, setFormData] = useState(initialFormData);
  const [touched, setTouched] = useState(false);

  const errors = useMemo(() => validateGenerationForm(formData), [formData]);
  const selectedContentType = CONTENT_TYPES.find((option) => option.value === formData.content_type);

  function handleChange(event) {
    const { name, value } = event.target;
    setFormData((previous) => ({
      ...previous,
      [name]: name === 'max_tokens' && value !== '' ? Number(value) : value,
    }));
  }

  function handleSubmit(event) {
    event.preventDefault();
    setTouched(true);

    if (hasValidationErrors(errors)) return;
    onGenerate(formData);
  }

  return (
    <section className="studio-form-card">
      <div className="section-heading compact">
        <Badge>Generation form</Badge>
        <h2>Build your request with precision</h2>
        <p>
          Keep the main form clean, then expand advanced options only when you want more control over the
          output.
        </p>
      </div>

      <form className="generator-form" onSubmit={handleSubmit}>
        <label className="field">
          <span>Topic</span>
          <input
            type="text"
            name="topic"
            value={formData.topic}
            onChange={handleChange}
            placeholder="Example: How AI is changing digital marketing"
            maxLength={200}
          />
          <small className={touched && errors.topic ? 'field-error' : ''}>
            {touched && errors.topic ? errors.topic : `${formData.topic.length}/200 characters`}
          </small>
        </label>

        <div className="form-grid two-columns">
          <label className="field">
            <span>Content type</span>
            <select name="content_type" value={formData.content_type} onChange={handleChange}>
              {CONTENT_TYPES.map((option) => (
                <option key={option.label} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
            <small className={touched && errors.content_type ? 'field-error' : ''}>
              {touched && errors.content_type
                ? errors.content_type
                : selectedContentType?.description || 'Choose the content format you want to generate.'}
            </small>
          </label>

          <label className="field">
            <span>Tone</span>
            <select name="tone" value={formData.tone} onChange={handleChange}>
              {TONE_OPTIONS.map((option) => (
                <option key={option.label} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
            <small>None means the backend default tone will be used.</small>
          </label>
        </div>

        <AdvancedOptions formData={formData} errors={touched ? errors : {}} onChange={handleChange} />

        <div className="form-actions-row">
          <Button type="submit" disabled={isWorking}>
            {isWorking ? 'Generating…' : 'Generate content'}
          </Button>

          <Button
            type="button"
            variant="secondary"
            disabled={isWorking}
            onClick={() => {
              setFormData(initialFormData);
              setTouched(false);
            }}
          >
            Reset form
          </Button>
        </div>
      </form>
    </section>
  );
}
