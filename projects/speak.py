import datetime
import speak
import webbrowser
import weather
import os

def handle_command(user_input):
    query = user_input.lower()

    if "your name" in query:
        response = "I am your virtual assistant."
        speak.speak(response)
        return response

    elif any(greet in query for greet in ["hello", "hye", "hay"]):
        response = "Hi there! How can I help you today?"
        speak.speak(response)
        return response

    elif "how are you" in query:
        response = "I'm functioning perfectly. Thanks for asking!"
        speak.speak(response)
        return response

    elif any(word in query for word in ["thanku", "thank"]):
        response = "It's always a pleasure to assist you!"
        speak.speak(response)
        return response

    elif "good morning" in query:
        response = "Good morning! I'm ready to assist you."
        speak.speak(response)
        return response

    elif "time now" in query or "current time" in query:
        now = datetime.datetime.now()
        time_msg = f"{now.hour} Hour : {now.minute} Minute"
        speak.speak(time_msg)
        return time_msg

    elif any(cmd in query for cmd in ["shutdown", "quit", "exit"]):
        response = "Okay, shutting down now."
        speak.speak(response)
        return response

    elif "play music" in query or "song" in query:
        webbrowser.open("https://gaana.com/")
        response = "Opening Gaana for your music. Enjoy!"
        speak.speak(response)
        return response

    elif "open google" in query or "google" in query:
        webbrowser.open("https://google.com/")
        response = "Google has been opened in your browser."
        speak.speak(response)
        return response

    elif "youtube" in query:
        webbrowser.open("https://youtube.com/")
        response = "Now opening YouTube."
        speak.speak(response)
        return response

    elif "weather" in query:
        weather_info = weather.Weather()
        speak.speak(weather_info)
        return weather_info

    elif "music from my laptop" in query:
        music_folder = 'D:\\music'
        try:
            tracks = os.listdir(music_folder)
            if tracks:
                os.startfile(os.path.join(music_folder, tracks[0]))
                response = "Playing your local music file."
            else:
                response = "No music found in the folder."
        except Exception as e:
            response = f"Error accessing music folder: {e}"
        speak.speak(response)
        return response

    else:
        fallback = "Sorry, I couldn't understand that."
        speak.speak(fallback)
        return fallback
