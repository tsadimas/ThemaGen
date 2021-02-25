import sys
import random
import os
import re
import yaml
import datetime

import log

# Gets or creates a logger
logger = log.get(__name__)  

logger.info('******* start ***********')

# read config
config_file = "config.yml"


try:
    f = open(config_file, 'r')
except OSError:
    print(f"Could not open/read file: {config_file}")
    sys.exit()

with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

categories = cfg["categories"]

def generate_fx():
    category_names = list(categories.keys())
    cat_specs = categories.values()

    category_sizes = []
    catogory_selections = []
    for spec in cat_specs:
        category_sizes.append(spec['size'])
        catogory_selections.append(spec['select'])
    for i in range(len(category_names)):
        for k in range(catogory_selections[i]):
            l = random.sample(range(category_sizes[i]),catogory_selections[i])
            j = [category_names+1 for category_names in l]
            for w in j:
                k="./questions/" + category_names[i] + "/" + category_names[i] +"_" + str(w) + ".md"
            x_array.append(k)
    return x_array

print(generate_fx)


#cleanup
dir = './files'
for f in os.listdir(dir):
    print(f)
    if os.path.isfile("./files/" +f):
        if  not re.match(r"[a-z_]+.sh", f):
            print(f"match {f}")
            os.remove(os.path.join(dir, f))



def generate_file(user):
    
    read_files = [] 
    for i in generate_fx():
        read_files.append(i)

    print(f"Read files : {read_files}")
    logger.info(f"user {user} - files {read_files}")

    with open("files/"+user+".md", "w") as outfile:
        outfile.write("![](./files/images/ds_02-20-logo.png) \n")
        outfile.write("\n")
        #outfile.write("## Χαροκόπειο Πανεπιστήμιο - Τμήμα Πληροφορικής και Τηλεματικής \n")
        #outfile.write("## Kατανεμημένα Συστήματα \n")
        outfile.write("\n")
        outfile.write("Χρήστης **" + user + "**")
        outfile.write("\n")
        outfile.write("\n")
        outfile.write("Το κάθε θέμα πιάνει 1.25 πόντους")
        outfile.write("\n")
        outfile.write("\n")

    with open("files/"+user+".md", "a+") as outfile:
        count =1;
        for f in read_files:
            outfile.write("\n")
            outfile.write("## **Θέμα " + str(count) + "** \n")
            
            with open(f, "r") as infile:
                outfile.write(infile.read())
                count+=1
            outfile.write("\n")

print(f"Arguments count: {len(sys.argv)}")
for i, arg in enumerate(sys.argv):
    print(f"Argument {i:>6}: {arg}")
    if i>=1:
        x_array=[]
        generate_file(arg)