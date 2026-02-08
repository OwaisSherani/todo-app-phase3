/**
 * Utility functions for consistent date formatting between server and client
 */

/**
 * Formats a date consistently regardless of timezone
 */
export function formatDateConsistently(dateString: string): string {
  // Parse the date string and create a UTC date to ensure consistency
  const date = new Date(dateString);
  
  // Format as "Month DD, YYYY" in a timezone-independent way
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    timeZone: 'UTC'
  });
}

/**
 * Formats a date for display with time in a timezone-independent way
 */
export function formatDateTimeConsistently(dateString: string): string {
  const date = new Date(dateString);
  
  return `${date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    timeZone: 'UTC'
  })} at ${date.toLocaleTimeString('en-US', {
    hour: '2-digit',
    minute: '2-digit',
    timeZone: 'UTC'
  })}`;
}

/**
 * Checks if a date is today in the user's timezone
 */
export function isToday(dateString: string): boolean {
  const date = new Date(dateString);
  const today = new Date();
  
  return date.getDate() === today.getDate() &&
         date.getMonth() === today.getMonth() &&
         date.getFullYear() === today.getFullYear();
}

/**
 * Checks if a date is yesterday in the user's timezone
 */
export function isYesterday(dateString: string): boolean {
  const date = new Date(dateString);
  const yesterday = new Date();
  yesterday.setDate(yesterday.getDate() - 1);
  
  return date.getDate() === yesterday.getDate() &&
         date.getMonth() === yesterday.getMonth() &&
         date.getFullYear() === yesterday.getFullYear();
}

/**
 * Formats a date as relative time (e.g., "Today", "Yesterday", "2 days ago")
 */
export function formatRelativeTime(dateString: string): string {
  const date = new Date(dateString);
  const now = new Date();
  
  // Calculate the difference in days
  const diffTime = Math.abs(now.getTime() - date.getTime());
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  
  if (isToday(dateString)) {
    return 'Today';
  } else if (isYesterday(dateString)) {
    return 'Yesterday';
  } else if (diffDays === 1) {
    return '1 day ago';
  } else if (diffDays < 7) {
    return `${diffDays} days ago`;
  } else {
    return formatDateConsistently(dateString);
  }
}