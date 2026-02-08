# UI Component Contracts: Premium, Professional Frontend UI for Todo Web App

**Feature**: 001-premium-frontend-ui
**Date**: 2026-01-04

## Overview

This document defines the contracts for UI components in the Todo Web App frontend. These contracts specify the interface, behavior, and styling requirements for each component to ensure consistency and maintainability.

## Button Component Contract

### Interface
```typescript
type ButtonVariant = 'primary' | 'secondary' | 'destructive' | 'ghost' | 'link';
type ButtonSize = 'sm' | 'default' | 'lg';

interface ButtonProps {
  children: React.ReactNode;
  variant?: ButtonVariant;
  size?: ButtonSize;
  disabled?: boolean;
  loading?: boolean;
  onClick?: () => void;
  className?: string;
  type?: 'button' | 'submit' | 'reset';
  asChild?: boolean;
}
```

### Behavior
- **Primary**: Used for main actions, has solid background
- **Secondary**: Used for secondary actions, outlined
- **Destructive**: Used for destructive actions (like delete), red color
- **Ghost**: Minimal styling, used for subtle actions
- **Link**: Styled like a link, used for navigation

### States
- **Default**: Normal appearance
- **Hover**: Slightly darker/lighter background (depending on variant)
- **Active**: Pressed appearance
- **Disabled**: Grayed out, no interaction
- **Loading**: Shows spinner, disabled

### Accessibility
- Proper ARIA labels
- Keyboard navigable (Tab key)
- Focus indicators
- Screen reader compatible

## Input Component Contract

### Interface
```typescript
interface InputProps {
  value?: string;
  onChange?: (value: string) => void;
  placeholder?: string;
  type?: string;
  disabled?: boolean;
  error?: string;
  label?: string;
  id?: string;
  className?: string;
}
```

### Behavior
- Supports all standard HTML input types
- Shows error state when error prop is provided
- Properly associated with label for accessibility

### States
- **Default**: Standard appearance
- **Focus**: Border highlight
- **Error**: Red border and error text
- **Disabled**: Grayed out, no interaction

## Card Component Contract

### Interface
```typescript
interface CardProps {
  children: React.ReactNode;
  className?: string;
  border?: boolean;
  elevated?: boolean;
}
```

### Behavior
- Container with consistent padding and border
- Optional border and elevation (shadow) properties
- Responsive design

## Modal Component Contract

### Interface
```typescript
interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title?: string;
  children: React.ReactNode;
  size?: 'sm' | 'default' | 'lg' | 'xl';
}
```

### Behavior
- Overlay background when open
- Click outside or ESC key to close
- Proper focus management (trap focus within modal)
- Accessible with screen readers

### States
- **Closed**: Not visible
- **Open**: Visible with overlay

## Task Item Component Contract

### Interface
```typescript
interface TaskItemProps {
  task: Task;
  onToggleComplete: (id: string) => void;
  onEdit: (id: string) => void;
  onDelete: (id: string) => void;
  className?: string;
}
```

### Behavior
- Displays task information (title, description, due date, priority)
- Shows completion status with checkbox
- Visual indication for completed tasks (strikethrough, faded appearance)
- Action buttons for edit and delete

### States
- **Active**: Normal appearance
- **Completed**: Strikethrough title, faded appearance
- **Hover**: Highlighted background

## Task List Component Contract

### Interface
```typescript
interface TaskListProps {
  tasks: Task[];
  onToggleComplete: (id: string) => void;
  onEdit: (id: string) => void;
  onDelete: (id: string) => void;
  filter: TaskFilter;
  onFilterChange: (filter: TaskFilter) => void;
  className?: string;
}
```

### Behavior
- Displays list of tasks with filtering and sorting
- Empty state when no tasks match filters
- Loading state during data fetch
- Error state if data fetch fails

## Authentication Form Contracts

### Sign Up Form
- Fields: email, password, confirm password
- Validation for email format and password strength
- Error handling for duplicate accounts
- Success feedback after account creation

### Sign In Form
- Fields: email, password
- Validation for credentials
- Error handling for invalid credentials
- Success feedback after authentication

## Responsive Behavior Contracts

### Breakpoints
- **Mobile**: 320px - 768px
- **Tablet**: 768px - 1024px
- **Desktop**: 1024px+

### Component Adaptations
- **Button**: Full-width on mobile, compact on desktop
- **Card**: Full-width on mobile, constrained width on desktop
- **Form**: Stacked layout on mobile, side-by-side on desktop
- **Task List**: Single column on mobile, multi-column on desktop

## Accessibility Contracts

### Keyboard Navigation
- All interactive elements must be reachable via Tab key
- Visual focus indicators for keyboard users
- Logical tab order matching visual flow

### Screen Reader Compatibility
- Proper ARIA labels and roles
- Semantic HTML structure
- Announcements for state changes

### Color Contrast
- Minimum 4.5:1 contrast ratio for normal text
- Minimum 3:1 contrast ratio for large text
- Sufficient contrast in both light and dark modes

## Performance Contracts

### Loading States
- Skeleton screens during data fetch
- Optimistic updates for immediate feedback
- Proper error boundaries

### Animation Performance
- 60fps animations using hardware acceleration
- Reduced motion option for users with preferences
- Subtle transitions that enhance UX without being distracting