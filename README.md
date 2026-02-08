# Todo App Frontend

A premium, professional todo application built with Next.js, TypeScript, and Tailwind CSS.

## Features

- Clean, professional UI with strong visual hierarchy
- Responsive design that works on mobile, tablet, and desktop
- Authentication flow (sign up and sign in)
- Task management (create, read, update, delete, mark complete)
- Task filtering and prioritization
- Loading states and skeleton screens
- Empty states and error handling
- Toast notifications for user feedback
- Dark/light mode with system preference detection
- Accessibility features (keyboard navigation, screen reader support)

## Tech Stack

- [Next.js](https://nextjs.org/) - React framework with App Router
- [TypeScript](https://www.typescriptlang.org/) - Type-safe JavaScript
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [Headless UI](https://headlessui.com/) - Accessible UI components
- [Framer Motion](https://www.framer.com/motion/) - Production-ready animations
- [Radix UI Primitives](https://www.radix-ui.com/) - Accessible UI primitives
- [Lucide React](https://lucide.dev/) - Icon library

## Getting Started

### Prerequisites

- Node.js 18+ installed
- npm or yarn package manager

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Start the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

4. Open your browser to [http://localhost:3000](http://localhost:3000)

## Project Structure

```
frontend/
├── app/                    # Next.js App Router pages
│   ├── layout.tsx          # Root layout
│   ├── page.tsx            # Home page
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
├── docs/                   # Documentation
└── public/                 # Static assets
```

## Scripts

- `npm run dev` - Start the development server
- `npm run build` - Build the application for production
- `npm run start` - Start the production server
- `npm run lint` - Run ESLint

## Design System

The application implements a consistent design system with:

### Color Palette
- **Neutral Base**: Gray scale (50-900) for backgrounds, text, borders
- **Accent Color**: Indigo (500-700) for primary actions, links, highlights
- **Destructive**: Red (500-600) for delete actions and errors
- **Success**: Green (500) for success states
- **Warning**: Amber (500) for warnings

### Typography Scale
- **Heading 1**: 2.5rem (40px) - Dashboard titles
- **Heading 2**: 2rem (32px) - Section titles
- **Heading 3**: 1.5rem (24px) - Card titles
- **Body Large**: 1.125rem (18px) - Primary text
- **Body Regular**: 1rem (16px) - Secondary text
- **Body Small**: 0.875rem (14px) - Labels, captions
- **Body Extra Small**: 0.75rem (12px) - Metadata, helper text

### Spacing System
- **Scale**: 0.25rem (4px) base unit with 8-step scale (0, 0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4, 6, 8)
- **Border Radius**: 0.375rem (6px) base with 0.5rem (8px) for cards
- **Shadows**: Subtle shadows for depth (0 1px 2px 0 rgba(0,0,0,0.05))
- **Motion**: 200ms ease-in-out for transitions, 300ms for animations

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License.