import sys
import random
import os
import re
import yaml
import datetime

import themagen.log
import themagen.config
import themagen.users


_logger = themagen.log.get(__name__)  

def generate():
    try:
        cfg = themagen.config.read()
        users = themagen.users.read_csv()
        _cleanup()
        for user in users:
            _generate_file(user.full_name_sanitized, cfg)
    except:
        _logger.error('program exit with error')
        sys.exit(1)


def _generate_file(user, cfg):
    read_files = _generate_fx(cfg["categories"])
    print(f"Read files : {read_files}")
    _logger.info(f"user {user} - files {read_files}")

    with open("./assets/files/"+user+".md", "w") as outfile:
        outfile.write("![](./assets/files/images/ds_02-20-logo.png) \n")
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

    with open("./assets/files/"+user+".md", "a+") as outfile:
        count =1;
        for f in read_files:
            outfile.write("\n")
            outfile.write("## **Θέμα " + str(count) + "** \n")
            
            with open(f, "r") as infile:
                outfile.write(infile.read())
                count+=1
            outfile.write("\n")


def _generate_fx(categories):
    x_array = []
    category_names = list(categories.keys())
    cat_specs = categories.values()

    category_sizes = []
    category_selections = []
    for spec in cat_specs:
        category_sizes.append(spec['size'])
        category_selections.append(spec['select'])
    for i in range(len(category_names)):
        for k in range(category_selections[i]):
            l = random.sample(range(category_sizes[i]),category_selections[i])
            j = [category_names+1 for category_names in l]
            for w in j:
                k = "./assets/questions/" + category_names[i] + "/" + category_names[i] +"_" + str(w) + ".md"
            x_array.append(k)
            _logger.log(k)
    return x_array


def _cleanup():
    #cleanup
    dir = './assets/files'
    for f in os.listdir(dir):
        print(f)
        if os.path.isfile("./assets/files/" +f):
            if  not re.match(r"[a-z_]+.sh", f):
                print(f"match {f}")
                os.remove(os.path.join(dir, f))
