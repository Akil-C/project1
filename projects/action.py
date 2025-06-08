import datetime
import speak
import webbrowser
import weather
import os

def handle_command(user_input):
    message = user_input.lower()

    if "your name" in message:
        response = "I am your virtual assistant"
        speak.speak(response)
        return response

    elif any(greet in message for greet in ["hello", "hye", "hay"]):
        response = "Hello! How may I assist you today?"
        speak.speak(response)
        return response

    elif "how are you" in message:
        response = "I'm functioning well, thank you for asking!"
        speak.speak(response)
        return response

    elif "thank" in message:
        response = "You're always welcome, happy to help!"
        speak.speak(response)
        return response

    elif "good morning" in message:
        response = "Good morning! Do you need anything?"
        speak.speak(response)
        return response

    elif "time now" in message or "current time" in message:
        now = datetime.datetime.now()
        current_time = f"{now.hour} Hour : {now.minute} Minute"
        speak.speak(current_time)
        return current_time

    elif any(word in message for word in ["shutdown", "quit", "exit"]):
        response = "Okay, shutting down the system now."
        speak.speak(response)
        return response

    elif "play music" in message or "song" in message:
        url = "https://gaana.com/"
        webbrowser.open(url)
        response = "Opening Gaana for your music. Enjoy!"
        speak.speak(response)
        return response

    elif "open google" in message or "google" in message:
        url = "https://google.com/"
        webbrowser.open(url)
        response = "Opening Google in your browser."
        speak.speak(response)
        return response

    elif "youtube" in message:
        url = "https://youtube.com/"
        webbrowser.open(url)
        response = "Opening YouTube now."
        speak.speak(response)
        return response

    elif "weather" in message:
        forecast = weather.Weather()
        speak.speak(forecast)
        return forecast

    elif "music from my laptop" in message:
        music_path = 'D:\\music'
        files = os.listdir(music_path)
        if files:
            os.startfile(os.path.join(music_path, files[0]))
            response = "Playing music from your device."
        else:
            response = "No music files found in the folder."
        speak.speak(response)
        return response

    else:
        response = "Sorry, I didn't catch that. Could you try again?"
        speak.speak(response)
        return response
