import { CONTENT_TYPES } from '../constants/contentOptions.js';

export function getContentTypeLabel(value) {
  return CONTENT_TYPES.find((option) => option.value === value)?.label || 'Generated Content';
}

export function getWordCount(text) {
  if (!text?.trim()) return 0;
  return text.trim().split(/\s+/).length;
}

export function getReadingTime(text) {
  const words = getWordCount(text);
  const minutes = Math.max(1, Math.ceil(words / 220));
  return `${minutes} min read`;
}

export function formatStatusLabel(status) {
  if (!status) return 'Idle';
  return status.charAt(0).toUpperCase() + status.slice(1);
}
