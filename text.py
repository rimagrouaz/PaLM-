from google import genai

client = genai.Client(api_key="AIzaSyCKUEncSveW66mkjJUTjKLiPpAaRvd-OHQ")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Donne-moi 5 idées de projets innovants dans le domaine de l'IA.",
)

print(response.text)