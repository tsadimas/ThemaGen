import sys
import random
import os
import re
import yaml
import datetime
import logging

# Gets or creates a logger
logger = logging.getLogger(__name__)  

# set log level
logger.setLevel(logging.INFO)

current_date_and_time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
current_date_and_time_string = str(current_date_and_time)
extension = ".log"


if not os.path.exists('logs'):
    os.makedirs('logs')

file_name =  "logs/" + current_date_and_time_string + extension
# define file handler and set formatter

file_handler = logging.FileHandler(file_name)
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

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
    #x = ['arch','class', 'gen','meth', 'req'] # categories
    x = list(categories.keys())
    cat_specs = categories.values()

    #y = [4, 3, 3, 3, 4] # number of questions available in each category 
    #z = [1, 2, 1, 2, 2] # number of questions that you want to create out of this category (should be less than number of questions on each category)
    y = []
    z = []
    for spec in cat_specs:
        y.append(spec['size'])
        z.append(spec['select'])
    for i in range(len(x)):
        for k in range(z[i]):
            l = random.sample(range(y[i]),z[i])
            j = [x+1 for x in l]
            for w in j:
                k="./questions/" + x[i] + "/" + x[i] +"_" + str(w) + ".md"
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