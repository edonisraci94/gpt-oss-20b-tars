



import subprocess
import json
import pyttsx3
import speech_recognition as sr


def pull_gpt_oss_20b():
    """Pull the gpt-oss:20b model using ollama."""
    try:
        result = subprocess.run([
            "ollama", "pull", "gpt-oss:20b"
        ], check=True, capture_output=True, text=True)
        print("Model pulled successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Failed to pull model:")
        print(e.stderr)




def remove_chain_of_thought(text):
    """Extract only the text after '...done thinking.' if present."""
    marker = '...done thinking.'
    idx = text.lower().find(marker)
    if idx != -1:
        # Return everything after the marker
        return text[idx + len(marker):].strip()
    return text.strip()

def chat_with_model(prompt):
    """Send a prompt to the gpt-oss:20b model using ollama and return the response."""
    try:
        result = subprocess.run([
            "ollama", "run", "gpt-oss:20b", prompt
        ], check=True, capture_output=True, text=True)
        response = result.stdout.strip()
        print("Model response:")
        print(response)
        filtered = remove_chain_of_thought(response)
        return filtered
    except subprocess.CalledProcessError as e:
        print("Failed to get response from model:")
        print(e.stderr)
        return None






def listen_for_wake_word(wake_word="tars"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print(f"Say '{wake_word}' to start talking to the model. Say 'exit' or 'quit' to stop.")
    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for wake word...")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            print(f"Heard: {text}")
            if text.strip() in ("exit", "quit"):
                print("Exiting chat.")
                break
            if wake_word in text:
                print("Wake word detected! Please speak your prompt after the beep.")
                engine.say("I'm listening.")
                engine.runAndWait()
                with mic as source:
                    recognizer.adjust_for_ambient_noise(source)
                    print("Listening for your prompt...")
                    audio = recognizer.listen(source)
                try:
                    prompt = recognizer.recognize_google(audio)
                    print(f"You said: {prompt}")
                    response = chat_with_model(prompt)
                    if response:
                        engine.say(response)
                        engine.runAndWait()
                except sr.UnknownValueError:
                    print("Sorry, I could not understand your prompt.")
                    engine.say("Sorry, I could not understand your prompt.")
                    engine.runAndWait()
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    pull_gpt_oss_20b()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Lower speed
    engine.setProperty('volume', 0.9)  # Volume level
    voices = engine.getProperty('voices')
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)  # Choose a deeper or more robotic voice if available
    listen_for_wake_word("machine")
