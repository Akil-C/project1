import speech_recognition as sr
from requests_html import HTMLSession  # Optional if not used directly
import speak

def capture_voice_input():
    recognizer = sr.Recognizer()
    voice_result = ""

    with sr.Microphone() as mic:
        speak.speak("Listening now...")
        audio_input = recognizer.listen(mic)

        try:
            voice_result = recognizer.recognize_google(audio_input)
            return voice_result

        except sr.UnknownValueError:
            speak.speak("Apologies, I couldn't understand that.")
        except sr.RequestError:
            speak.speak("Network issue detected. Please check your internet connection.")
           