#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

# Current Max Statement Num ==

import os
import sys
import speech_recognition as sr
import asyncio
import threading	
import vocabulary
from time import ctime
import time
import os
from gtts import gTTS


#--------------------- Global Variables --------------------------------
Statement_num = 0
Miss_num = 0
count = 0
#-----------------------------------------------------------------------

def speak(audioString):
	print(audioString)
	tts = gTTS(text=audioString, lang='en')
	tts.save("response_to_speech.mp3")
	os.system("mpg321 response_to_speech.mp3")

def check_in_regaurding_work():
	speak("Just checking in sir, are you still working?")

def recordAudio():
	#--------------------- Global Variables ----------------------------------
	global Miss_num
	global Statement_num
	global count

	#----------------- These lines in testing as of 2/28/2021 ---------------------
	config: {			
		speechContexts: [{
			phrases: ["Mel"],
			boost: 50
		}]
	}
   
	r = sr.Recognizer()
	with sr.Microphone() as source:

     	#r.adjust_for_ambient_noise(source)                            # this is a new test line as of 1/29/2021
		print("\n---------------------------------")
		print("Say something!")
		print("Statement Number : " ,Statement_num)
		print("Miss Number : ", Miss_num) 
		print("Total Count : ", count)

	#audio = r.listen(source, phrase_time_limit = 5)   // uncomment this to record audio 12/7/21


    # Speech recognition using Google Speech Recognition -------------------
	data = ""
	count += 1
	try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		
		#data = r.recognize_google(audio)                                     ## Uncomment this to record audio 12/7/21
		data = input("input statement \n")
        #print(data)
    
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		if Miss_num > 1:
			Miss_num = 0
			Statement_num = 0
		else:
			Miss_num += 1
    
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

	return data


#------------------ PROGRAM RUNS HERE -----------------------------------------------------------------------

# initialization
time.sleep(2)


#speak("Hi Sir. What can I do for you today?")							  # This line for speech
print("Hello Sir. System Initialized. \nWhat can I do for you today?")    # This line for text

while 1:
	data = recordAudio()
	response = vocabulary.response(data, Statement_num)
	 
	print("Mel's Response :: ")
	#speak(response) 										# This line for speech
	print(response)											# This line for text
	