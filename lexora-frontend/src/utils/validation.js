export function validateGenerationForm(formData) {
  const errors = {};

  if (!formData.topic.trim()) {
    errors.topic = 'Topic is required.';
  }

  if (!formData.content_type) {
    errors.content_type = 'Content type is required.';
  }

  if (formData.topic.length > 200) {
    errors.topic = 'Topic must be 200 characters or fewer.';
  }

  if (formData.audience.length > 200) {
    errors.audience = 'Audience must be 200 characters or fewer.';
  }

  if (formData.brief.length > 2000) {
    errors.brief = 'Brief must be 2000 characters or fewer.';
  }

  if (formData.reference_text.length > 5000) {
    errors.reference_text = 'Reference text must be 5000 characters or fewer.';
  }

  return errors;
}

export function hasValidationErrors(errors) {
  return Object.keys(errors).length > 0;
}
