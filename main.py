import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour > 12 and hour <= 24:
        speak("Good evening!")
    speak("My name is Snappy, how may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 3500
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please... ")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            speak('Opening youtube...')
            url = 'youtube.com'
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
            webbrowser.get('chrome').open(url)
        elif 'open google' in query:
            speak('Opening google...')
            url = 'google.com'
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
            webbrowser.get('chrome').open(url)
        elif 'open discord' in query:
            speak('Opening discord...')
            url = 'https://discord.com/channels/781088174386184243/781088174386184247'
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
            webbrowser.get('chrome').open(url)
        elif 'open whatsapp' in query:
            speak('Opening whatsapp...')
            url = 'web.whatsapp.com'
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
            webbrowser.get('chrome').open(url)
        elif 'thank you' in query:
            speak("You're welcome")
            break
        elif 'play music' in query:
            music_dir= r"C:\Users\Umesh Kota\Music\Songs"
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))
        elif 'what is the time' in query:
            strTime =  datetime.datetime.now().strftime("%H:%M")
            speak(strTime)
        elif 'open spotify' in query:
            url = 'https://open.spotify.com/playlist/7yFQ0kZCnOhRjh60ErEBKN'
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
            webbrowser.get('chrome').open(url)
        elif 'open netflix' in query:
            url = 'https://www.netflix.com/browse'
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
            webbrowser.get('chrome').open(url)
        elif 'play jojo' in query:
            url = 'https://www.crunchyroll.com/jojos-bizarre-adventure'
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
            webbrowser.get('chrome').open(url)
