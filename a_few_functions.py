from datetime import datetime as dt
from datetime import date as dte
import spotify_access
from gtts import gTTS
import os
import playsound


def speak(audioString, printString=True):
    if printString:
        print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("response_to_speech.mp3")
    if os.name == 'nt':
        playsound.playsound('response_to_speech.mp3', True)
        os.remove('response_to_speech.mp3')
    else:
        os.system("mpg321 response_to_speech.mp3")


def returndate():
    today = dte.today()
    d2 = today.strftime("%A, %B %d, %Y")
    return d2


def returntime():
    now = dt.now()
    dt_string = now.strftime("%I:%M %p")
    return (dt_string)


def getsong():
    speak("What song would you like to play?")
    song = input()
    speak("Who is the artist?")
    artist = input()
    return (song, artist)


def playmusic():
    song = getsong()
    return (f"Playing {spotify_access.play(song[0], song[1])}")
