import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import sys
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    # speaks the data as audio output
    engine.say(audio)
    engine.runAndWait()


def wish():
    # decides which wish message should be spoken based on the current time
    hour = int(datetime.datetime.now().hour)
    if 0 < hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    elif 18 <= hour <= 24:
        speak("Good Evening")
    speak("I am Jarvis, How can I help you?")


def take():
    # takes audio through microphone as input an converts it into string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # the non audio duration before speaking something
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Say that again please.....")
        k=1
        return "None"
    return query


if __name__ == '__main__':
    """
    main function
    """
    wish()
    k=1
    while True:
        if(k==1):
            query = take().lower()
            if "wikipedia" in query:
                speak("Searching wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif "youtube" in query:
                webbrowser.open("youtube.com")
            elif "google" in query:
                webbrowser.open("google.com")
            elif "github" in query:
                webbrowser.open("github.com")
            elif "stack overflow" in query:
                webbrowser.open("stackoverflow.com")
            elif "amazon" in query:
                webbrowser.open("amazon.in")
            elif "music" in query:
                music_dir = "C:\\Users\\Sourav\\songs"
                songs = os.listdir(music_dir)
                x = random.randrange(0, 20, 2)
                os.startfile(os.path.join(music_dir, songs[x]))
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")
            elif 'eclipse' in query:
                eclipse = "C:\\Users\\Sourav\\eclipse\\java-2019-12\\eclipse\\eclipse.exe"
                os.startfile(eclipse)
            elif 'close' in query:
                sys.exit()
            elif 'search' in query:
                query = query.replace("search", "")
                webbrowser.open(query)
            elif "thank you" in query:
                speak("You are welcome")