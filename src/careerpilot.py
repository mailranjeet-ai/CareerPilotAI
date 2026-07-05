from ollama import chat

def load_system_prompt():
    with open(
        "src/prompts/career_assistant.txt",
        "r",
        encoding="utf-8"
    ) as file:
        return file.read()

print("=== Welcome to CareerPilot AI ===")
print("Type 'exit' to quit.\n")

conversation = [
    {
        "role": "system",
        "content": load_system_prompt()
    }
]

while True:
    question = input("You: ")
    conversation.append(
    {
        "role": "user",
        "content": question
    }
    )
    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = chat(
        model="qwen3:8b",
        messages=conversation
    )

    print("\nQwen:")
    print(response.message.content)
    conversation.append(
    {
        "role": "assistant",
        "content": response.message.content
    }
    )
    print()