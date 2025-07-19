import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Dictionary for playing specific songs via YouTube
music = {
    "sea": "https://www.youtube.com/watch?v=RD4DfVxVeqk2o&start_radio=1",
    "yo": "https://www.youtube.com/watch?v=RD4DfVxVeqk2o&index=3",
    "nono": "https://www.youtube.com/watch?v=RD4DfVxVeqk2o&index=10",
    "mark": "https://www.youtube.com/watch?v=RD4DfVxVeqk2o&index=11",
}

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Default system voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower().strip()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")
        
        elif query.startswith('play '):
            song_name = query.replace('play ', '').strip().lower()
            if song_name in music:
                speak(f"Playing {song_name}")
                webbrowser.open(music[song_name])
            else:
                speak("I couldn't find that song in the list. Please try another one.")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            os.system("open -a 'Visual Studio Code'")
        
        elif 'quit' in query or 'exit' in query:
            speak("Goodbye, have a great day!")
            break

        else:
            print("No command matched.")
