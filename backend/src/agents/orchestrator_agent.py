import cohere
from typing import Dict, Any, List
from ..config.environment import settings
from mcp import Tool
from ..tools.task_tools import TOOLS


class ChatOrchestratorAgent:
    """
    Orchestrates the AI chatbot interactions by interpreting user input,
    selecting appropriate MCP tools, and generating AI responses.
    """

    def __init__(self):
        # Initialize Cohere client
        self.co = cohere.Client(api_key=settings.cohere_api_key)
        self.tools = TOOLS

    def process_user_message(self, user_message: str, conversation_context: List[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Process a user message and return an AI response with any actions performed.

        Args:
            user_message: The message from the user
            conversation_context: Previous conversation messages for context

        Returns:
            Dictionary containing the AI response and any actions performed
        """
        # Prepare the prompt for the model
        prompt = self._prepare_prompt(user_message, conversation_context)

        # Generate response using Cohere
        response = self.co.chat(
            message=prompt,
            connectors=[{"id": "web-search"}],  # Using connectors if needed
            tools=self.tools,
            model="command-r-plus"  # Using a suitable model for tool use
        )

        # Process the response to extract actions and final response
        processed_result = self._process_response(response)

        return processed_result

    def _prepare_prompt(self, user_message: str, conversation_context: List[Dict[str, str]] = None) -> str:
        """
        Prepare the prompt for the AI model with conversation context.
        """
        if conversation_context:
            context_str = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation_context])
            prompt = f"""
            Conversation context:
            {context_str}

            User's new message: {user_message}

            Please respond appropriately, using tools if the user wants to manage tasks.
            """
        else:
            prompt = f"""
            User's message: {user_message}

            Please respond appropriately, using tools if the user wants to manage tasks.
            """

        return prompt

    def _process_response(self, response: Any) -> Dict[str, Any]:
        """
        Process the AI response to extract actions and format the final response.
        """
        # Extract the text response
        ai_response = response.text

        # Extract any tool calls that were made
        actions_performed = []
        if hasattr(response, 'tool_calls') and response.tool_calls:
            for tool_call in response.tool_calls:
                # Process each tool call and add to actions performed
                action = {
                    "action": tool_call.name,
                    "params": tool_call.parameters,
                    "result": getattr(tool_call, 'result', 'No result available')
                }
                actions_performed.append(action)

        # Return the formatted response
        return {
            "response": ai_response,
            "actions_performed": actions_performed
        }