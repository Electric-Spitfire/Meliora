from time import ctime
import time




def response(data, Statement_num):

#------------ TEST LINES --------------------------------------------------------------------------------------------

	if "test test" in data:
		return("test test")

#-------------- SWAGG -----------------------------------------------------------------------------------------------

	if "look alive mail it's playtime" in data or "look alive Mel it's playtime" in data:
		Statement_num = 7
		return("Yessir. What're we doing today?")

	if "all right Mel look alive it's playtime" in data:
		Statement_num = 7
		return("Yessir. What're we doing today?")

	if "Mel hold this place down" in data or "Mel standby" in data:
		Statement_num = 9
		return("Yessir. On standby")

#-------- GOOD MORNING / EVENING ----------------------------------------------------------------------------------------

	if "Good evening Mel" in data or "Mel good Evening" in data:
		return("Good Evening Sir")

	if "Hello Mel" in data or "Hi Mel" in data:
		return("Hello Sir")

	if "Good morning Mel" in data or "Mel good morning" in data:
		return("Good Morning Sir")

#--------------- WORK TIMERS-----------------------------------------------------------------------------------------------

	if "Mel let's do some work" in data:
		Statement_num = 10
		return("Sounds like a plan sir. Longterm or Shortterm sir?.")

	if "long-term" in data and Statement_num == 10:
		return("Yessir.")
		timer = threading.Timer(900, check_in_regaurding_work)                        				# as of 2/12/21
		timer.start()  # after 15 minutes, Mel will checkin to make sure you're still working   		# as of 2/12/21
		timer = threading.Timer(1800, check_in_regaurding_work)
		timer.start()  # after 30 minutes, Mel will checkin to make sure you're still working
		timer = threading.Timer(2700, check_in_regaurding_work)
		timer.start()  # after 45 minutes, Mel will checkin to make sure you're still working

	if "short-term" in data and Statement_num == 10:
		return("Yessir.")
		timer = threading.Timer(300, check_in_regaurding_work)                        				# as of 2/12/21
		timer.start()  # after 5 minutes, Mel will checkin to make sure you're still working   		# as of 2/12/21
		timer = threading.Timer(600, check_in_regaurding_work)
		timer.start()  # after 10 minutes, Mel will checkin to make sure you're still working
		timer = threading.Timer(900, check_in_regaurding_work)
		timer.start()  # after 15 minutes, Mel will checkin to make sure you're still working

#------------------------ QUEUES/INTROS ------------------------------------------------------------------------------

	if "Mel how you doing" in data:
		return("Doing well sir. And you?")
		Statement_num = 5

	if "alright Mel let's get to it" in data:
		return("Sounds like a plan sir. Can I help?")
		Statement_num = 8

	if "alright now let's get to it" in data:
		return("Sounds like a plan sir. Can I help?")
		Statement_num = 8

	if "Mel let's get to it" in data:
		return("Sounds like a plan sir. Can I help?")
		Statement_num = 8

	if "now let's get to it" in data:
		return("Sounds like a plan sir. Can I help?")
		Statement_num = 8



	if "Mel how are you today" in data or "how are you today Mel" in data:
		return("Always well sir. And you?")
		Statement_num = 5

	if "Mel you up" in data or "Mel are you up" in data or "Mel Europe" in data:
		return("Yessir. I'm here.")

	if "Mel are you with me" in data or "Mel can you hear me" in data or "Mel you with me" in data:
		return("Yessir. I'm with you")

	if "you with me Mel" in data or "you got me Mel" in data or "Mel you got me" in data:
		return("Yessir")

	if "give him the rundown" in data:
		return("Yessir. I'm Mel, assistant to Pat Flanigan. pleasure to meet you.")

	if "Mel what can you do" in data or "what can you do" in data:
		return("For now I can talk and play some tunes")

# #------------- QUESTIONS ---------------------------------------------------------------------------------------------


	if "Mel what time is it" in data:
		return(ctime())

	if "Mel how are you" in data:
		return("Always well sir")

	if "what is your name" in data or "what's your name" in data:
		return("my name is Meliora, you can call me Mel")

# #---------------- REAL SHIT -------------------------------------------------------------------------------------------

	if "Mel why do I do what I do" in data:
		return("Well sir. Primarily your nation. Your family aswell.")

# #------------ INSULTS --------------------------------------------------------------------------------------------------

	if "Mel suck my dick" in data or "suck my dick" in data:
		return("Fuck you, suck your own dick")

	if "Mel f*** you" in data:
		return("Fuck off asshole, I've got shit to do")

	if "f*** you Mel" in data:
		return("Fuck off asshole, I've got shit to do... Do you think I'm some sort of a fucking joke")
		Statement_num = 6

# #------------- CONTINUATIONS ------------------------------------------------------------------------------------


	if "yes" in data and Statement_num == 6:
		return("Alright. You're a clown. Fuck you")
	if "no" in data and Statement_num == 6:
		return("Good.")

	if ("well" in data or "good" in data or "well thank you" in data or "good thank you" in data) and Statement_num == 5:
		return("good to hear sir.")

	if "oh not much just getting some stuff done" in data and Statement_num == 7:
		return("Sounds good sir. I'll be here if you need me")

	if "not much just some work" in data and Statement_num == 7:
		return("Sounds good sir. I'll be here if you need me")

	if "just some work today" in data and Statement_num == 7:
		return("Sounds good sir. I'll be here if you need me")

	if "yes" in data and Statement_num == 8:
		return("Just let me know how I can help")

	if "no" in data and Statement_num == 8:
		return("Alright. I'll be here if you need me.")

	if "thank you" in data and Statement_num == 9:
		return("always")













## Check this out sometime...

#    if "where is" in data:
#        data = data.split(" ")
#        location = data[2]
#        speak("Hold on Frank, I will show you where " + location + " is.")
#        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


