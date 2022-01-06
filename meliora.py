



	# "Good morning. It's 7 A.M. The weather in Malibu is 72 degrees with scattered clouds." 
	# "The surf conditions are fair with waist to shoulder highlines, high tide will be at 10:52 a.m."
		
		# ―J.A.R.V.I.S.


	# "Say, J.A.R.V.I.S., is it that time?"
	# "The House Party Protocol, sir?"
	# "Correct."
		
		# ―Tony Stark and J.A.R.V.I.S.


	# "All wrapped up here, sir. Will there be anything else?"
	# "You know what to do."
	# "The Clean Slate Protocol, sir?"
	# "Screw it, it's Christmas. Yes, yes."
		
		# ―J.A.R.V.I.S. and Tony Stark







#---------------------------------------------------------------------
#		Import statements

import asyncio
import os
import sys
import threading
import time
import difflib
from time import ctime
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import vocabulary


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
			phrases: ["mel"],
			boost: 50
		}]
	}
   
	r = sr.Recognizer()
	with sr.Microphone() as source:

     	#r.adjust_for_ambient_noise(source)                            # this is a new test line as of 1/29/2021
		print("\n---------------------------------")
		print("Say something!")
		#print("Statement Number : " ,Statement_num)
		#print("Miss Number : ", Miss_num) 
		#print("Total Count : ", count)

		#audio = r.listen(source, phrase_time_limit = 5)   # uncomment this to record audio 12/7/21 
														  # DO NOT UNINDENT THE ABOVE LINE, INDENTATION IS MAD IMPORTANT


    # Speech recognition using Google Speech Recognition -------------------
	data = ""
	count += 1
	try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		
		#rawresponse = r.recognize_google(audio)                                     ## Uncomment this to record audio 12/7/21
		rawresponse = input("input statement \n")							  ## Uncomment this to input text 12/24/21
		data = rawresponse.lower()
    
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


speak("System Initialized. \nHello Sir. What can I do for you today?")							  # This line for speech
print("System Initialized. \nHello Sir. What can I do for you today?")    # This line for text

while 1:
	data = recordAudio()
	response = vocabulary.response(data)

	print("Mel heard :: ")
	print(data)	
	print("\n")

	print("Mel's Response :: ")
	if (response != "nothing to see here"):
		speak(response) 										# This line for speech
		print(response)											# This line for text

										
	


	
