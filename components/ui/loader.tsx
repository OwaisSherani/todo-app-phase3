import { cn } from '@/lib/utils'
import { motion } from 'framer-motion'

interface LoaderProps extends React.HTMLAttributes<HTMLDivElement> {
  size?: 'sm' | 'default' | 'lg';
}

function Loader({ className, size = 'default', ...props }: LoaderProps) {
  const sizeClasses = {
    sm: 'h-4 w-4',
    default: 'h-8 w-8',
    lg: 'h-12 w-12',
  }

  return (
    <div className={cn('flex items-center justify-center', className)} {...props}>
      <motion.div
        className={cn(
          'rounded-full border-4 border-primary-200 border-t-primary-600',
          sizeClasses[size]
        )}
        animate={{ rotate: 360 }}
        transition={{ 
          repeat: Infinity, 
          duration: 1, 
          ease: 'linear' 
        }}
      />
    </div>
  )
}

export { Loader }