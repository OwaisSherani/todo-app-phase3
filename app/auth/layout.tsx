import { Card, CardContent } from '@/components/ui/card'
import { cn } from '@/lib/utils'

export default function AuthLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-50 to-secondary-50 p-4">
      <Card className={cn(
        'w-full max-w-md shadow-lg',
        'border-0 shadow-subtle'
      )}>
        <CardContent className="p-8">
          {children}
        </CardContent>
      </Card>
    </div>
  )
}