import pyttsx3
import platform
from platform import sys
import speech_recognition as sr
import datetime
import time
import os
import pywhatkit
from requests import get
import wikipedia
import webbrowser
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import pyautogui
from jarvisUI import Ui_MainWindow

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
    if hour>=0 and hour<=12:
        speak(f"Good Morning sir")
    elif hour>=12 and hour<=18:
        speak(f"Good Afternoon sir")
    else:
        speak(f"Good Evening sir")
    speak("i am jarvis sir, Please tell me how may i help you!!!")

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.....")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=2, phrase_time_limit=5)
        try:
            print("Recognising.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said:{query}")
        except Exception as e:
            speak("say that again please")
            return "none"
        return query

    def TaskExecution(self):
        to_wish()
        while True:
            self.query = self.takecommand()

            if "hi" in self.query:
                speak("hi sir")

            elif "how are you" in self.query:
                speak("i am fine sir , what about you?")

            elif "i am also fine" in self.query:
                speak("it's good to listen that from you")

            elif "give complement" in self.query:
                speak("what should i say, sir")
                self.query = self.takecommand()
                speak("hmmm....")
                speak("then, can i say that she is beautifull")
                self.query = self.takecommand()
                speak("ohk then, you are so beautifull girl i have seen")
    
            elif "open Notepad" in self.query:
                speak("opening notepad")
                npath = "C://WINDOWS//system32//notepad.exe"
                os.startfile(npath)

            elif "play" in self.query:
                ytsong = self.query.replace("play", "")
                speak(f"playing {ytsong}")
                pywhatkit.playonyt(ytsong)

            elif "thanks" in self.query:
                speak("its' my pleasure sir")

            elif "open command prompt" in self.query:
                speak("opening command prompt")
                os.system("start cmd")

            elif "IP address" in self.query:
                speak("fetching our details")
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")

            elif "Wikipedia" in self.query:
                speak("searching wikipedia....")
                result_wiki = wikipedia.summary(self.query,sentence=2)
                speak("according to wikipedia.... ")
                speak(result_wiki)

            elif "open YouTube" in self.query:
                speak("opening youtube")
                webbrowser.open('www.youtube.com')

            elif "open Google Chrome" in self.query:
                speak("opening Google Chrome")
                chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                os.startfile(chrome_path)

            elif "take a screenshot" in self.query:
                speak("sir, please enter name for screenshot file")
                ss_name = input("enter name:")
                speak("hold the screen for few seconds sir, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{ss_name}.jpg")
                speak("i am done sir, the screenshot is saved in our main folder. Now i am ready for next command")

            elif "Goodbye" in self.query:
                speak("thanks for using me sir, now i am going you can call me or can use me anytime")
                sys.exit()    

startExecution = MainThread()   

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("jarvis.gif")    
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())