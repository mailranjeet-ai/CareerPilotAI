from utils.file_loader import load_prompt
from models.conversation import Conversation
from services.ollama_service import OllamaService
from agents.career_agent import CareerAgent

agent = CareerAgent()

print("=== Welcome to CareerPilot AI ===")
print("Type 'exit' to quit.\n")

conversation = Conversation(
    load_prompt("career_assistant.txt")
)

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    conversation.add_user_message(question)

    answer = agent.process(
    question,
    conversation
)

    print("\nQwen:")
    print(answer)

    conversation.add_assistant_message(answer)

    print()