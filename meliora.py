#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

# Current Max Statement Num ==

import os
import sys

import speech_recognition as sr
import asyncio
import threading	# as of 2/12/21 import mel_responses
import vocabulary
from time import ctime
import time
import os
from gtts import gTTS



Statement_num = 0
Miss_num = 0
count = 0




def speak(audioString):
	print(audioString)
	tts = gTTS(text=audioString, lang='en')
	tts.save("response_to_speech.mp3")
	os.system("mpg321 response_to_speech.mp3")

def check_in_regaurding_work():
	speak("Just checking in sir, are you still working?")


def recordAudio():
	global Miss_num
	global Statement_num
	global count


#----------------- This is in testing as of 2/28/2021 ---------------------
	config: {			
		speechContexts: [{
			phrases: ["Mel"],
			boost: 50
		}]
	}

#--------------------- RECORD AUDIO ---------------------------------------
   
	r = sr.Recognizer()
	with sr.Microphone() as source:

#    	r.adjust_for_ambient_noise(source)                            # this is a new test line as of 1/29/2021
		print("\n---------------------------------")
		print("Say something!")
		print("Statement Number : " ,Statement_num)
		print("Miss Number : ", Miss_num) 
		print("Total Count : ", count)

#	audio = r.listen(source, phrase_time_limit = 5)   // uncomment this to record audio 12/7/21


    # Speech recognition using Google Speech Recognition
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




#async def checkup(what,delay):
#	await asyncio.sleep(delay)
#	speak("what")







# def jarvis(data):
# 	global Statement_num


# #------------ TEST LINES --------------------------------------------------------------------------------------------

# 	if "test test" in data:
# 		speak("test test")


# #-------------- SWAGG -----------------------------------------------------------------------------------------------

# 	if "look alive mail it's playtime" in data or "look alive Mel it's playtime" in data:
# 		Statement_num = 7
# 		speak("Yessir. What're we doing today?")

# 	if "all right Mel look alive it's playtime" in data:
# 		Statement_num = 7
# 		speak("Yessir. What're we doing today?")

# 	if "Mel hold this place down" in data or "Mel standby" in data:
# 		Statement_num = 9
# 		speak("Yessir. On standby")



# #--------------- WORK -----------------------------------------------------------------------------------------------

# 	if "Mel let's do some work" in data:
# 		Statement_num = 10
# 		speak("Sounds like a plan sir. Longterm or Shortterm sir?.")

# 	if "long-term" in data and Statement_num == 10:
# 		speak("Yessir.")
# 		timer = threading.Timer(900, check_in_regaurding_work)                        				# as of 2/12/21
# 		timer.start()  # after 15 minutes, Mel will checkin to make sure you're still working   		# as of 2/12/21
# 		timer = threading.Timer(1800, check_in_regaurding_work)
# 		timer.start()  # after 30 minutes, Mel will checkin to make sure you're still working
# 		timer = threading.Timer(2700, check_in_regaurding_work)
# 		timer.start()  # after 45 minutes, Mel will checkin to make sure you're still working

# 	if "short-term" in data and Statement_num == 10:
# 		speak("Yessir.")
# 		timer = threading.Timer(300, check_in_regaurding_work)                        				# as of 2/12/21
# 		timer.start()  # after 5 minutes, Mel will checkin to make sure you're still working   		# as of 2/12/21
# 		timer = threading.Timer(600, check_in_regaurding_work)
# 		timer.start()  # after 10 minutes, Mel will checkin to make sure you're still working
# 		timer = threading.Timer(900, check_in_regaurding_work)
# 		timer.start()  # after 15 minutes, Mel will checkin to make sure you're still working






# #------------------------ QUEUES/INTROS ------------------------------------------------------------------------------

# 	if "Mel how you doing" in data:
# 		speak("Doing well sir. And you?")
# 		Statement_num = 5

# 	if "alright Mel let's get to it" in data:
# 		speak("Sounds like a plan sir. Can I help?")
# 		Statement_num = 8

# 	if "alright now let's get to it" in data:
# 		speak("Sounds like a plan sir. Can I help?")
# 		Statement_num = 8

# 	if "Mel let's get to it" in data:
# 		speak("Sounds like a plan sir. Can I help?")
# 		Statement_num = 8

# 	if "now let's get to it" in data:
# 		speak("Sounds like a plan sir. Can I help?")
# 		Statement_num = 8



# 	if "Mel how are you today" in data or "how are you today Mel" in data:
# 		speak("Always well sir. And you?")
# 		Statement_num = 5

# 	if "Mel you up" in data or "Mel are you up" in data or "Mel Europe" in data:
# 		speak("Yessir. I'm here.")

# 	if "Mel are you with me" in data or "Mel can you hear me" in data or "Mel you with me" in data:
# 		speak("Yessir. I'm with you")

# 	if "you with me Mel" in data or "you got me Mel" in data or "Mel you got me" in data:
# 		speak("Yessir")

# 	if "give him the rundown" in data:
# 		speak("Yessir. I'm Mel, assistant to Pat Flanigan. pleasure to meet you.")

# 	if "Mel what can you do" in data or "what can you do" in data:
# 		speak("For now I can talk and play some tunes")



# #------------- QUESTIONS ---------------------------------------------------------------------------------------------


# 	if "Mel what time is it" in data:
# 		speak(ctime())

# 	if "Mel how are you" in data:
# 		speak("Always well sir")

# 	if "what is your name" in data or "what's your name" in data:
# 		speak("my name is Meliora, you can call me Mel")



# #---------------- REAL SHIT -------------------------------------------------------------------------------------------

# 	if "Mel why do I do what I do" in data:
# 		speak("Well sir. Primarily your nation. Your family aswell.")


# #------------ INSULTS --------------------------------------------------------------------------------------------------

# 	if "Mel suck my dick" in data or "suck my dick" in data:
# 		speak("Fuck you, suck your own dick")

# 	if "Mel f*** you" in data:
# 		speak("Fuck off asshole, I've got shit to do")

# 	if "f*** you Mel" in data:
# 		speak("Fuck off asshole, I've got shit to do... Do you think I'm some sort of a fucking joke")
# 		Statement_num = 6









# #------------- CONTINUATIONS ------------------------------------------------------------------------------------


# 	if "yes" in data and Statement_num == 6:
# 		speak("Alright. You're a clown. Fuck you")
# 	if "no" in data and Statement_num == 6:
# 		speak("Good.")

# 	if ("well" in data or "good" in data or "well thank you" in data or "good thank you" in data) and Statement_num == 5:
# 		speak("good to hear sir.")



# 	if "oh not much just getting some stuff done" in data and Statement_num == 7:
# 		speak("Sounds good sir. I'll be here if you need me")

# 	if "not much just some work" in data and Statement_num == 7:
# 		speak("Sounds good sir. I'll be here if you need me")

# 	if "just some work today" in data and Statement_num == 7:
# 		speak("Sounds good sir. I'll be here if you need me")




# 	if "yes" in data and Statement_num == 8:
# 		speak("Just let me know how I can help")
# 	if "no" in data and Statement_num == 8:
# 		speak("Alright. I'll be here if you need me.")


# 	if "thank you" in data and Statement_num == 9:
# 		speak("always")















#    if "where is" in data:
#        data = data.split(" ")
#        location = data[2]
#        speak("Hold on Frank, I will show you where " + location + " is.")
#        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

# initialization
time.sleep(2)
#speak("Hi Sir. What can I do for you today?")
print("Hello Sir. System Initialized. \nWhat can I do for you today?")

while 1:
	data = recordAudio()
	response = vocabulary.response(data, Statement_num)
	#speak(response)
    
	print("Mel's Response :: ")
	print(response)