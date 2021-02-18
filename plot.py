from matplotlib import pyplot as plt
import os
import glob
import sys
import ntpath


x = [1, 2, 3, 4, 5]
y = [5, 7, 3, 8, 4]

#get file object reference to the file
file = open(sys.argv[1], "r")

#read content of file to string
data = file.read()

files = []
occurences=[]


if not os.path.exists('plots'):
    os.makedirs('plots')


for filepath in glob.iglob(r'questions/*/*.md', recursive=True):
    print(ntpath.basename(filepath))
    files.append(ntpath.basename(filepath))
    print(data.count(filepath))
    occurences.append(data.count(filepath))


plt.xticks(fontsize=4, rotation=90)
plt.plot(files,occurences)
plt.savefig("plots/plot.png")