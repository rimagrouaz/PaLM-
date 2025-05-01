from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client(api_key="AIzaSyCKUEncSveW66mkjJUTjKLiPpAaRvd-OHQ")

contents = ('Une maison futuriste flottant au-dessus des nuages, au coucher du soleil, style science-fiction')

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(
      response_modalities=['TEXT', 'IMAGE']
    )
)

for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO((part.inline_data.data)))
    image.save('gemini-image.png')
    image.show()