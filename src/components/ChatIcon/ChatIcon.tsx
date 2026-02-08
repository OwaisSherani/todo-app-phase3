'use client';

import React, { useState } from 'react';
import './ChatIcon.css';

interface ChatIconProps {
  onClick: () => void;
}

const ChatIcon: React.FC<ChatIconProps> = ({ onClick }) => {
  const [isVisible, setIsVisible] = useState(true);

  const handleClick = () => {
    setIsVisible(false);
    onClick();
  };

  if (!isVisible) {
    return null;
  }

  return (
    <div className="chat-icon-container" onClick={handleClick}>
      <div className="chat-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M21 15C21 15.5304 20.7893 16.0391 20.4142 16.4142C20.0391 16.7893 19.5304 17 19 17H17L14.25 20.75C14.05 21 13.7 21.05 13.5 20.75C13.3 20.5 13.25 20.1 13.5 19.9L15.75 16.75H13C12.4696 16.75 11.9609 16.5393 11.5858 16.1642C11.2107 15.7891 11 15.2804 11 14.75V5.25C11 4.71957 11.2107 4.21086 11.5858 3.83579C11.9609 3.46071 12.4696 3.25 13 3.25H18C18.5304 3.25 19.0391 3.46071 19.4142 3.83579C19.7893 4.21086 20 4.71957 20 5.25V15Z" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          <path d="M7 8.25H12M7 11.75H12M7 15.25H10" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
        </svg>
      </div>
    </div>
  );
};

export default ChatIcon;