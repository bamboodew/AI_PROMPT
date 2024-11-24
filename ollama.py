from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)


def chat():
    messages = []
    print("\nChat started. Type 'exit' or 'end' to finish the conversation.\n")

    while True:
        # Get user input
        user_input = input("😀: ").strip()

        # Check for exit conditions
        if user_input.lower() in ["exit", "end"]:
            print("\nChat ended. Goodbye!")
            break

        # Add user message to history
        messages.append({"role": "user", "content": user_input})

        # Get AI response
        response = client.chat.completions.create(model="qwen2:7b", messages=messages)

        # Get and print AI response
        ai_message = response.choices[0].message.content
        print(f"🤖: {ai_message}\n")

        # Add AI response to history
        messages.append({"role": "assistant", "content": ai_message})


if __name__ == "__main__":
    chat()
