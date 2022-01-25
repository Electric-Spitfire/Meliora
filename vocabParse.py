import re
import spotify_access
import a_few_functions
import printColor
import json
from json.decoder import JSONDecodeError
import random
import wikipedia


class parser:
    def __init__(self) -> None:
        f = open('speeches.json')
        self.speeches = json.load(f)
        f.close()
        pass

    def parseSpotifyPlay(self, request):
        spotify_access.setupDevice()
        ''' reads input from user and uses spotify_access to play song
        "(play)(.*)((by)(.*))?"
        accepts a string of the form "play song by artist"
        accepts a string of the form "play song"
        returns a string of the form "song by artist" as found by spotipy
        '''
        regex = r"(play)(.*)((by)(.*))?"
        match = re.search(regex, request)
        if match:
            song = match.group(2).strip()
            artist = match.group(4)
            return spotify_access.play(song, artist)
        else:
            return None

    def parseSpotifyQueue(self, request):
        spotify_access.setupDevice()
        ''' reads input from user and uses spotify_access to play song
        "(queue)(.*)((by)(.*))?"
        accepts a string of the form "play song by artist"
        accepts a string of the form "play song"
        returns a string of the form "song by artist" as found by spotipy
        '''
        regex = r"(queue)(.*)((by)(.*))?"
        match = re.search(regex, request)
        if match:
            song = match.group(2).strip()
            artist = match.group(4)
            return spotify_access.queue(song, artist)
        else:
            return None

    def parseTime(self, request):
        '''
        accepts a string of the form "what time is it"
        accepts a string of the form "what's the time"
        accepts a string of the form "what is the time"
        :return: the current time in 12-hour format
        '''
        regex = r"(what)((')?s)?( )?((is )?the time|time is it)(.*)"
        match = re.search(regex, request)
        if match:
            return a_few_functions.returntime()
        else:
            return None

    def parseDate(self, request):
        '''
        accepts a string of the form "what day is it"
        accepts a string of the form "what's the date"
        accepts a string of the form "what is the date"
        :return: the current date in the format Day of the Week, Month Day, Year
                                                        Friday, January 21, 2022
        '''
        regex = r"(what)((')?s)?( )?((is )?the date|date is it|('s|is)? todays date| day is it)(.*)"
        match = re.search(regex, request)
        if match:
            return a_few_functions.returndate()
        else:
            return None

    def parseInspire(self, request):
        '''
        accepts a string of the form "inspire me"
        :return: a random quote from the speeches.json file
        '''
        regex = r"(inspire me)(.*)"
        match = re.search(regex, request)
        if match:
            speech_number = random.randint(0, len(self.speeches))
            return self.speeches[str(speech_number)]
        else:
            return None

    def parseTODOAdd(self, request):
        '''
        accepts a string of the form "add task to todo"
        :return: the task added to todo.json
        '''
        regex = r"(add)(.*)(to TODO)(.*)"
        match = re.search(regex, request)
        if match:
            todo = match.group(2).strip()
            with open('todo.json', 'r') as outfile:
                list = json.load(outfile)
                count = len(list)
                list[str(count)] = todo
                outfile.close()
            with open('todo.json', 'w') as outfile:
                json.dump(list, outfile)
                outfile.close()
            return todo
        else:
            return None

    def parseTODOREAD(self, request):
        '''
        accepts a string of the form "read todo"
        :return: the todo list from todo.json
        :param request:
        :return:
        '''
        regex = r"(read)(.*)(TODO)"
        match = re.search(regex, request)
        if match:
            with open('todo.json', 'r') as outfile:
                list = json.load(outfile)
                list.pop("TODO")
                outfile.close()
            return list or "TODO list is empty"

    def parseTODODEL(self, request):
        '''
        accepts a string of the form "delete task from todo"
        accepts a string of the form "remove task from todo"
        :return: the full list of todo items from todo.json with the task removed
        '''
        regex = r"(delete|remove)(.*)(from TODO)"
        match = re.search(regex, request)
        if match:
            todo = match.group(2).strip()
            with open('todo.json', 'r') as outfile:
                list = json.load(outfile)
                try:
                    printColor.red(f"deleted {list.pop(todo)}")
                    a_few_functions.speak(f"deleted {list.pop(todo)}", False)
                    outfile.close()
                except KeyError:
                    a_few_functions.speak("TODO item not found")
            with open('todo.json', 'w') as outfile:
                json.dump(list, outfile)
                outfile.close()
            return self.parseTODOREAD("read TODO")

    def parseWIKI(self, request):
        """
        accepts a string in the form "learn about {search term}"
        :param request:
        :return: top result
        """
        regex = r"(learn about)(.*)"
        match = re.search(regex, request)
        if match:
            search_term = match.group(2).strip()
            # print(search_term)
            a_few_functions.speak(f"Searching for {search_term}", False)
            results = wikipedia.search(search_term)
            if results:
                full_summary =  wikipedia.summary(results[0], sentences=4, auto_suggest=False)
                remove_parenthesis = re.sub(r'\([^()]*\)', '', full_summary).split('.')
                new_summary = remove_parenthesis[0] + '. ' + remove_parenthesis[1] + '. ' + remove_parenthesis[2] + '. '
                return new_summary
        return None

    def parseShutDown(self, request):
        """
        accepts a string in the form "shut down"
        :param request:
        :return: None; quits the program
        """
        regex = r"(shut down)"
        match = re.search(regex, request)
        if match:
            a_few_functions.speak("Shutting down", False)
            exit()


def main(command=None):
    p = parser()  # instantiate the parser
    '''
    if command is None then the file is being run directly
    otherwise the file is being imported by run_meliora.py and the command is passed in
    '''

    if not command:
        command = input("Enter command:\n ")
    attrs = (getattr(p, name) for name in dir(p) if
             not name.startswith('_'))  # get all the functions in the parser class
    methods = filter(callable, attrs)  # filter out the non-callable functions
    '''
    the following loop iterates through the functions in the parser class and runs them returning any non-None values
    '''
    for method in methods:
        result = method(command)
        if result:
            return result

    return "I'm sorry, I don't know how to do that."  # if no function returns a value then return this


if __name__ == '__main__':
    print(main())
