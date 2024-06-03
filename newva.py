import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print(f"SPEAK: {audio}")  # Debug print statement
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Mam!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Mam!")
    else:
        speak("Good Evening Mam!")
    assname = ("Poooja")
    speak("I am your Assistant")
    speak(assname)

def username():
    speak("What should I call you, mam?")
    uname = input("Enter your name: ")  # For debugging
    speak("Welcome Miss")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    
    print("#####################".center(columns))
    print(f"Welcome, {uname}".center(columns))
    print("#####################".center(columns))
    
    speak("How can I help you, mam")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak("Unable to Recognize your voice.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("Unable to Recognize your voice.")
        return "None"
    except Exception as e:
        print(e)
        speak("Unable to Recognize your voice.")
        return "None"
    
    return query

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # Enable low security in gmail
        server.login('your email id', 'your email password')
        server.sendmail('your email id', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("I am not able to send this email")

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()
    
    while True:
        query = takeCommand().lower()

        if query == "none":
            continue
        
        print(f"Processing query: {query}")  # Debug print statement

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow. Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "C:\\Users\\GAURAV\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")

        elif 'email to bindu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Whome should I send")
                to = input("Enter the recipient email address: ")
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Mam")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you're fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Mam?")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you":
            speak("I have been created by Gaurav.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely you are human.")

        elif "why you came to world" in query:
            speak("Thanks to Bindu. further It's a secret")

        elif 'power point presentation' in query:
            speak("Opening Power Point presentation")
            power = r"C:\Users\bindu\OneDrive\Documents\Internship"
            os.startfile(power)

        elif 'is love' in query:
            speak("It is 7th sense that destroys all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Bindu")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Bindu")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully")

        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)

        elif 'news' in query:
            try:
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('Here are some top news from the times of India')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'])
                    i += 1
            except Exception as e:
                print(str(e))

        elif 'lock window' in query:
            speak("Locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec! Your system is on its way to shut down")
            subprocess.call('shutdown /p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin emptied")

        elif "don't listen" in query or "stop listening" in query:
            speak("For how much time you want to stop jarvis from listening commands?")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Bindu Camera", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown /h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the applications are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should I write, Mam?")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Mam, Should I include date and time?")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
            file.close()

        elif "show note" in query:
            speak("Showing Notes")
            file = open("poooja.txt", "r")
            content = file.read()
            print(content)
            speak(content)
            file.close()

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:
                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        elif "Poooja" in query:
            wishMe()
            speak("Poooja in your service Mam")
            speak(assname)

        elif "weather" in query:
            api_key = "Api key"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("City name")
            print("City name: ")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(current_temperature) +
                      "\n atmospheric pressure (in hPa unit) =" + str(current_pressure) +
                      "\n humidity (in percentage) = " + str(current_humidity) +
                      "\n description = " + str(weather_description))
                speak(" Temperature in kelvin unit is " + str(current_temperature) +
                      "\n atmospheric pressure in hPa unit is " + str(current_pressure) +
                      "\n humidity in percentage is " + str(current_humidity) +
                      "\n description is " + str(weather_description))
            else:
                speak("City Not Found")

        elif "send message" in query:
            # You need to create an account on Twilio to use this service
            account_sid = 'Account Sid key'
            auth_token = 'Auth token'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=takeCommand(),
                from_='Sender No',
                to='Receiver No'
            )

            print(message.sid)

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you?")
            speak(assname)

        elif "will you be my gf" in query or "will you be my bf":
            speak("I'm not sure about that, maybe you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you asked me that")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                result = next(res.results).text
                print(result)
                speak(result)
            except StopIteration:
                print("No results")
