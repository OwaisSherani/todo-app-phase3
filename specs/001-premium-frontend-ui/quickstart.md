# Quickstart Guide: Premium, Professional Frontend UI for Todo Web App

**Feature**: 001-premium-frontend-ui
**Date**: 2026-01-04

## Getting Started

This guide will help you set up and run the premium, professional frontend UI for the Todo Web App.

### Prerequisites

- Node.js 18+ installed
- npm or yarn package manager
- A code editor (VS Code recommended)

### Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

3. **Install dependencies**:
   ```bash
   npm install
   # or
   yarn install
   ```

### Development

1. **Start the development server**:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

2. **Open your browser** to `http://localhost:3000`

3. **Start coding**! The page will automatically reload as you make changes.

### Project Structure

```
frontend/
├── app/                    # Next.js App Router pages
│   ├── layout.tsx          # Root layout
│   ├── page.tsx            # Home page (redirects to auth or dashboard)
│   ├── auth/               # Authentication pages
│   │   ├── layout.tsx
│   │   ├── signin/
│   │   │   └── page.tsx
│   │   └── signup/
│   │       └── page.tsx
│   └── dashboard/          # Main application pages
│       ├── layout.tsx
│       └── page.tsx
├── components/             # Reusable UI components
│   ├── ui/                 # Base UI components (buttons, inputs, etc.)
│   ├── auth/               # Authentication-specific components
│   ├── dashboard/          # Dashboard-specific components
│   └── design-system/      # Design system components
├── lib/                    # Utility functions
├── hooks/                  # Custom React hooks
├── styles/                 # Global styles and themes
├── types/                  # TypeScript type definitions
└── public/                 # Static assets
```

### Key Technologies

- **Next.js 14+**: React framework with App Router
- **TypeScript**: Type-safe JavaScript
- **Tailwind CSS**: Utility-first styling
- **Headless UI**: Unstyled, accessible UI components
- **Framer Motion**: Production-ready animations

### Running Tests

1. **Run unit tests**:
   ```bash
   npm run test
   # or
   yarn test
   ```

2. **Run end-to-end tests**:
   ```bash
   npm run test:e2e
   # or
   yarn test:e2e
   ```

### Building for Production

1. **Build the application**:
   ```bash
   npm run build
   # or
   yarn build
   ```

2. **Preview the production build**:
   ```bash
   npm run start
   # or
   yarn start
   ```

### Environment Variables

Create a `.env.local` file in the `frontend` directory with the following variables:

```env
NEXT_PUBLIC_API_URL=http://localhost:3001/api
NEXT_PUBLIC_APP_NAME=Todo App
```

### Design System Usage

The application uses a custom design system built on top of Tailwind CSS and Headless UI. To use components:

```tsx
import { Button, Card, Input } from '@/components/ui'

// Example usage
<Button variant="primary" size="default">
  Click me
</Button>
```

### Theming

The application supports light and dark themes with system preference detection:

- Themes are defined in `styles/themes.css`
- Theme switching is handled by `ThemeProvider` in `app/providers/theme-provider.tsx`
- Components automatically adapt to the current theme

### Key Features

1. **Responsive Design**: Works on mobile, tablet, and desktop
2. **Accessibility**: Full keyboard navigation and screen reader support
3. **Performance**: Optimized loading and smooth animations
4. **Type Safety**: Full TypeScript coverage
5. **Design Consistency**: Unified design system across all components

### Next Steps

1. Review the [implementation plan](./plan.md) for detailed architecture
2. Check the [data model](./data-model.md) for state structure
3. Look at the [research](./research.md) for technology decisions
4. Explore the [component contracts](./contracts/) for API specifications