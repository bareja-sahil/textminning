import re
import collections
import numpy
import pandas as pd
import os


def main():
    data_path = os.path.join(os.path.dirname((os.path.dirname(__file__))), 'DataSet')
    for direc in os.listdir(data_path):
        if os.path.isdir(os.path.join(data_path, direc)):
            text_miner(os.path.join(data_path, direc))


def text_miner(direc):
    stop_words = pd.read_csv(os.path.join(os.path.dirname((os.path.dirname(__file__))), 'stopwords.txt'), sep=",", header=None).values[0]
    stop_words = numpy.char.array(stop_words).upper()
    for fl in os.listdir(direc):
        if os.path.isfile(os.path.join(direc, fl)):
            with open(os.path.join(direc, fl)) as fle:
                lines = fle.readlines()
                # ln = map(lambda x : x.strip().split(" "), lines)
                arr = numpy.array([])
                for ln in lines:
                    words = re.sub(" +", " ", ln).strip().split(" ")
                    # To remove extra spaces from a word then split with word wise.
                    if words[0] != '':
                        words = map((lambda x:  re.sub('[^A-Za-z0-9]+', '', x.upper())), words)
                        arr = numpy.append(arr, words)
                # arr = numpy.array(ln)
                arr = numpy.vstack(numpy.unique(arr, return_counts=True)).T
                # arr = numpy.ma.masked_array(t.keys(), mask=())
                st = stop_words.reshape(len(stop_words), 1)[:, None]
                d = numpy.setdiff1d(arr, stop_words)
                stop_words.reshape(len(stop_words), 1)[:, None] == arr



            numpy.load(os.path.join(direc, fl))




if __name__ == "__main__":
    main()
