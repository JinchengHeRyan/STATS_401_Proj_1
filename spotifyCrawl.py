import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from tqdm import tqdm
from util.utils import *

# input files path
input_csv = "./data/smallSet/data.csv"
output_csv = "./out_data/smallSet/outData.csv"

csv_input = pd.read_csv(input_csv)
outFile = open(output_csv, "w")

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id="60f4e82a30ec4a2ba657a2e8403e454a",
        client_secret="3acce0c5edde49d38e28d1c17b818c7c",
    ),
    # retries=1000000,
    requests_timeout=100,
)

metric_space = [
    "trackID",
    "artistID",
    "artistName",
    "album_artist_ID",
    "album_artist_name",
    "track_popularity",
    "artist_popularity",
    "artist_genre",
    "album_release_date",
    "danceability",
    "valence",
    "tempo",
    "energy",
]


if __name__ == "__main__":
    writeMetric_Name(outFile, metric_space)

    for i, row in enumerate(tqdm(csv_input.iterrows(), ncols=80)):
        try:
            trackID = row[1]["id"]
            information = spotify.track(trackID)
            info = spotify.audio_features(trackID)[0]
            metric = get_metric(information, info, metric_space, spotify)
            writeMetric(outFile, metric, metric_space)
        except:
            continue
