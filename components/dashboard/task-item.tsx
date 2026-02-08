'use client'

import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { formatPriority } from '@/lib/utils'
import { Task } from '@/types'
import { CheckIcon, PencilIcon, TrashIcon } from 'lucide-react'
import { motion } from 'framer-motion'
import { formatDateConsistently, formatRelativeTime } from '@/utils/date-utils'

interface TaskItemProps {
  task: Task;
  onToggleComplete: (id: string) => void;
  onEdit: (task: Task) => void;
  onDelete: (task: Task) => void;
}

export function TaskItem({ task, onToggleComplete, onEdit, onDelete }: TaskItemProps) {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  const handleDelete = () => {
    onDelete(task);
  };

  return (
    <motion.div
      layout
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      transition={{ duration: 0.2 }}
    >
      <Card className={`p-4 ${task.completed ? 'opacity-70' : ''}`}>
        <div className="flex items-start gap-3">
          <Button
            variant="outline"
            size="icon"
            className={`h-5 w-5 mt-1 flex-shrink-0 ${task.completed ? 'bg-green-500 text-white' : ''}`}
            onClick={() => onToggleComplete(task.id)}
            aria-label={task.completed ? 'Mark as incomplete' : 'Mark as complete'}
          >
            {task.completed && <CheckIcon className="h-4 w-4" />}
          </Button>

          <div className="flex-1 min-w-0">
            <div className="flex items-center gap-2">
              <h3 className={`font-medium truncate ${task.completed ? 'line-through' : ''}`}>
                {task.title}
              </h3>
              <span className={`text-xs px-2 py-0.5 rounded-full ${
                task.priority === 'high' ? 'bg-red-100 text-red-800' :
                task.priority === 'medium' ? 'bg-yellow-100 text-yellow-800' :
                'bg-green-100 text-green-800'
              }`}>
                {formatPriority(task.priority)}
              </span>
            </div>

            {task.description && (
              <p className="text-sm text-muted-foreground mt-1 truncate">
                {task.description}
              </p>
            )}

            {task.dueDate && (
              <p className="text-xs text-muted-foreground mt-1">
                Due: {mounted ? formatDateConsistently(task.dueDate) : <span>&nbsp;</span>}
              </p>
            )}

            <p className="text-xs text-muted-foreground mt-1">
              Created: {mounted ? formatRelativeTime(task.createdAt) : <span>&nbsp;</span>}
              {task.completedAt && ` • Completed: ${mounted ? formatRelativeTime(task.completedAt) : <span>&nbsp;</span>}`}
            </p>
          </div>

          <div className="flex gap-1">
            <Button
              variant="ghost"
              size="icon"
              onClick={() => onEdit(task)}
              aria-label="Edit task"
            >
              <PencilIcon className="h-4 w-4" />
            </Button>
            <Button
              variant="ghost"
              size="icon"
              onClick={handleDelete}
              aria-label="Delete task"
            >
              <TrashIcon className="h-4 w-4" />
            </Button>
          </div>
        </div>
      </Card>
    </motion.div>
  );
}