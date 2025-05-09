import bs4
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://open.spotify.com/",
        client_id= "8014bc0dc9a94f49bd2d5df97c1b5e6e",
        show_dialog=True,
        client_secret="534acf9bda0f4baaa71de402420b75f2",
        cache_path="token.txt",
        username="Sneaky"
    )
)
user_id = sp.current_user()["id"]
choice = input("Which year do you want to travel to?\nType the date in this format YYYY-MM-DD:")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

url = "https://www.billboard.com/charts/hot-100/" + choice

response = requests.get(url=url,headers=header)

soup =bs4.BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

song_uris = []
year = choice.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on Spotify")

playlist = sp.user_playlist_create(user=user_id, name=f"{choice} Billboard 100",public=False)

sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)