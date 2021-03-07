init:
		pip install -r requirements.txt

freeze:
		pip list > requirements.txt

test:
		pytest tests

createconfig:
		cp config.yml.example config.yml

# gentests:
# 		python3 main.py gentests

# generatepdf:
# 		python3 main.py genpdf

# sendemails:
# 		python3 main.py sendmails

# plot:
# 		python3 plot.py logs/$(logfilename)	

.PHONY: init test
