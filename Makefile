all: infgen/Makefile infgen/infgen column0.txt 

infgen/Makefile:
	git submodule update --init --recursive

column0.txt: prices0.txt
	python double-plain.py

