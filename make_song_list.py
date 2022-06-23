#library imports
import json
from re import S
import requests
import requests
from Song import Song
#This is a function that recieves a spotify playlist link and returns a list of song objects
def make_song_list(playlist_url):

    #an id for the playlist, taken from the url by taking a specific part
    playlist_id = playlist_url[34:56]
    
    #URL created on spotify site, where it will return the list of songs and artists, based off the given fields
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}?fields=tracks.items(track(name%2C%20artists(name)))"
    
    #Headers for spotify
    headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
    "Authorization": "Bearer BQBxgAXjahBAp9dE0f8bWn1sp7lpkJ6-cCZPfjdZKnslkyBYsWY2QEH4bMcibX_GdrnO0MMWJm_9WtNoirklrSxC--wNhRwwJz-biE8C_onUNVi2gy_ubJItbwjIwvICb0qtxysc1c7GpcZhsmanTrCH-URRVHuNBlSavDfmoKpEqlhV3Per65c7fstHI5fbQxg"
    }

    #Make request to spotify
    response = requests.request("GET", url, headers=headers)
    
    #converting to json 
    response_json = json.loads(response.text)
    
    #create a song list to return
    song_list = []

    
    #go over all songs we recieved, and create a song object for each
    for song, index in enumerate(response_json['tracks']['items']):

        artists = []

        for  artist,k in enumerate(index['track']['artists']):
            artists.append(k['name'])

        song_list.append(Song(index['track']['name'], artists ))

    return song_list

songs = make_song_list("https://open.spotify.com/playlist/3xb0H0BQTbQltzWaKfdgHi?si=b9d63c50b0164f6e")
for song in songs:
    print (song)