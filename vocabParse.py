import re
import spotify_access
import a_few_functions
import json
from json.decoder import JSONDecodeError
import random



class parser:
    def __init__(self) -> None:
        f = open('speeches.json')
        self.speeches = json.load(f)
        f.close()
        pass

    def parseSpotify(self,request):
        spotify_access.setupDevice()
        ''' reads input from user and uses spotify_access to play songp
        "(play)(.*)((by)(.*))?"
        accepts a string of the form "play song by artist"
        accepts a string of the form "play song"
        returns a string of the form "song by artist" as found by spotipy
        '''
        regex= r"(play)(.*)((by)(.*))?"
        match = re.search(regex,request)
        if match:
            song = match.group(2).strip()
            artist = match.group(4)
            return spotify_access.play(song,artist)
        else:
            return None

    def parseTime(self,request):
        regex= r"(what)((')?s)?( )?((is )?the time|time is it)(.*)"
        match = re.search(regex,request)
        if match:
            return a_few_functions.returntime()
        else:
            return None
    
    def parseDate(self,request):
        regex= r"(what)((')?s)?( )?((is )?the date|date is it|('s|is)? todays date| day is it)(.*)"
        match = re.search(regex,request)
        if match:
            return a_few_functions.returndate()
        else:
            return None
        
    def parseInspire(self,request):
        regex= r"(inspire me)(.*)"
        match = re.search(regex,request)
        if match:
            speech_number = random.randint(0,len(self.speeches))
            return self.speeches[str(speech_number)]
        else:
            return None

def main(command=None):
    p = parser()
    if not command:
        command = input("Enter command: ")
    attrs = (getattr(p,name) for name in dir(p) if not name.startswith('_'))
    methods = filter(callable, attrs)
    for method in methods:
        result = method(command)
        if result:
            return result
        
    return "I'm sorry, I don't know how to do that."
    

if __name__ == '__main__':
    print(main())