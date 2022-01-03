from time import ctime
import time
import difflib


def closeenough(string, goalstring, percentage):
	return(difflib.SequenceMatcher(None, goalstring, string).ratio() >= percentage)





def response(data, Statement_num):

#------------ TEST LINES --------------------------------------------------------------------------------------------

	if closeenough("test test", data, .75):
		return "test test"
	
# #-------------- SWAGG -----------------------------------------------------------------------------------------------

	if ( difflib.SequenceMatcher(None, "look alive mel it's playtime", data).ratio() >= 0.65):
 		Statement_num = 7
 		return("Yessir. What're we doing today?")


	if ( difflib.SequenceMatcher(None, "mel hold this place down", data).ratio() >= 0.85):
 		return("Yessir. On standby")
		 

	if ( difflib.SequenceMatcher(None, "mel standby", data).ratio() >= 0.85):
 		return("Yessir. On standby")

 
# #-------- GOOD MORNING / EVENING ----------------------------------------------------------------------------------------


	if ( difflib.SequenceMatcher(None, "good morning mel", data).ratio() >= 0.75):
 		return("Good Morning Sir")

	if ( difflib.SequenceMatcher(None, "good evening mel", data).ratio() >= 0.75):
 		return("Good Evening Sir")

	if ( difflib.SequenceMatcher(None, "hello mel", data).ratio() >= 0.75):
 		return("Hello Sir")

	if ( difflib.SequenceMatcher(None, "hi mel", data).ratio() >= 0.75):
 		return("Hello Sir")


# #--------------- WORK TIMERS-----------------------------------------------------------------------------------------------

# 	if "mel let's do some work" in data:
# 		Statement_num = 10
# 		return("Sounds like a plan sir. Longterm or Shortterm sir?.")

# 	if "long-term" in data and Statement_num == 10:
# 		return("Yessir.")
# 		timer = threading.Timer(900, check_in_regaurding_work)                        				# as of 2/12/21
# 		timer.start()  # after 15 minutes, Mel will checkin to make sure you're still working   		# as of 2/12/21
# 		timer = threading.Timer(1800, check_in_regaurding_work)
# 		timer.start()  # after 30 minutes, Mel will checkin to make sure you're still working
# 		timer = threading.Timer(2700, check_in_regaurding_work)
# 		timer.start()  # after 45 minutes, Mel will checkin to make sure you're still working

# 	if "short-term" in data and Statement_num == 10:
# 		return("Yessir.")
# 		timer = threading.Timer(300, check_in_regaurding_work)                        				# as of 2/12/21
# 		timer.start()  # after 5 minutes, Mel will checkin to make sure you're still working   		# as of 2/12/21
# 		timer = threading.Timer(600, check_in_regaurding_work)
# 		timer.start()  # after 10 minutes, Mel will checkin to make sure you're still working
# 		timer = threading.Timer(900, check_in_regaurding_work)
# 		timer.start()  # after 15 minutes, Mel will checkin to make sure you're still working

# #------------------------ QUEUES/INTROS ------------------------------------------------------------------------------




# 	if "alright mel let's get to it" in data:
# 		return("Sounds like a plan sir. Can I help?")
# 		Statement_num = 8

# 	if "alright now let's get to it" in data:
# 		return("Sounds like a plan sir. Can I help?")
# 		Statement_num = 8

# 	if "mel let's get to it" in data:
# 		return("Sounds like a plan sir. Can I help?")
# 		Statement_num = 8

# 	if "now let's get to it" in data:
# 		return("Sounds like a plan sir. Can I help?")
# 		Statement_num = 8










	if closeenough("mel how are you today", data, .75):
		Statement_num = 5
		return "Always well sir. And you?"

	if closeenough("mel you up", data, .75):
		return "Yessir. I'm here."

	if (closeenough("mel are you with me", data, .7) or closeenough("mel can you hear me", data, .7)):
		return "Yessir. I'm with you"

	if closeenough("mel you got me", data, .7):
		return "Yessir. I'm with you"

	if closeenough("give him the rundown", data, .75):
		return "Yessir. I'm Mel, assistant to Pat Flanigan. pleasure to meet you."

	if closeenough("mel what can you do", data, .75):
		return "For now I can talk and play some tunes, but I'm on my way up"


# # #------------- QUESTIONS ---------------------------------------------------------------------------------------------

	if closeenough("mel what time is it", data, .75):
		return(ctime())

	if closeenough("what is your name", data, .7):
		return("my name is Meliora, you can call me Mel")

# # #---------------- REAL SHIT -------------------------------------------------------------------------------------------

# 	if "mel why do I do what I do" in data:
# 		return("Well sir. Primarily your nation. Your family aswell.")

# # #------------ INSULTS --------------------------------------------------------------------------------------------------

# 	if "mel suck my dick" in data or "suck my dick" in data:
# 		return("Fuck you, suck your own dick")

# 	if "mel f*** you" in data:
# 		return("Fuck off asshole, I've got shit to do")

# 	if "f*** you Mel" in data:
# 		return("Fuck off asshole, I've got shit to do... Do you think I'm some sort of a fucking joke")
# 		Statement_num = 6

# # #------------- CONTINUATIONS ------------------------------------------------------------------------------------


# 	if "yes" in data and Statement_num == 6:
# 		return("Alright. You're a clown. Fuck you")
# 	if "no" in data and Statement_num == 6:
# 		return("Good.")

# 	if ("well" in data or "good" in data or "well thank you" in data or "good thank you" in data) and Statement_num == 5:
# 		return("good to hear sir.")

# 	if "oh not much just getting some stuff done" in data and Statement_num == 7:
# 		return("Sounds good sir. I'll be here if you need me")

# 	if "not much just some work" in data and Statement_num == 7:
# 		return("Sounds good sir. I'll be here if you need me")

# 	if "just some work today" in data and Statement_num == 7:
# 		return("Sounds good sir. I'll be here if you need me")

# 	if "yes" in data and Statement_num == 8:
# 		return("Just let me know how I can help")

# 	if "no" in data and Statement_num == 8:
# 		return("Alright. I'll be here if you need me.")

# 	if "thank you" in data and Statement_num == 9:
# 		return("always")

	else:
		return("nothing to see here")











## Check this out sometime...

#    if "where is" in data:
#        data = data.split(" ")
#        location = data[2]
#        speak("Hold on Frank, I will show you where " + location + " is.")
#        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


