import re
import json
from json.decoder import JSONDecodeError
import spotify_access

f = open('patterns.json')
patterns = json.load(f)
def parseSpotify(request):
    regex = r"(^play)\s(.*)\s(by)\s(.*)"
    match = re.search(regex,request)
    if match:
        song = match.group(2)
        artist = match.group(4)
        return spotify_access.play(song,artist)
    else:
        return None

def main():
    result = parseSpotify("play "+input("What would you like to listen to?"))
    return result

if __name__ == '__main__':
    print(main())