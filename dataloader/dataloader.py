import pandas as pd


class csvTrackIdLoader:
    def __init__(self, csvPath: str, batchSize=1):
        """
        :param csvPath: path of csv file
        :param batchSize: batch size
        """
        self.filepath = csvPath
        self.df = pd.read_csv(csvPath)
        self.batchsize = batchSize
        self.startIndex = 0
        self.endIndex = 0

    def __len__(self):
        if len(self.df) % self.batchsize != 0:
            return len(self.df) // self.batchsize + 1
        else:
            return len(self.df) // self.batchsize

    def __iter__(self):
        return self

    def __next__(self):
        if self.startIndex >= len(self.df):
            raise StopIteration
        self.endIndex = self.startIndex + self.batchsize
        if self.endIndex >= len(self.df):
            self.endIndex = len(self.df)
        ans = list()
        for i, info in self.df[self.startIndex : self.endIndex].iterrows():
            ans.append(info["id"])

        self.startIndex += self.batchsize
        return ans
