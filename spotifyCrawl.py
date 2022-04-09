import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from tqdm import tqdm
from util.utils import *
from dataloader import csvTrackIdLoader

# input files path
input_csv = "./data/smallSet/data.csv"
output_csv = "./out_data/smallSet/outData.csv"

csv_input = pd.read_csv(input_csv)
outFile = open(output_csv, "w")

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id="2f088e29c62846a3975616f763269566",
        client_secret="bff923971e354eb4b13499a1b1d67d14",
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
    batchsize = 50
    id_loader = csvTrackIdLoader(csvPath=input_csv, batchSize=batchsize)

    for i, trackIDs in enumerate(tqdm(id_loader, ncols=80)):
        try:
            tracks_info = spotify.tracks(trackIDs)
            audios_info = spotify.audio_features(trackIDs)
            metric = get_metric(
                tracks_info, audios_info, metric_space, spotify, batchsize
            )
            writeMetric(outFile, metric, metric_space, batchsize)
            tqdm.write("Success!")
        except:
            tqdm.write("Fail!")
