export const CONTENT_TYPES = [
  { label: 'None', value: '', description: 'Choose a content format' },
  { label: 'Blog Post', value: 'blog', description: 'Structured long-form article with headings and clear flow' },
  { label: 'LinkedIn Post', value: 'linkedin', description: 'Professional social post with hook, body, CTA, and hashtags' },
  { label: 'Tweet', value: 'tweet', description: 'Short and punchy content for X / Twitter' },
  { label: 'Instagram Caption', value: 'instagram', description: 'Engaging caption with a social tone and hashtags' },
  { label: 'Short Story', value: 'short_story', description: 'Creative narrative with story structure and emotion' },
];

export const TONE_OPTIONS = [
  { label: 'None', value: '' },
  { label: 'Professional', value: 'professional' },
  { label: 'Casual', value: 'casual' },
  { label: 'Witty', value: 'witty' },
  { label: 'Inspirational', value: 'inspirational' },
  { label: 'Educational', value: 'educational' },
  { label: 'Neutral', value: 'neutral' },
];

export const TOKEN_OPTIONS = [
  { label: 'None', value: '' },
  { label: 'Short · 250 tokens', value: 250 },
  { label: 'Standard · 500 tokens', value: 500 },
  { label: 'Detailed · 900 tokens', value: 900 },
  { label: 'Long · 1500 tokens', value: 1500 },
  { label: 'Maximum · 2000 tokens', value: 2000 },
];

export const FEATURE_CARDS = [
  {
    icon: '✦',
    title: 'Blog Posts',
    text: 'Structured long-form writing with sections, clarity, and a clear ending.',
  },
  {
    icon: 'in',
    title: 'LinkedIn Posts',
    text: 'Career and business posts with a strong hook, practical value, and CTA.',
  },
  {
    icon: '𝕏',
    title: 'Tweets',
    text: 'Short, memorable ideas suitable for fast social publishing.',
  },
  {
    icon: '◎',
    title: 'Instagram Captions',
    text: 'Captions with a natural social tone, emotional pull, and hashtags.',
  },
  {
    icon: '✍',
    title: 'Short Stories',
    text: 'Creative narratives with characters, atmosphere, and story flow.',
  },
];
