// User Entity
export interface UserPreferences {
  theme: 'light' | 'dark' | 'system';
  notificationsEnabled: boolean;
  taskView: 'list' | 'grid';
}

export interface User {
  id: string;
  email: string;
  name?: string;
  createdAt: Date;
  preferences: UserPreferences;
}

// Task Entity
export interface Task {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  createdAt: Date;
  updatedAt: Date;
  completedAt: Date | null;
  dueDate: Date | null;
  priority: 'low' | 'medium' | 'high';
}

// UI State Models
export interface TaskFilter {
  status: 'all' | 'active' | 'completed';
  priority: 'all' | 'low' | 'medium' | 'high';
  searchQuery: string;
  sortBy: 'createdAt' | 'updatedAt' | 'dueDate' | 'priority';
  sortOrder: 'asc' | 'desc';
}

export interface UIState {
  currentUser: User | null;
  tasks: Task[];
  taskFilters: TaskFilter;
  isLoading: boolean;
  error: string | null;
  isModalOpen: boolean;
  currentModalType: 'create' | 'edit' | 'delete' | null;
  currentModalData: any;
}

// Component State Models
export interface FormState {
  values: Record<string, any>;
  errors: Record<string, string>;
  isSubmitting: boolean;
  submitSuccess: boolean;
  submitError: string | null;
}

export interface ToastState {
  id: string;
  message: string;
  type: 'success' | 'error' | 'warning' | 'info';
  duration: number;
  isVisible: boolean;
}

// API Response Models (Simulated)
export interface AuthResponse {
  user: User;
  token: string;
}

export interface TaskResponse {
  task: Task;
  message: string;
}

export interface TaskListResponse {
  tasks: Task[];
  total: number;
  page: number;
  limit: number;
}

// Component Props
export type ButtonVariant = 'primary' | 'secondary' | 'destructive' | 'ghost' | 'link';
export type ButtonSize = 'sm' | 'default' | 'lg';

export interface ButtonProps {
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

export interface InputProps {
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

export interface CardProps {
  children: React.ReactNode;
  className?: string;
  border?: boolean;
  elevated?: boolean;
}

export interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title?: string;
  children: React.ReactNode;
  size?: 'sm' | 'default' | 'lg' | 'xl';
}

export interface TaskItemProps {
  task: Task;
  onToggleComplete: (id: string) => void;
  onEdit: (id: string) => void;
  onDelete: (id: string) => void;
  className?: string;
}

export interface TaskListProps {
  tasks: Task[];
  onToggleComplete: (id: string) => void;
  onEdit: (id: string) => void;
  onDelete: (id: string) => void;
  filter: TaskFilter;
  onFilterChange: (filter: TaskFilter) => void;
  className?: string;
}