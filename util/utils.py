def get_metric(track_information, audio_info, metric_space, spotify):
    ans = dict()
    for metric in metric_space:
        if metric == "trackID":
            trackID = track_information["id"]
            ans[metric] = trackID

        elif metric == "artistID":
            artistID = track_information["artists"][0]["id"]
            ans[metric] = artistID

        elif metric == "artistName":
            artistName = track_information["artists"][0]["name"]
            ans[metric] = artistName

        elif metric == "album_artist_ID":
            album_artist_ID = track_information["album"]["artists"][0]["id"]
            ans[metric] = album_artist_ID

        elif metric == "album_artist_name":
            album_artist_ID_name = track_information["album"]["artists"][0]["name"]
            ans[metric] = album_artist_ID_name

        elif metric == "track_popularity":
            track_popularity = track_information["popularity"]
            ans[metric] = track_popularity

        elif metric == "artist_popularity":
            artist_information = spotify.artist(ans["artistID"])
            artist_popularity = artist_information["popularity"]
            ans[metric] = artist_popularity

        elif metric == "artist_genre":
            artist_information = spotify.artist(ans["artistID"])
            genre_inf = artist_information["genres"]
            if len(genre_inf) == 0:
                genre = ""
            else:
                genre = genre_inf[0]
            ans[metric] = genre

        elif metric == "album_release_date":
            rl_date = track_information["album"]["release_date"]
            # year = rl_date.split("-")[0]
            ans[metric] = rl_date

        elif metric == "danceability":
            ans[metric] = audio_info["danceability"]

        elif metric == "valence":
            ans[metric] = audio_info["valence"]

        elif metric == "tempo":
            ans[metric] = audio_info["tempo"]

        elif metric == "energy":
            ans[metric] = audio_info["energy"]

        else:
            raise AssertionError

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
