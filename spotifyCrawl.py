import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import json
from tqdm import tqdm

input_csv = "./data/data.csv"

csv_input = pd.read_csv(input_csv)
print(csv_input["id"])

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id="60f4e82a30ec4a2ba657a2e8403e454a",
        client_secret="3acce0c5edde49d38e28d1c17b818c7c",
    )
)

for i, row in enumerate(tqdm(csv_input.iterrows(), ncols=80)):
    trackID = row[1]["id"]
    information = spotify.track(trackID)
    print(information)
