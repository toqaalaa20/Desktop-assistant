# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 22:04:06 2022

@author: Toqa Alaa
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
listener = sr.Recognizer()
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):  
    engine.say(text)
    engine.runAndWait()
    
    
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening........")
            voice= listener.listen(source)
            command= listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command= command.replace('siri', '')       
    except:    
        pass   
    
    return command 
    
def run_siri():
    command= take_command()
    print(command)
    if 'play' in command:
        song= command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(f'Current time is{time}')
    elif 'day' in command:
        day=datetime.datetime.today().strftime("%d")
        talk(f'Today is {day}')
    elif 'google' in command or 'who is' in command:
        search= command.replace('google','')
        result= wikipedia.summary(search,1)
        talk(result)
    elif 'joke' in command:
        joke= pyjokes.get_joke('en', 'neutral')
        print(joke)
        talk(joke)
    elif 'open' in command: 
        if 'facebook' in command:
            webbrowser.open_new('https://www.facebook.com/')   
        if 'youtube' in command:
            webbrowser.open('https://www.youtube.com')
        if 'instagram' in command:
            webbrowser.open('https://www.instagram.com/')
        if 'github' in command:
            webbrowser.open('https://github.com/')
    elif 'bye' in command:
        talk('Bye, see you again')
        exit()
    else:
        talk('please say it again')
    
 
while True:
    
    run_siri()
    