from ollama import chat


class OllamaService:

    def ask(self, model, messages):

        response = chat(
            model=model,
            messages=messages
        )

        return response.message.content