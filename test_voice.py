import pyttsx3

speaker = pyttsx3.init()

print("Testing voice...")

speaker.say("Hello Zamer. This is a voice test.")

speaker.runAndWait()

print("Voice test finished.")