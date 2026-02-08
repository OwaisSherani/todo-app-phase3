'use client'

import { Button } from '@/components/ui/button'
import { motion } from 'framer-motion'
import Link from 'next/link'
import { useRouter } from 'next/navigation'

interface HeaderProps {
  title: string;
  showAuthButtons?: boolean;
  onLogout?: () => void;
}

export function Header({ title, showAuthButtons = false, onLogout }: HeaderProps) {
  const router = useRouter();

  const handleLogout = () => {
    // Simulate logout
    if (onLogout) {
      onLogout();
    }
    // Redirect to sign in page
    router.push('/auth/signin');
  };

  return (
    <motion.header 
      className="border-b"
      initial={{ y: -20, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.3 }}
    >
      <div className="container flex h-16 items-center justify-between px-4">
        <Link href="/" className="flex items-center space-x-2">
          <span className="text-xl font-bold">Todo App</span>
        </Link>
        
        <div className="flex items-center space-x-4">
          <h1 className="text-xl font-semibold">{title}</h1>
          
          {showAuthButtons ? (
            <Button variant="outline" onClick={handleLogout}>
              Logout
            </Button>
          ) : null}
        </div>
      </div>
    </motion.header>
  );
}