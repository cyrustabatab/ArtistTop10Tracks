import spotipy
import tkinter
from tkinter import messagebox
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint


# TODO try and get centered text output

CLIENT_ID ="CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
REDIRECT_URI = "https://127.0.0.1/9090"



auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET)


sp = spotipy.Spotify(auth_manager=auth_manager)



def get_top_10_tracks(artist_uri):


    results = sp.artist_top_tracks(artist_uri)
    
    for i,(label,track) in enumerate(zip(labels,results['tracks'])):
        label['text'] = f"{i +1:>2}. {track['name']}"

def get_artist():

    artist = artist_entry.get()
    if not artist:
        messagebox.showerror(title="Error",message="Please enter artist")
    else:
        results = sp.search(q=f'artist:{artist}',limit=1)
        artist_uri = (results['tracks']['items'][0]['artists'][0]['uri'])
        get_top_10_tracks(artist_uri)





font = ("Arial",40,"bold")
small_font = ("Arial",20,"bold")


window = tkinter.Tk()
window.title("Top 10 Track Finder")
window.configure(padx=20,pady=20)


title_label = tkinter.Label(text="Top 10 Tracks",font=font)
title_label.pack(pady=50)


info_label = tkinter.Label(text="Enter Artist Name",font=font)
info_label.pack()


artist_entry = tkinter.Entry(font=font)
artist_entry.focus_set()
artist_entry.pack()

button = tkinter.Button(text="GET",font=font,command=get_artist)
button.pack(pady=10)
labels = []

for i in range(10):
    label = tkinter.Label(text='',font=small_font)
    label.pack(anchor=tkinter.W)
    labels.append(label)






window.mainloop()











