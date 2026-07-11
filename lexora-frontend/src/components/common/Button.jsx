export function Button({
  as = 'button',
  variant = 'primary',
  className = '',
  children,
  ...props
}) {
  const Component = as;
  return (
    <Component className={`button button-${variant} ${className}`.trim()} {...props}>
      {children}
    </Component>
  );
}
