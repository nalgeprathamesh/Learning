# Combining uses of 2 module and getting a random joke from pyjoke and then converting it into tts

import pyjokes
import pyttsx3

joke = pyjokes.get_joke()
print(joke)
engine = pyttsx3.init()
engine.say(joke)
engine.runAndWait()
