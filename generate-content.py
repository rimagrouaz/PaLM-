from google import genai

client = genai.Client(api_key="your_api_key")

myfile = client.files.upload(file="gemini-native-image.png")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[myfile, "Caption this image."])

print(response.text)
