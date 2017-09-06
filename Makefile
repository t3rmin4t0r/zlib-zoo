all: infgen/Makefile infgen/infgen column0.txt 
	gzip -2 < column0.txt |  ./infgen/infgen -x  | grep match | cut -f 2 -d ' ' | sort -n | uniq -c | sort -n -r -k 1 | column -t

infgen/Makefile:
	git submodule update --init --recursive

column0.txt: prices0.txt
	python double-plain.py

