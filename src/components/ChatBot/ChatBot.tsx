'use client';

import React, { useState, useEffect, useRef } from 'react';
import './ChatBot.css';
import { apiClient } from '../../services/apiClient';

interface ChatMessage {
  id: string | number;
  text: string;
  sender: 'user' | 'ai' | 'system';
  timestamp: Date;
  actions?: Array<{
    action: string;
    details?: any;
  }>;
}

interface ChatBotProps {
  userId: string;
  isOpen: boolean;
  onClose: () => void;
}

const ChatBot: React.FC<ChatBotProps> = ({ userId, isOpen, onClose }) => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [conversationId, setConversationId] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Load conversation history when component mounts or conversationId changes
  useEffect(() => {
    if (conversationId) {
      loadConversationHistory();
    }
  }, [conversationId]);

  // Scroll to bottom of messages
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const loadConversationHistory = async () => {
    // In a real implementation, we would fetch the conversation history from the backend
    // For now, we'll simulate loading by showing a welcome message if no messages exist
    if (messages.length === 0) {
      const welcomeMessage: ChatMessage = {
        id: 'welcome',
        text: "Welcome back! I'm your AI task assistant. How can I help you today?",
        sender: 'ai',
        timestamp: new Date()
      };
      setMessages([welcomeMessage]);
    }
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSend = async () => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage: ChatMessage = { id: Date.now(), text: inputValue, sender: 'user', timestamp: new Date() };
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Send message to backend
      const response = await apiClient.sendMessage(userId, {
        message: inputValue,
        conversation_id: conversationId
      });

      // Update conversation ID if new conversation was created
      if (response.conversation_id && !conversationId) {
        setConversationId(response.conversation_id);
      }

      // Add AI response to messages
      const aiMessage: ChatMessage = {
        id: Date.now() + 1,
        text: response.response,
        sender: 'ai',
        actions: response.actions_performed,
        timestamp: new Date()
      };

      setMessages(prev => [...prev, aiMessage]);

      // Show any error if present in response
      if (response.error) {
        const errorMessage: ChatMessage = {
          id: Date.now() + 2,
          text: `Error: ${response.error}`,
          sender: 'system',
          timestamp: new Date()
        };
        setMessages(prev => [...prev, errorMessage]);
      }
    } catch (error: any) {
      const errorMessage: ChatMessage = {
        id: Date.now() + 2,
        text: `Error: ${error.message || 'Failed to send message'}`,
        sender: 'system',
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  if (!isOpen) return null;

  return (
    <div className="chatbot-container">
      <div className="chatbot-header">
        <h3>AI Task Assistant</h3>
        <button className="close-button" onClick={onClose}>×</button>
      </div>
      <div className="chatbot-messages">
        {messages.length === 0 ? (
          <div className="welcome-message">
            <p>Hello! I'm your AI task assistant. You can ask me to:</p>
            <ul>
              <li>Add tasks: "Add a task to buy groceries"</li>
              <li>List tasks: "Show me my tasks"</li>
              <li>Complete tasks: "Complete the meeting prep task"</li>
              <li>Delete tasks: "Remove the old task"</li>
              <li>Update tasks: "Change the meeting task to tomorrow"</li>
            </ul>
          </div>
        ) : (
          messages.map((message) => (
            <div key={message.id} className={`message ${message.sender}`}>
              <div className="message-content">
                <p>{message.text}</p>
                {message.actions && message.actions.length > 0 && (
                  <div className="actions-performed">
                    <small>Actions performed:</small>
                    <ul>
                      {message.actions.map((action, index) => (
                        <li key={index}>{action.action}{action.details && ` (${action.details.title || action.details.status})`}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
              <span className="timestamp">{message.timestamp.toLocaleTimeString()}</span>
            </div>
          ))
        )}
        {isLoading && (
          <div className="message ai">
            <div className="message-content">
              <p>Thinking...</p>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      <div className="chatbot-input-area">
        <textarea
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your message here..."
          disabled={isLoading}
        />
        <button onClick={handleSend} disabled={isLoading || !inputValue.trim()}>
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatBot;