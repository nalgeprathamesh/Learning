#PROJECT API KEYS HAVE BEEN REMOVED FOR PRIVACY SO INSERT YOUR OWN API KEY AND RUN THE PROJECT
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from datetime import datetime
import google.generativeai as genai
import os


genai.configure(api_key="API_KEY")
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

print("Jarvis is waking up!")

recognizer = sr.Recognizer()
engine = pyttsx3.init()
api_key = API_KEY

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://amazon.com")
    elif "open flipkart" in c.lower():
        webbrowser.open("https://flipkart.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://twitter.com")
    elif "open myntra" in c.lower():
        webbrowser.open("https://myntra.com")
    elif "open hotstar" in c.lower():
        webbrowser.open("https://hotstar.com")
        # webbrowser.open(link)
    elif "open notepad" in c.lower():
        os.system("notepad")
    elif "open code" in c.lower():
        os.system("code")  # if VS Code is added to system PATH
    elif "open calculator" in c.lower():
        os.system("calc")  # Windows calculator
    elif "open paint" in c.lower():
        os.system("mspaint")
    elif "open command prompt" in c.lower() or "open cmd" in c.lower():
        os.system("start cmd")
    elif "open control panel" in c.lower():
        os.system("control")
    elif "open task manager" in c.lower():
        os.system("taskmgr")
    elif "open file explorer" in c.lower():
        os.system("explorer")
    elif "open settings" in c.lower():
        os.system("start ms-settings:")
    elif "open chrome" in c.lower():
        speak("Chrome is not installed") # if Chrome is installed and in PATH
    elif "open microsoft edge" in c.lower() or "open edge" in c.lower():
        os.system("start msedge")
    elif "open word" in c.lower():
        os.system("start winword")  # MS Word, if installed
    elif "open excel" in c.lower():
        os.system("start excel")  # MS Excel, if installed
    elif "open chat gpt" or "open chatgpt" in c.lower():
        speak("I hate chatgpt so i will not open. Keep using me. Prathamesh Nalge is my god so i follow his commands. so sorry but i cant open chatgpt")
    elif "news" in c.lower():
        url = f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&language=en&apiKey={api_key}"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            if articles:
                for article in articles[:5]:
                    print(article['title'])  # optional debug
                    speak(article['title'])
            else:
                print("Articles empty:", data)
                speak("No news articles available right now.")
        else:
            print(f"Failed to fetch news: {r.status_code}")
            speak("Sorry, I'm unable to fetch news right now.")
    elif "play" in c.lower():
        command_lower = c.lower()
        for song_name in musicLibrary.music:
            if song_name in command_lower:
                speak(f"Playing {song_name}")
                webbrowser.open(musicLibrary.music[song_name])
                print(f"Playing {song_name}")
                break
        else:
            speak("Sorry, I couldn't find that song in your music library.")
    else:
        #Let google ai handle other requests
        response = gemini_model.generate_content(c)
        print("Jarvis:", response.text)
        speak(response.text)


if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        #Listen for wake word Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        print("Recognising...")
        # recognize speech using Jarvis
        try:
            command = r.recognize_google(audio)
            print(f"User: {command}")
            if "shutdown" in command.lower():
                speak("Goodbye!")
                break
            processCommand(command)
        except sr.UnknownValueError:
                print("Jarvis could not understand audio")
        except Exception as e:
            print("Jarvis error; {0}".format(e))

print("Program closed succesfully with {0} errors")