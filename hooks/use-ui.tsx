"use client"

import { createContext, useContext, useReducer } from 'react'
import { Task, UIState } from '@/types'

type UIAction =
  | { type: 'SET_LOADING'; payload: boolean }
  | { type: 'SET_ERROR'; payload: string | null }
  | { type: 'SET_CURRENT_USER'; payload: any | null }
  | { type: 'ADD_TASK'; payload: Task }
  | { type: 'UPDATE_TASK'; payload: Task }
  | { type: 'DELETE_TASK'; payload: string }
  | { type: 'SET_TASKS'; payload: Task[] }
  | { type: 'SET_MODAL'; payload: { isOpen: boolean; type: 'create' | 'edit' | 'delete' | null; data?: any } }
  | { type: 'SET_TASK_FILTER'; payload: Partial<UIState['taskFilters']> }

const initialState: UIState = {
  currentUser: null,
  tasks: [],
  taskFilters: {
    status: 'all',
    priority: 'all',
    searchQuery: '',
    sortBy: 'createdAt',
    sortOrder: 'desc',
  },
  isLoading: false,
  error: null,
  isModalOpen: false,
  currentModalType: null,
  currentModalData: null,
}

const UIContext = createContext<{
  state: UIState;
  dispatch: React.Dispatch<UIAction>;
}>({
  state: initialState,
  dispatch: () => null,
});

const uiReducer = (state: UIState, action: UIAction): UIState => {
  switch (action.type) {
    case 'SET_LOADING':
      return { ...state, isLoading: action.payload };
    case 'SET_ERROR':
      return { ...state, error: action.payload };
    case 'SET_CURRENT_USER':
      return { ...state, currentUser: action.payload };
    case 'SET_TASKS':
      return { ...state, tasks: action.payload };
    case 'ADD_TASK':
      return { ...state, tasks: [action.payload, ...state.tasks] };
    case 'UPDATE_TASK':
      return {
        ...state,
        tasks: state.tasks.map(task =>
          task.id === action.payload.id ? action.payload : task
        ),
      };
    case 'DELETE_TASK':
      return {
        ...state,
        tasks: state.tasks.filter(task => task.id !== action.payload),
      };
    case 'SET_MODAL':
      return {
        ...state,
        isModalOpen: action.payload.isOpen,
        currentModalType: action.payload.type,
        currentModalData: action.payload.data || null,
      };
    case 'SET_TASK_FILTER':
      return {
        ...state,
        taskFilters: { ...state.taskFilters, ...action.payload }
      };
    default:
      return state;
  }
};

export const UIProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(uiReducer, initialState);

  return (
    <UIContext.Provider value={{ state, dispatch }}>
      {children}
    </UIContext.Provider>
  );
};

export const useUI = () => {
  const context = useContext(UIContext);
  if (!context) {
    throw new Error('useUI must be used within a UIProvider');
  }
  return context;
};