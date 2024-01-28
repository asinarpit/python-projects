from ast import main
from tkinter.tix import MAIN
from xml.dom.pulldom import default_bufsize
import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
# import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir.")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir.")
    else:
        speak("Good evening sir.")

    speak('I am Raven. How may I help you?')    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing audio...\n")
        query =  r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")

    except Exception as e:
        print("Say that again please...\n")
        return "None"

    return query

def sendEmail(to, content):
    pass

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching in Wikipedia......')
            # query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(f'Raven: {result}')
            speak(result)

        elif 'open youtube' in query:
            speak("Opening youtube....")
            print("Raven: Opening Youtube....")
            webbrowser.open('youtube.com')

        elif 'open visual code' in query:
            speak("Opening Visual code...")
            print("Raven: Opening Visual Code...")
            path = "C:\\Users\\asin0\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'play music' in query:
            music_direc = "D:\\Music"
            print("Playing music....")
            os.startfile(music_direc)

        elif 'open pycharm' in query:
            speak("Opening pycharm...")
            print("Opening pycharm...")
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.1.3\\bin\\pycharm64.exe"
            os.startfile(path)

        
