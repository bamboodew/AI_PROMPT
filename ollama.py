from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

response = client.chat.completions.create(
    model="qwen2:7b", messages=[{"role": "user", "content": "hello"}]
)
print(response.choices[0].message.content)