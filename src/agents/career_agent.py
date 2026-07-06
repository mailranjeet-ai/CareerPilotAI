from services.ollama_service import OllamaService
from tools.tool_registry import ToolRegistry


class CareerAgent:
    """
    Main AI Agent for CareerPilot AI.

    Responsibilities:
    - Decide whether to use a tool.
    - Execute the appropriate tool.
    - Ask the LLM for normal conversations.
    """

    def __init__(self):
        self.ollama = OllamaService()
        self.registry = ToolRegistry()

    def process(self, question, conversation):

        question = question.strip().lower()

        # ---------- Tool Execution ----------

        if self.registry.has_tool(question):

            result = self.registry.execute(question)

            if isinstance(result, list):

                if not result:
                    return "No files found."

                return "\n".join(result)

            return result

        # ---------- Normal AI Conversation ----------

        return self.ollama.ask(
            model="qwen3:8b",
            messages=conversation.get_messages()
        )