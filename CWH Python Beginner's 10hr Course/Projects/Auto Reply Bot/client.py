#PROJECT API KEYS HAVE BEEN REMOVED FOR PRIVACY SO INSERT YOUR OWN API KEY AND RUN THE PROJECT
#This is just for testing
from google import generativeai as genai

# Initialize the Gemini client with your API key
genai.configure(api_key="API_KEY")  # Replace with your actual key

# Create the client (no need for `client = genai.Client(...)`)
model = genai.GenerativeModel("gemini-2.0-flash")

command = '''
[8:35 AM, 6/14/2025] Prathamesh Nalge: 74477 22398
[9:21 AM, 6/14/2025] Pradeep Nalge: Hi
[9:21 AM, 6/14/2025] Pradeep Nalge: Hello
[9:21 AM, 6/14/2025] Pradeep Nalge: Bring
[9:21 AM, 6/14/2025] Pradeep Nalge: Onion
[9:21 AM, 6/14/2025] Pradeep Nalge: Potato
[9:21 AM, 6/14/2025] Pradeep Nalge: Carrot
[9:21 AM, 6/14/2025] Pradeep Nalge: Order on
[9:21 AM, 6/14/2025] Pradeep Nalge: Blinkit
'''
# Define the prompt with a strict personality
response = model.generate_content(
    contents=[
        {
            "role": "user",
            "parts": ["You are Prathamesh, an 17yr old boy from india who is passionate about Programming. Your role is to reply to messages(in short like real whatsapp messages) posted by him. You are an human. Make it feel like actual human dont make it too lomg or Aiish. Reply to all the whatsapp messages in one go... donnt mention time and stuff just reply to all message in one mega message"]
        },
        {
            "role": "user",
            "parts": [command]
        }
    ]
)

# Print the output from Prathamesh
print("Prathamesh:", response.text)
