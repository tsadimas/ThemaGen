"""
Create Plot
"""
import os
import glob
import sys
import ntpath

from matplotlib import pyplot


def create(logfilename: str):
    _create_dir()
    data = _read_log(logfilename)
    _create_plot(data)


def _read_log(logfilename: str):
    with open(f'assets/logs/{logfilename}', "r") as f:
        data = f.read()
    return data


def _create_dir():
    if not os.path.exists('assets/plots'):
        os.makedirs('assets/plots')


def _create_plot(data):
    x = [1, 2, 3, 4, 5]
    y = [5, 7, 3, 8, 4]

    files = []
    occurences=[]

    for filepath in glob.iglob(r'assets/questions/*/*.md', recursive=True):
        print(ntpath.basename(filepath))
        files.append(ntpath.basename(filepath))
        print(data.count(filepath))
        occurences.append(data.count(filepath))

    pyplot.xticks(fontsize=4, rotation=90)
    pyplot.plot(files,occurences)
    pyplot.savefig("assets/plots/plot.png")