# GPT-OSS-20B-Tars: Voice-Activated Chatbot
Note: I could not really add Tars as an activation word, my microphone did not quite pick it up well. Maybe some awesome poeple out there might fix this ;) 
It runs pretty good on my RTX3060.

This project lets you interact with the `gpt-oss:20b` model using your voice, with wake-word activation ("Machine") and spoken responses. It runs locally but can be adapted for online use with proper server and microphone/browser support.

## Features
- Wake word detection: Say "Machine" to activate.
- Voice-to-text: Speak your prompt after the wake word.
- Model interaction: Sends your prompt to the `gpt-oss:20b` model via Ollama.
- Text-to-speech: The model's answer is read aloud.

## Requirements
- Python 3.8+
- [Ollama](https://ollama.com/) installed and running
- Microphone and speakers
- Linux (for other OS, adjust dependencies as needed) --> I currently tested in only on Linux Ubunutu 24.04 

### Python dependencies
- `pyttsx3` (text-to-speech)
- `speechrecognition` (voice input)
- `pyaudio` (microphone access)

Install them with:
```bash
sudo apt-get update
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyttsx3 speechrecognition pyaudio
```
Or install the python pacakges with:
```bash
pip install -r requirements.txt‚
```

## Usage
1. Start Ollama and ensure the `gpt-oss:20b` model is available.
2. Run the script:
   ```bash
   python3 chat_with_me.py
   ```
3. Say "Machine" to activate, then speak your prompt after the beep.
4. The model will answer and read the response aloud.
5. Say "exit" or "quit" to stop.

## Troubleshooting
- If you get a `PyAudio` error, make sure `portaudio19-dev` and `python3-pyaudio` are installed.
- For microphone issues, check your system's audio settings and permissions. I used a cheap Microphone, and well the results where not the best, but sometimes it got what i said really good. 


