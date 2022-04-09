import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import json
from tqdm import tqdm

# input files path
input_csv = "./data/data.csv"
output_csv = "./out_data/outData.csv"

csv_input = pd.read_csv(input_csv)
outFile = open(output_csv, "w")

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id="60f4e82a30ec4a2ba657a2e8403e454a",
        client_secret="3acce0c5edde49d38e28d1c17b818c7c",
    )
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
]


def get_metric(track_information, metric_space, spotify):
    ans = dict()
    for metric in metric_space:
        if metric == "trackID":
            trackID = track_information["id"]
            ans[metric] = trackID

        if metric == "artistID":
            artistID = track_information["artists"][0]["id"]
            ans[metric] = artistID

        if metric == "artistName":
            artistName = track_information["artists"][0]["name"]
            ans[metric] = artistName

        if metric == "album_artist_ID":
            album_artist_ID = track_information["album"]["artists"][0]["id"]
            ans[metric] = album_artist_ID

        if metric == "album_artist_name":
            album_artist_ID_name = track_information["album"]["artists"][0]["name"]
            ans[metric] = album_artist_ID_name

        if metric == "track_popularity":
            track_popularity = track_information["popularity"]
            ans[metric] = track_popularity

        if metric == "artist_popularity":
            artist_information = spotify.artist(ans["artistID"])
            artist_popularity = artist_information["popularity"]
            ans[metric] = artist_popularity

        if metric == "artist_genre":
            artist_information = spotify.artist(ans["artistID"])
            genre_inf = artist_information["genres"]
            if len(genre_inf) == 0:
                genre = ""
            else:
                genre = genre_inf[0]
            ans[metric] = genre

        if metric == "album_release_date":
            rl_date = track_information["album"]["release_date"]
            year = rl_date.split("-")[0]
            ans[metric] = year

    return ans


def writeMetric_Name(file, metric_space):
    ans = str()
    for metric in metric_space:
        ans += metric
        ans += ","
    ans += "\n"
    file.write(ans)


def writeMetric(file, metricInf, metric_space):
    ans = str()
    for metric in metric_space:
        ans += str(metricInf[metric])
        ans += ","
    ans += "\n"
    file.write(ans)


writeMetric_Name(outFile, metric_space)

for i, row in enumerate(tqdm(csv_input.iterrows(), ncols=80)):
    trackID = row[1]["id"]
    information = spotify.track(trackID)
    metric = get_metric(information, metric_space, spotify)
    writeMetric(outFile, metric, metric_space)
