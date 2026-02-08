// Application constants
export const APP_NAME = 'Todo App'
export const DEFAULT_THEME = 'system'
export const DEFAULT_TASK_VIEW = 'list'

// API endpoints (simulated for frontend-only implementation)
export const API_ENDPOINTS = {
  AUTH: {
    SIGNUP: '/api/auth/signup',
    SIGNIN: '/api/auth/signin',
    SIGNOUT: '/api/auth/signout',
  },
  TASKS: {
    GET_ALL: '/api/tasks',
    CREATE: '/api/tasks',
    UPDATE: '/api/tasks',
    DELETE: '/api/tasks',
  },
}

// UI constants
export const UI_CONSTANTS = {
  TOAST_DURATION: 5000, // 5 seconds
  MODAL_CLOSE_DELAY: 300, // 300ms for animations
  DEBOUNCE_DELAY: 300, // 300ms for search debouncing
}

// Validation constants
export const VALIDATION = {
  MIN_PASSWORD_LENGTH: 8,
  MAX_TITLE_LENGTH: 255,
  MAX_DESCRIPTION_LENGTH: 1000,
}

// Breakpoints for responsive design
export const BREAKPOINTS = {
  MOBILE: 768,
  TABLET: 1024,
  DESKTOP: 1200,
}

// Task priority colors
export const PRIORITY_COLORS = {
  low: 'text-green-600 bg-green-100',
  medium: 'text-yellow-600 bg-yellow-100',
  high: 'text-red-600 bg-red-100',
}