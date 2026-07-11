export function Logo({ compact = false }) {
  return (
    <div className={`brand ${compact ? 'compact' : ''}`}>
      <span className="brand-mark" aria-hidden="true">
        <svg viewBox="0 0 64 64" role="img">
          <defs>
            <linearGradient id="lexoraPremiumGradient" x1="8" y1="8" x2="56" y2="56">
              <stop offset="0%" stopColor="#0f172a" />
              <stop offset="52%" stopColor="#2563eb" />
              <stop offset="100%" stopColor="#14b8a6" />
            </linearGradient>
          </defs>
          <rect x="8" y="8" width="48" height="48" rx="18" fill="url(#lexoraPremiumGradient)" />
          <path
            d="M22 43V21h6.3v16.5H42V43H22Zm26-22-9.1 11L48 43h-7.2l-8.6-10.8L41.1 21H48Z"
            fill="#ffffff"
          />
          <circle cx="47" cy="17" r="4" fill="#f59e0b" />
        </svg>
      </span>

      {!compact && (
        <span className="brand-copy">
          <span className="brand-name">LEXORA</span>
          <span className="brand-tagline">AI Content Studio</span>
        </span>
      )}
    </div>
  );
}
