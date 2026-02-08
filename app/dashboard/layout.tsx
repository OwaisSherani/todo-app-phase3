import { Header } from '@/components/design-system/header'
import { Footer } from '@/components/design-system/footer'

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="flex min-h-screen flex-col">
      <Header title="Dashboard" showAuthButtons={true} />
      <main className="flex-1 p-4 md:p-8">
        {children}
      </main>
      <Footer />
    </div>
  )
}