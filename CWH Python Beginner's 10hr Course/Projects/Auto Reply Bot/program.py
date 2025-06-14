#PROJECT API KEYS HAVE BEEN REMOVED FOR PRIVACY SO INSERT YOUR OWN API KEY AND RUN THE PROJECT
import pyautogui
import time
import pyperclip
from google import generativeai as genai

print("Program has initiated")
# Initialize the Gemini client with your API key
genai.configure(api_key="API_KEY")  # Replace with your actual key

# Create the client (no need for `client = genai.Client(...)`)
model = genai.GenerativeModel("gemini-2.0-flash")

# Give some time to switch to the correct window
time.sleep(2)

# Step 1: Click on the icon at (644, 18)
pyautogui.click(644, 18)
time.sleep(1)  # Wait for UI to respond

    #755,520
    # 962,673
# Step 2: Drag from (723, 177) to (1208, 686)
pyautogui.moveTo(755, 520)
pyautogui.mouseDown()
pyautogui.moveTo(962, 673, duration=0.5)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy selected text to clipboard
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Wait for clipboard to update

# Step 4: Get it into a variable
chat_history = pyperclip.paste()
print("Copied Text:", chat_history)

# Open vs code again
# pyautogui.click(571,11)
# time.sleep(1)

response = model.generate_content(
    contents=[
        {
            "role": "user",
            "parts": ["You are Prathamesh, an 17yr old boy from india who is passionate about Programming. Your role is to reply to messages(in short like real whatsapp messages) posted by him. You are an human. Make it feel like actual human dont make it too lomg or Aiish. Reply to all the whatsapp messages in one go... donnt mention time and stuff just reply to all message in one mega message"]
        },
        {
            "role": "user",
            "parts": [chat_history]
        }
    ]
)

# Print the output from Prathamesh
generated_text = response.text
print(generated_text)

time.sleep(5)
# Click and type
pyautogui.click(834, 729)
time.sleep(0.5)
pyautogui.write(generated_text, interval=0.01)

# Click the next button
time.sleep(0.5)
pyautogui.click(1285, 733)