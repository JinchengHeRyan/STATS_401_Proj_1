import spotipy
import os
import time
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from tqdm import tqdm
from util.utils import *
from dataloader import csvTrackIdLoader
import argparse


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
    parser = argparse.ArgumentParser("Spotify Data Crawler")
    parser.add_argument(
        "--inputCSV",
        default="./data/smallSet/data.csv",
        type=str,
        required=False,
        help="input csv file which contains track IDs",
    )
    parser.add_argument(
        "--outputDir",
        default="./out_data/",
        type=str,
        required=False,
        help="output directory of the crawled data",
    )
    parser.add_argument(
        "--batchsize",
        default=50,
        type=int,
        required=False,
        help="batch size you want to crawl the data, 50 is recommended and is the maximum of being supported",
    )
    parser.add_argument(
        "--clientID",
        default="2f088e29c62846a3975616f763269566",
        type=str,
        required=False,
        help="client ID of your spotify development account",
    )
    parser.add_argument(
        "--clientSecret",
        default="bff923971e354eb4b13499a1b1d67d14",
        type=str,
        required=False,
        help="client secret of your spotify development account",
    )
    args = parser.parse_args()

    spotify = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(
            client_id=args.clientID,
            client_secret=args.clientSecret,
        ),
        # retries=1000000,
        requests_timeout=100,
    )

    # Assert the input csv file
    assert os.path.isfile(args.inputCSV), "No such input csv file: %s" % args.inputCSV

    # Create output csv file
    os.makedirs(args.outputDir, exist_ok=True)
    output_csv = os.path.join(
        args.outputDir, time.strftime("%Y-%m-%d-%H%M.csv", time.localtime(time.time()))
    )
    outFile = open(output_csv, "w")

    # input files path
    input_csv = args.inputCSV
    csv_input = pd.read_csv(input_csv)

    writeMetric_Name(outFile, metric_space)
    batchsize = args.batchsize
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
