import numpy
import pandas as pd
import os


def main():
    data_path = os.path.join(os.path.dirname((os.path.dirname(__file__))), 'DataSet')
    for direc in os.listdir(data_path):
        if os.path.isdir(os.path.join(data_path, direc)):
            text_miner(os.path.join(data_path, direc))


def text_miner(direc):
    stop_words = pd.read_csv(os.path.join(os.path.dirname((os.path.dirname(__file__))), 'stopwords.txt'), sep=",", header=None).values
    for fl in os.listdir(direc):
        if os.path.isfile(os.path.join(direc, fl)):
            with open (os.path.join(direc, fl)) as fle:
                lines = fle.readlines()
                ln = reduce(lambda x : x.strip().split(" "), lines)
                arr = numpy.array([])

                arr = numpy.array(ln)
                d = numpy.setdiff1d(arr, stop_words)

            numpy.load(os.path.join(direc, fl))




if __name__ == "__main__":
    main()
