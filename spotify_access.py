import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import json
from json.decoder import JSONDecodeError
import os
username = "shahkush"
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
device = None

f = open('spotify_creds.json')
credentials = json.load(f)


cid = credentials['CID']
secret = credentials['SECRET'] 
f.close()
try:
    token = util.prompt_for_user_token(username, scope,cid,secret,redirect_uri="http://localhost:8888/callback/")
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp = spotipy.Spotify(auth=token)

for d in sp.devices()['devices']:
    if d['name'] == 'KUSH-PC':
        device = d['id']
    print(d)

def searchSong(song,debug=False):
    results = sp.search(q=song, limit=50,type='track')
    tracks = results['tracks']['items']
    if debug:
        for t in tracks:
            print(f"song: {t['name']} by {t['album']['artists'][0]['name']}")
    return results

def play(song,artist=None):
    results = searchSong(song)
    tracks = results['tracks']['items']
    for t in tracks:
        if t['album']['artists'][0]['name'].lower() == artist.lower() and t['name'].lower() == song.lower():
            #add song to queue and skip to it
            # implemented this way becuase sp.start_playback(device_id=device, uris=[track['uri']]) plays the song and clears the queue
            #this will play the song and continue playing the queue
            sp.add_to_queue(t['uri'], device)
            sp.next_track(device)
            return f"{t['name']} by {t['album']['artists'][0]['name']}"   
def main():
    while True:
    #    print(play(input("Enter song name: "),input("Enter artist name: ")))
       searchSong(input("Enter song name: "),debug=True)

if __name__ == '__main__':
    main()