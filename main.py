import speech_recognition as sr
import pyttsx3
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio_data = recognizer.listen(source)
        print("Recognizing...")
        try:
            text = recognizer.recognize_google(audio_data)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def open_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def open_news(query):
    url = f"https://www.google.com/search?q={query}&tbm=nws"
    webbrowser.open(url)

def main():
    speak("Hello, I am your voice assistant. How can I help you?")
    command = recognize_speech()
    if command:
        if "youtube" in command:
            speak("What do you want to search on YouTube?")
            search_query = recognize_speech()
            if search_query:
                speak(f"Opening YouTube for {search_query}")
                open_youtube(search_query)
        elif "news" in command:
            speak("What news topic are you interested in?")
            search_query = recognize_speech()
            if search_query:
                speak(f"Searching news for {search_query}")
                open_news(search_query)
        else:
            speak("Sorry, I didn't understand. Please say 'YouTube' or 'news'.")

if _name_ == "_main_":
    main()