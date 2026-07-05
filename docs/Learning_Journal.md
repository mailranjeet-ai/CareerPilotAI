CareerPilot AI Bootcamp - Learning Journal
Day 1 - Building the Foundation of CareerPilot AI
Objective
Set up the development environment and build the first working version of CareerPilot AI that communicates with a locally running LLM.

Concepts Learned
1. Generative AI vs LLM vs AI Agent
• Generative AI creates text, code and images.
• Qwen3:8B is the Large Language Model (LLM).
• An AI Agent combines an LLM with memory, tools and workflows.

Key Learning:
LLMs think. Agents act.

2. Ollama
• Ollama is a local runtime/server.
• It loads and serves the Qwen model.

Architecture:
User → Python → Ollama → Qwen3:8B → Response

3. Python Virtual Environment
• Created a dedicated .venv.
• Keeps project dependencies isolated.

4. Conversation Memory
• LLMs do not remember previous conversations.
• The application stores and resends conversation history.

5. System Prompt
• Created career_assistant.txt.
• Separated prompt configuration from Python code.

6. Prompt Engineering
• Identity
• Behaviour
• Formatting
• Responsibilities

7. Software Engineering
• Separate configuration from code.
• Build modular applications.
• Understand architecture before coding.
What I Built
• Local AI Assistant
• Interactive Console Chat
• Conversation Memory
• External System Prompt
• Prompt Loader
• Local LLM Communication







Architecture

User
 ↓
CareerPilot.py
 ↓
Conversation Memory
 ↓
career_assistant.txt
 ↓
Ollama
 ↓
Qwen3:8B
 ↓
Response


Tools Used
• Python 3.14
• VS Code
• Git
• Ollama
• Qwen3:8B
Project Structure
CareerPilotAI/
└── src/
    ├── careerpilot.py
    └── prompts/
        └── career_assistant.txt

Key Takeaways
• An LLM is only one component of an AI application.
• Ollama is a runtime, not the model.
• Memory belongs to the application.
• System prompts define assistant behaviour.
• Prompt engineering is a core AI engineering skill.
• Good architecture matters.

Challenges Faced
• Initial Python to Ollama connection issue.
• Learned structured debugging of runtime and client.

Progress
✅ Environment Setup
✅ Local AI Communication
✅ Conversation Memory
✅ System Prompt
✅ Interactive AI Assistant


Goals for Day 2
• Refactor into a modular architecture.
• Build reusable services.
• Introduce AI tools.
• Prepare for browser automation.
Personal Reflection
Today I built my first AI application running entirely on my own laptop. I now understand how Python, Ollama, prompts, conversation memory and Qwen work together. The biggest lesson was that memory belongs to the application, not the LLM.
=========================================================================
