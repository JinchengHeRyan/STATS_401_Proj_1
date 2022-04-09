def get_metric(track_info, audio_info, metric_space, spotify, batchsize):
    ans = dict()
    artists_information = None
    for metric in metric_space:
        if metric == "trackID":
            ans[metric] = [track_info["tracks"][i]["id"] for i in range(batchsize)]

        elif metric == "artistID":
            ans[metric] = [
                track_info["tracks"][i]["artists"][0]["id"] for i in range(batchsize)
            ]

        elif metric == "artistName":
            ans[metric] = [
                track_info["tracks"][i]["artists"][0]["name"] for i in range(batchsize)
            ]

        elif metric == "album_artist_ID":
            ans[metric] = [
                track_info["tracks"][i]["album"]["artists"][0]["id"]
                for i in range(batchsize)
            ]

        elif metric == "album_artist_name":
            ans[metric] = [
                track_info["tracks"][i]["album"]["artists"][0]["name"]
                for i in range(batchsize)
            ]

        elif metric == "track_popularity":
            ans[metric] = [
                track_info["tracks"][i]["popularity"] for i in range(batchsize)
            ]

        elif metric == "artist_popularity":
            if artists_information is None:
                artists_information = spotify.artists(ans["artistID"])
            ans[metric] = [
                artists_information["artists"][i]["popularity"]
                for i in range(batchsize)
            ]

        elif metric == "artist_genre":
            if artists_information is None:
                artists_information = spotify.artists(ans["artistID"])

            genre_inf = [
                artists_information["artists"][i]["genres"] for i in range(batchsize)
            ]
            genre = list()
            for gen in genre_inf:
                if len(gen) == 0:
                    gen_now = ""
                else:
                    gen_now = gen[0]
                genre.append(gen_now)
            ans[metric] = genre

        elif metric == "album_release_date":
            # year = rl_date.split("-")[0]
            ans[metric] = [
                track_info["tracks"][i]["album"]["release_date"]
                for i in range(batchsize)
            ]

        elif metric == "danceability":
            ans[metric] = [audio_info[i]["danceability"] for i in range(batchsize)]

        elif metric == "valence":
            ans[metric] = [audio_info[i]["valence"] for i in range(batchsize)]

        elif metric == "tempo":
            ans[metric] = [audio_info[i]["tempo"] for i in range(batchsize)]

        elif metric == "energy":
            ans[metric] = [audio_info[i]["energy"] for i in range(batchsize)]

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


def writeMetric(file, metricInf, metric_space, batchsize):
    for i in range(batchsize):
        ans = str()
        for metric in metric_space:
            print("len = {}, metric = {}".format(len(metricInf[metric]), metric))
            ans += str(metricInf[metric][i])
            ans += ","
        ans += "\n"
        file.write(ans)
