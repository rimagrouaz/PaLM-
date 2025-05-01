from google import genai

client = genai.Client(api_key="your_api_key")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Ech cn had 3 tenis balls. How many tennis balls does he have now?",
)

print(response.text)
