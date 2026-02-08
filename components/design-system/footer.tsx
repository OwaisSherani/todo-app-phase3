import { cn } from '@/lib/utils'

interface FooterProps {
  className?: string;
}

export function Footer({ className }: FooterProps) {
  const currentYear = new Date().getFullYear();

  return (
    <footer className={cn("border-t py-6 md:py-8", className)}>
      <div className="container flex flex-col items-center justify-between gap-4 md:h-12 md:flex-row">
        <div className="text-center text-sm leading-loose text-muted-foreground md:text-left">
          © {currentYear} Todo App. All rights reserved.
        </div>
        <div className="flex items-center gap-4">
          <a 
            href="/terms" 
            className="text-sm text-muted-foreground hover:underline hover:underline-offset-4"
          >
            Terms
          </a>
          <a 
            href="/privacy" 
            className="text-sm text-muted-foreground hover:underline hover:underline-offset-4"
          >
            Privacy
          </a>
        </div>
      </div>
    </footer>
  );
}