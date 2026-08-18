import speech_recognition as sr
import pyttsx3
import time

from researcher import chat_with_history


recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("\n🎙️ Listening...")

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return None

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text

    except sr.UnknownValueError:
        print("I couldn't understand that.")
        return None

    except sr.RequestError as e:
        print("Speech recognition error:", e)
        return None


def speak(text):
    print("AI:", text)

    # Create a fresh speech engine for every response
    speaker = pyttsx3.init()

    speaker.say(text)
    speaker.runAndWait()

    # Properly shut down the engine
    speaker.stop()

    del speaker

    # Small pause before microphone starts again
    time.sleep(0.5)


history = []

print("🎙️ Voice Assistant Started")
print("Say 'exit', 'quit', or 'stop' to end.\n")


while True:

    message = listen()

    if not message:
        continue

    if message.lower().strip() in ["exit", "quit", "stop"]:
        print("Voice assistant stopped.")
        break

    response = chat_with_history(
        message,
        history
    )

    speak(response)

    history.append({
        "role": "user",
        "content": message
    })

    history.append({
        "role": "assistant",
        "content": response
    })