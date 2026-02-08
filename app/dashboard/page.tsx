'use client'

import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button'
import { TaskList } from '@/components/dashboard/task-list'
import { TaskItem } from '@/components/dashboard/task-item'
import { TaskCreateForm } from '@/components/dashboard/task-create-form'
import { EmptyState } from '@/components/ui/empty-state'
import { PlusIcon } from 'lucide-react'
import { Task } from '@/types'
import { ConfirmationDialog } from '@/components/ui/confirmation-dialog'
import { toast } from '@/hooks/use-toast'
import ChatIcon from '@/src/components/ChatIcon/ChatIcon'
import ChatBot from '@/src/components/ChatBot/ChatBot'

// Mock data for initial tasks
const initialTasks: Task[] = [
  {
    id: '1',
    title: 'Complete project proposal',
    description: 'Finish the project proposal document and send to stakeholders',
    completed: false,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    completedAt: null,
    dueDate: new Date(Date.now() + 3 * 24 * 60 * 60 * 1000).toISOString(), // 3 days from now
    priority: 'high'
  },
  {
    id: '2',
    title: 'Schedule team meeting',
    description: 'Schedule a team meeting for next week',
    completed: true,
    createdAt: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(), // 2 days ago
    updatedAt: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
    completedAt: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString(), // 1 day ago
    dueDate: null,
    priority: 'medium'
  },
  {
    id: '3',
    title: 'Review documentation',
    description: 'Review the new API documentation',
    completed: false,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    completedAt: null,
    dueDate: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString(), // 7 days from now
    priority: 'low'
  }
];

export default function DashboardPage() {
  const [tasks, setTasks] = useState<Task[]>(initialTasks);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [taskToEdit, setTaskToEdit] = useState<Task | null>(null);
  const [taskToDelete, setTaskToDelete] = useState<Task | null>(null);
  const [showDeleteDialog, setShowDeleteDialog] = useState(false);
  const [filter, setFilter] = useState<'all' | 'active' | 'completed'>('all');
  const [isChatOpen, setIsChatOpen] = useState(false);

  // In a real app, this would come from the auth context
  // For now, we'll use a mock user ID - in production, get this from your auth provider
  const userId = typeof window !== 'undefined' ? localStorage.getItem('userId') || 'mock-user-id' : 'mock-user-id';

  // Filter tasks based on the selected filter
  const filteredTasks = tasks.filter(task => {
    if (filter === 'active') return !task.completed;
    if (filter === 'completed') return task.completed;
    return true; // 'all'
  });

  const handleCreateTask = (newTask: Omit<Task, 'id' | 'createdAt' | 'updatedAt' | 'completedAt'>) => {
    const task: Task = {
      ...newTask,
      id: Date.now().toString(), // In a real app, this would come from the backend
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      completedAt: null,
    };

    setTasks([task, ...tasks]);
    setShowCreateForm(false);
    toast({
      message: 'Task created',
      description: 'Your task has been created successfully.',
      type: 'success',
      duration: 3000,
      isVisible: true,
    });
  };

  const handleUpdateTask = (updatedTask: Task) => {
    setTasks(tasks.map(task => task.id === updatedTask.id ? updatedTask : task));
    setTaskToEdit(null);
    toast({
      message: 'Task updated',
      description: 'Your task has been updated successfully.',
      type: 'success',
      duration: 3000,
      isVisible: true,
    });
  };

  const handleToggleComplete = (id: string) => {
    setTasks(tasks.map(task => {
      if (task.id === id) {
        const completed = !task.completed;
        return {
          ...task,
          completed,
          completedAt: completed ? new Date().toISOString() : null,
          updatedAt: new Date().toISOString()
        };
      }
      return task;
    }));
  };

  const handleEditTask = (task: Task) => {
    setTaskToEdit(task);
    setShowCreateForm(true);
  };

  const handleDeleteTask = (task: Task) => {
    setTaskToDelete(task);
    setShowDeleteDialog(true);
  };

  const confirmDeleteTask = () => {
    if (taskToDelete) {
      setTasks(tasks.filter(task => task.id !== taskToDelete.id));
      setTaskToDelete(null);
      setShowDeleteDialog(false);
      toast({
        message: 'Task deleted',
        description: 'Your task has been deleted.',
        type: 'error',
        duration: 3000,
        isVisible: true,
      });
    }
  };

  const cancelDeleteTask = () => {
    setTaskToDelete(null);
    setShowDeleteDialog(false);
  };

  const toggleChat = () => {
    setIsChatOpen(!isChatOpen);
  };

  const closeChat = () => {
    setIsChatOpen(false);
  };

  return (
    <div className="container mx-auto max-w-4xl relative">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">My Tasks</h1>
        <Button onClick={() => setShowCreateForm(true)}>
          <PlusIcon className="mr-2 h-4 w-4" />
          Add Task
        </Button>
      </div>

      {showCreateForm && (
        <TaskCreateForm
          onSubmit={taskToEdit ?
            (taskData) => handleUpdateTask({...taskToEdit, ...taskData}) :
            handleCreateTask}
          onCancel={() => {
            setShowCreateForm(false);
            setTaskToEdit(null);
          }}
          task={taskToEdit || undefined}
        />
      )}

      <div className="mb-4 flex space-x-2">
        <Button
          variant={filter === 'all' ? 'default' : 'outline'}
          size="sm"
          onClick={() => setFilter('all')}
        >
          All
        </Button>
        <Button
          variant={filter === 'active' ? 'default' : 'outline'}
          size="sm"
          onClick={() => setFilter('active')}
        >
          Active
        </Button>
        <Button
          variant={filter === 'completed' ? 'default' : 'outline'}
          size="sm"
          onClick={() => setFilter('completed')}
        >
          Completed
        </Button>
      </div>

      {filteredTasks.length === 0 ? (
        <EmptyState
          title="No tasks yet"
          description="Get started by creating a new task."
          action={{
            label: "Create Task",
            onClick: () => setShowCreateForm(true)
          }}
        />
      ) : (
        <TaskList
          tasks={filteredTasks}
          onToggleComplete={handleToggleComplete}
          onEdit={handleEditTask}
          onDelete={handleDeleteTask}
        />
      )}

      <ConfirmationDialog
        isOpen={showDeleteDialog}
        onClose={cancelDeleteTask}
        onConfirm={confirmDeleteTask}
        title="Delete Task"
        description={`Are you sure you want to delete the task "${taskToDelete?.title}"? This action cannot be undone.`}
        confirmText="Delete"
        cancelText="Cancel"
        variant="destructive"
      />

      {/* Chat Icon - appears when chat is closed */}
      {!isChatOpen && (
        <div className="fixed bottom-6 right-6 z-50">
          <ChatIcon onClick={toggleChat} />
        </div>
      )}

      {/* ChatBot Component - appears when chat is open */}
      <ChatBot
        userId={userId}
        isOpen={isChatOpen}
        onClose={closeChat}
      />
    </div>
  );
}