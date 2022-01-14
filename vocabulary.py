import datetime
from itertools import permutations as perm
from time import ctime
import time
import difflib
import random
import speechvault
import a_few_functions


# -----------------------------------------------------------------------------------------------------------------------------------
global expecting_response
expecting_response = False


intent = ""
introduction = False
question = False


# ------------------------------------------------------------------------------------------------------------------------------------
# This returns True or False depending if a word is close enough to another word
def closeenough(goalstring, string, percentage):
    perms = list(perm(string.split()))
    for p in perms:
        if (difflib.SequenceMatcher(None, goalstring, ' '.join(p)).ratio() >= percentage):
            return True
    # return (difflib.SequenceMatcher(None, goalstring, string).ratio() >= percentage)


# This ONLY returns True (no false) if a word is close enough to a list of words, this depends on closeenough
def closeenoughinlist(listofgoalstrings, string, percentage):
    for word in listofgoalstrings:
        if (closeenough(word, string, .75)):
            return True


def endofconvo():
    global expecting_response
    expecting_response = False


def expectingresponse():
    global expecting_response
    expecting_response = True


def response(data):

    # -------------- GENERAL CONVERSATION STARTERS ---------------------------------------------------------------------------------------------
    CALL_listofintroductions = [
        "hello mel", "hi mel", "good day mel", "mel you up",  "mel you got me",
        "yo whats up mel", "hey mel", "whats up mel", "yo mel", "hello again mel"
    ]
    RESPONSE_listofintroductions = [
        "Hello Sir.", "How are you today. Boss", "Welcome back Sir", "Welcome back.  Boss",
        "How are you today. Sir", "Good to see you again. Boss. How are you?", "Sir. How's the Day?"
    ]
    CALL_listofmelintroduceyourself = [
        "mel introduce yourself", "mel give him the rundown", "mel give her the rundown", "introduce yourself mel", "mel say hi", "say hi mel"
    ]

    if closeenoughinlist(CALL_listofintroductions, data, .75):
        response = random.choice(RESPONSE_listofintroductions)
        if (response == "How are you today. Boss"
            or response == "How are you today. Sir"
            or response == "Good to see you again. Boss. How are you?"
                or response == "Sir. How's the Day?"):
            expectingresponse()
        return response

    if closeenoughinlist(CALL_listofmelintroduceyourself, data, .95):
        return "Yessir. I'm Mel, assistant to Pat Flanigan. pleasure to meet you."

    if closeenough("mel what can you do", data, .75):
        return "For now I can talk and play some tunes, but I'm on my way up"

    if closeenough("mel how are you today", data, 0.75):
        expectingresponse()
        return("Excellent Sir. And You?")
    if (closeenoughinlist(["good", "excellent", "well", "good thank you", "excellent thank you", "well thank you", "crushing"], data, .75) and expecting_response == True):
        endofconvo()
        return("Very Good to hear Sir.")
    if (closeenoughinlist(["bad", "terrible", "not so well", "quite poor mel", "not so good", "honestly bad", "down bad"], data, .75) and expecting_response == True):
        endofconvo()
        return("I'm sorry Sir, Perhaps some work will cheer you up?")


# ------------ TEST LINES --------------------------------------------------------------------------------------------------------------------

    if closeenough("test test", data, .75):
        return "test test"


# -------------- SWAGG ------------------------------------------------------------------------------------------------------------------------
    CALL_listofmelstandby = [
        "mel hold this place down", "mel standby"
    ]
    RESPONSE_listofmelstandby = [
        "Yessir. On standby", "Yessir. On Lock"
    ]

    if closeenoughinlist(CALL_listofmelstandby, data, .75):
        return random.choice(RESPONSE_listofmelstandby)


# --------- SOME IRONMAN QUOTES -----------------------------------------------------------------------------------------------------------------

    if closeenough("look alive mel it's playtime", data, 0.65):
        return("Yessir. Let's get this bread")

    if closeenough("mel what am i looking at", data, .75):  # From Ironman, you uncultured swine
        return "Not sure, I'm working on it."


# --------------- WORK TIMER----------------------------------------------------------------------------------------------------------------------

    if closeenough("mel let's do some work", data, .75):
        Statement_num = 10
        return("Sounds like a plan sir. Longterm or Shortterm sir?.")

    if (closeenough("long-term", data, .75) and Statement_num == 10):
        return("Yessir.")
        # as of 2/12/21
        timer = threading.Timer(900, check_in_regaurding_work)
        timer.start()  # after 15 minutes, Mel will checkin to make sure you're still working   		# as of 2/12/21
        timer = threading.Timer(1800, check_in_regaurding_work)
        timer.start()  # after 30 minutes, Mel will checkin to make sure you're still working
        timer = threading.Timer(2700, check_in_regaurding_work)
        timer.start()  # after 45 minutes, Mel will checkin to make sure you're still working

    if (closeenough("short-term", data, .75) and Statement_num == 10):
        return("Yessir.")
        # as of 2/12/21
        timer = threading.Timer(300, check_in_regaurding_work)
        timer.start()  # after 5 minutes, Mel will checkin to make sure you're still working   		# as of 2/12/21
        timer = threading.Timer(600, check_in_regaurding_work)
        timer.start()  # after 10 minutes, Mel will checkin to make sure you're still working
        timer = threading.Timer(900, check_in_regaurding_work)
        timer.start()  # after 15 minutes, Mel will checkin to make sure you're still working


# ------------------------ WAKE UP QUEUES --------------------------------------------------------------------------------------------------
    CALL_listofmel_areyouwithme = [
        "mel are you with me", "mel can you hear me", "mel you with me", "mel you up", "mel you working", "mel lets get to it", "alright mel lets get to it"
    ]
    RESPONSE_listofmel_areyouwithme = [
        "Yessir.. I'm with you.", "Of course Sir. How can I help", "Yessir. Let's get crushing", "Yessir. Lets get this fucking bread"
    ]

    if closeenoughinlist(CALL_listofmel_areyouwithme, data, .75):
        return random.choice(RESPONSE_listofmel_areyouwithme)


# # # #------------- QUESTIONS ------------------------------------------------------------------------------------------------------------------

    if closeenough("mel what is the date", data, .8):
        return(a_few_functions.returndate())

    if closeenough("mel what is the time", data, 0.8):
        return(a_few_functions.returntime())

    if closeenough("mel play some music", data, .8):
        return(a_few_functions.playmusic())


# Look into this shit.. interesting to get mel to return the full month, day, etc.
# now = datetime.datetime.now()
# print(now.year, now.month, now.day, now.hour, now.minute, now.second)
# # 2015 5 6 8 53 40

# 	if closeenough("what is your name", data, .7):
# 		return("my name is Meliora, you can call me Mel")

# # # #---------------- REAL SHIT -------------------------------------------------------------------------------------------------------------

# # 	if "mel why do I do what I do" in data:
# # 		return("Well sir. Primarily your nation. Your family aswell.")

# # # #------------ INSULTS --------------------------------------------------------------------------------------------------------------------

# # 	if "mel suck my dick" in data or "suck my dick" in data:
# # 		return("Fuck you, suck your own dick")

# # 	if "mel f*** you" in data:
# # 		return("Fuck off asshole, I've got shit to do")

# # 	if "f*** you Mel" in data:
# # 		return("Fuck off asshole, I've got shit to do... Do you think I'm some sort of a fucking joke")
# # 		Statement_num = 6

# # # #------------- CONTINUATIONS --------------------------------------------------------------------------------------------------------------------


# # 	if "yes" in data and Statement_num == 6:
# # 		return("Alright. You're a clown. Fuck you")
# # 	if "no" in data and Statement_num == 6:
# # 		return("Good.")

# # 	if ("well" in data or "good" in data or "well thank you" in data or "good thank you" in data) and Statement_num == 5:
# # 		return("good to hear sir.")

# # 	if "oh not much just getting some stuff done" in data and Statement_num == 7:
# # 		return("Sounds good sir. I'll be here if you need me")

# # 	if "not much just some work" in data and Statement_num == 7:
# # 		return("Sounds good sir. I'll be here if you need me")

# # 	if "just some work today" in data and Statement_num == 7:
# # 		return("Sounds good sir. I'll be here if you need me")

# # 	if "yes" in data and Statement_num == 8:
# # 		return("Just let me know how I can help")

# # 	if "no" in data and Statement_num == 8:
# # 		return("Alright. I'll be here if you need me.")

# # 	if "thank you" in data and Statement_num == 9:
# # 		return("always")

    if closeenough("mel give me a speech", data, .75):
        return random.choice(speechvault.RESPONSE_listofbeautifulspeeches)

    else:
        return("nothing to see here")


# ## Check this out sometime...

# #    if "where is" in data:
# #        data = data.split(" ")
# #        location = data[2]
# #        speak("Hold on Frank, I will show you where " + location + " is.")
# #        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
