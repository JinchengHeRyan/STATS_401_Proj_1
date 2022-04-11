## STATS Proj 1

### Team Member: [@Yixuan Li](https://github.com/austenoooo), [@Shuyi Guan](https://github.com/clairekeke), [@Jincheng He](https://github.com/JinchengHeRyan)

--------------------

This repo can be used to crawl spotify data

--------------------

#### Usage:

All the required packages are listed in `requirements.txt`, you can install by:

```shell
pip install -r requirements.txt
```

The descriptions of optional arguments are as the following

```
usage: Spotify Data Crawler [-h] [--inputCSV INPUTCSV] [--outputDir OUTPUTDIR]
                            [--batchsize BATCHSIZE] [--clientID CLIENTID]
                            [--clientSecret CLIENTSECRET]

optional arguments:
  -h, --help            show this help message and exit
  --inputCSV INPUTCSV   input csv file which contains track IDs
  --outputDir OUTPUTDIR
                        output directory of the crawled data
  --batchsize BATCHSIZE
                        batch size you want to crawl the data, 50 is
                        recommended and is the maximum of being supported
  --clientID CLIENTID   client ID of your spotify development account
  --clientSecret CLIENTSECRET
                        client secret of your spotify development account
```

Run the script:

```shell
python spotifyCrawl.py \
--inputCSV <input path of your csv file> \
--outputDir <directory to store the output csv file> \
--batchsize <batchsize> \
--clientID <your own clientID> \
--clientSecret <your own clientSecret>
```

All the above arguments are optional, if not being provided, the default value is set as the following:

```
inputCSV = "./data/smallSet/data.csv"
outputDir = "./out_data/"
batchsize = 50
clientID = "2f088e29c62846a3975616f763269566"
clientSecret = "bff923971e354eb4b13499a1b1d67d14"
```

**Please be aware that my clientID has limitation of the rate to crawl data and may cause failure**
