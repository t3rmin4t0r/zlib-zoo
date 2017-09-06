all: infgen infgen/infgen column0.txt 

infgen:
	git submodule update --recursive --remote

column0.txt: prices0.txt
	python double-plain.py

