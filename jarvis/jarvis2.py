import pyttsx3
from platform import sys
from pywhatkit.main import search
import requests
import speech_recognition as sr
import datetime
import time
import os
import pywhatkit
from requests import get
import bs4
from bs4 import BeautifulSoup as bs
import wikipedia
import webbrowser
import psutil as ps
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def to_wish():
    hour = int(datetime.datetime.now().hour) 
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good Morning sir, it's {tt}")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon sir, it's {tt}")
    else:
        speak("Good Evening sir, it's {tt}")
    speak("I am Jarvis sir, please tell me How can i help you!!!")

# def battery_percentage():
#     battery = ps.sensors_battery()
#     batt_percentage = battery.percent
#     speak(f"sir our system has {batt_percentage} percent battery")
#     if batt_percentage >= 75:
#         speak("sir we have enough power to continue our work")
#     elif batt_percentage >= 40 and batt_percentage <= 75:
#         speak("sir we should connect our system to charging point to charge our battery")
#     elif batt_percentage <= 15 and batt_percentage <= 30:
#         speak("sir we don't have power to continue our work please connect the charger")
#     elif batt_percentage <= 15:
#         speak("sir we have very low power connect the charger, if u don't do this the system will get turned off very soon")
#     speak("so have great journey")    

def temperature():
    speak("sir which place temperature you want to find")
    temp_search = takecommand()
    search = f"weather in {temp_search}"
    url = f"https://www.google.com/search?&q={search}"
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    update = soup.find("div", class_="BNeawe").text
    speak(f"current temprature in {temp_search} is {update} ")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


if __name__ == "__main__":  # main program
    to_wish()
    while True:

        query = takecommand()

        if "open Notepad" in query:
            speak("opening Notepad")
            n_path = "C:\\Users\\Gaganjit\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\Accessories\\Notepad.exe"
            os.startfile(n_path)

        elif "hi" in query:
            speak("Hi Sir")

        elif "how are you" in query:
            speak("i am fine sir how are you")

        elif "I am also fine" in query:
            speak("It is good to listen that from you")

        elif "give compliment" in query:
            speak("what should i say, sir")
            query = takecommand()
            speak("hmmm....")
            speak("then, can i say that person is beautifull")
            query = takecommand()
            speak("ohk then, you are so beautifull person i have seen")
    
        elif "open Notepad" in query:
            speak("opening notepad")
            npath = "C://WINDOWS//system32//notepad.exe"
            os.startfile(npath)

        elif "play" in query:
            ytsong = query.replace("play", "")
            speak(f"playing {ytsong}")
            pywhatkit.playonyt(ytsong)

        elif "thanks" in query:
            speak("its' my pleasure sir")

        elif "open command prompt" in query:
            speak("opening command prompt")
            os.system("start cmd")

        elif "IP address" in query:
            speak("fetching our details")
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "Wikipedia" in query:
            speak("searching wikipedia....")
            result_wiki = wikipedia.summary(query,sentence=2)
            speak("according to wikipedia.... ")
            speak(result_wiki)

        elif "open YouTube" in query:
            speak("opening youtube")
            webbrowser.open('www.youtube.com')

        elif "open Google Chrome" in query:
            speak("opening Google Chrome")
            chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chrome_path)

        elif "take a screenshot" in query:
            speak("sir, please enter name for screenshot file")
            ss_name = input("enter name:")
            speak("hold the screen for few seconds sir, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{ss_name}.jpg")
            speak("i am done sir, the screenshot is saved in our main folder. Now i am ready for next command")

        elif "temperature" in query:
            temperature()   


        # elif "how much power we have" or "battery" in query:
        #     battery_percentage()

        # elif "where i am" or "where we are" in query:
        #     speak("wait sir let me check")
        #     try:
        #         ipadd = requests.get('https://api.ipify.org').text    
        #         url = 'https://get.geojs.io/vi/ip/geo/' + ipadd + 'json'
        #         geo_requests = requests.get(url)
        #         geo_data = geo_requests.json()
        #         city = geo_data['city']
        #         country = ge_data['country']
        #         speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
        #     except Exception as e :
        #         speak("sorry sir, there is some network disturbance i can't find our location")    


        elif "goodbye" in query:
            speak("thanks for using me sir, now i am going you can call me or can use me anytime")
            sys.exit()    
