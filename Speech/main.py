from __future__ import print_function

import datetime
import os
import os.path
import pickle
import subprocess
import sys
import time
from urllib.request import DataHandler

import pyttsx3
import pytz
import speech_recognition as sr
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

MONTHS = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

r = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio, language="de-DE")
        except sr.UnknownValueError():
            print("Sorry, I could not understand that")
        except sr.RequestError():
            print("Sorry, my speech service is down")
        return voice_data.lower()


def authenticate_calendar():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service


def get_events(day, service):
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(), singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        speak('No upcoming events found.')
    else:
        speak(f"You have {len(events)} events on this day.")
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            start_time = str(start.split(
                "T")[1].split("+")[0])

            print(event["summary"] + " at " + str(start_time)[0:5])
            speak(event["summary"] + " at " + str(start_time)[0:5] + "o'clock")


def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count(str(today)) > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < today.month and month != -1:
        year = year + 1

    if day < today.day and month == -1 and day != -1:
        month = month + 1

    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if month == -1 or day == -1:
        return None

    return datetime.date(month=month, day=day, year=year)


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(f"./Notes/{file_name}", "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", f"./Notes/{file_name}"])


def respond(text):
    CALENDAR_STRS = ["what do i have", "what is on",
                     "what are my plans", "do i have plans", "am i busy"]
    for phrase in CALENDAR_STRS:
        if phrase in text:
            date = get_date(text)
            if date:
                get_events(date, SERVICE)
            else:
                speak("Sorry, I didn't get that.")

    NOTE_STRS = ["note", "write this down", "note this", "remember this"]
    for phrase in NOTE_STRS:
        if phrase in text:
            speak("What do you want to write down?")
            note_text = get_audio()
            note(note_text)
            speak("Noted that.")

    EXIT_STRS = ["exit", "stop", "close"]
    for phrase in EXIT_STRS:
        if phrase in text:
            speak("Exiting now.")
            time.sleep(1)
            sys.exit(1)

    CHROME_STRS = ["chrome", "open chrome", "webbrowser"]
    for phrase in CHROME_STRS:
        if phrase in text:
            speak("Opening Chrome.")
            subprocess.Popen(
                "C:\Program Files\Google\Chrome\Application\chrome.exe")


SERVICE = authenticate_calendar()
print("Start")

while True:
    print("Listening")
    try:
        text = get_audio()
        if text.count("robot") > 0:
            try:
                speak("What do you want me to do?")
                text = get_audio()
                respond(text)
            except sr.UnknownValueError:
                pass
        else:
            pass
    except sr.UnknownValueError:
        pass
