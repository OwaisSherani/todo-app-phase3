# Data Model: Premium, Professional Frontend UI for Todo Web App

**Feature**: 001-premium-frontend-ui
**Date**: 2026-01-04

## Overview

This document defines the data models for the frontend UI of the Todo Web App. Since this is a frontend-only implementation, the data models represent the UI state and data structures that will be managed in the frontend application.

## User Entity

### User
Represents an authenticated user in the UI state.

**Fields**:
- `id`: string - Unique identifier for the user
- `email`: string - User's email address
- `name`: string - User's display name (optional)
- `createdAt`: Date - Account creation timestamp
- `preferences`: UserPreferences - User-specific settings

### UserPreferences
Represents user-specific settings and preferences.

**Fields**:
- `theme`: 'light' | 'dark' | 'system' - UI theme preference
- `notificationsEnabled`: boolean - Whether notifications are enabled
- `taskView`: 'list' | 'grid' - Preferred task display format

## Task Entity

### Task
Represents a todo item in the UI state.

**Fields**:
- `id`: string - Unique identifier for the task
- `title`: string - Task title (required, max 255 characters)
- `description`: string - Detailed task description (optional, max 1000 characters)
- `completed`: boolean - Completion status (default: false)
- `createdAt`: Date - Task creation timestamp
- `updatedAt`: Date - Last update timestamp
- `completedAt`: Date | null - Completion timestamp (null if not completed)
- `dueDate`: Date | null - Optional due date for the task
- `priority`: 'low' | 'medium' | 'high' - Task priority level (default: 'medium')

**Validation Rules**:
- Title must be 1-255 characters
- Description must be 0-1000 characters if provided
- Completed status can only be changed via specific actions
- Due date must be in the future if provided

**State Transitions**:
- `incomplete` → `completed`: When user marks task as complete
- `completed` → `incomplete`: When user unmarks task as complete

## UI State Models

### TaskFilter
Represents the current filtering state for the task list.

**Fields**:
- `status`: 'all' | 'active' | 'completed' - Filter by completion status
- `priority`: 'all' | 'low' | 'medium' | 'high' - Filter by priority
- `searchQuery`: string - Text search filter
- `sortBy`: 'createdAt' | 'updatedAt' | 'dueDate' | 'priority' - Sorting criteria
- `sortOrder`: 'asc' | 'desc' - Sorting order

### UIState
Represents the overall UI state for the application.

**Fields**:
- `currentUser`: User | null - Currently authenticated user
- `tasks`: Task[] - List of tasks for the current user
- `taskFilters`: TaskFilter - Current filtering state
- `isLoading`: boolean - Whether data is currently loading
- `error`: string | null - Any error messages
- `isModalOpen`: boolean - Whether a modal is currently open
- `currentModalType`: 'create' | 'edit' | 'delete' | null - Type of modal open
- `currentModalData`: any - Data associated with the current modal

## Component State Models

### FormState
Represents the state of a form component.

**Fields**:
- `values`: Record<string, any> - Current form field values
- `errors`: Record<string, string> - Field-specific error messages
- `isSubmitting`: boolean - Whether the form is currently submitting
- `submitSuccess`: boolean - Whether the last submission was successful
- `submitError`: string | null - Error from last submission

### ToastState
Represents the state of toast notifications.

**Fields**:
- `id`: string - Unique identifier for the toast
- `message`: string - Toast message content
- `type`: 'success' | 'error' | 'warning' | 'info' - Toast type
- `duration`: number - Duration in milliseconds before auto-dismissal
- `isVisible`: boolean - Whether the toast is currently visible

## API Response Models (Simulated)

Since this is a frontend-only implementation, these represent the expected API response structures that would be used if connecting to a backend.

### AuthResponse
Represents the response from authentication endpoints.

**Fields**:
- `user`: User - The authenticated user object
- `token`: string - Authentication token (simulated for frontend state)

### TaskResponse
Represents the response from task-related endpoints.

**Fields**:
- `task`: Task - The task object
- `message`: string - Success or error message

### TaskListResponse
Represents the response from task list endpoints.

**Fields**:
- `tasks`: Task[] - List of task objects
- `total`: number - Total number of tasks matching filters
- `page`: number - Current page number
- `limit`: number - Number of tasks per page