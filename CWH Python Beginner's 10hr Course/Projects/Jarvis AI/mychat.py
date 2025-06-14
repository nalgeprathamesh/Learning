#PROJECT API KEYS HAVE BEEN REMOVED FOR PRIVACY
import google.generativeai as genai

genai.configure(api_key="API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-pro"
response = model.generate_content("Explain how AI works in a few words.")

print(response.text)
