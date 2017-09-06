from gzip import open as gzopen
import struct 
from itertools import izip_longest, imap

def data():
	for l in open("prices0.txt"):
		if l.strip() == "\N" : pass
		else : yield float(l.strip())

linear = open("column0.txt", "wb")
#hexdump = open("column1.txt", "wb")

def toHex(s):
	lst = []
	for ch in s:
		hv = hex(ord(ch)).replace('0x', '')
		if len(hv) == 1:
			hv = '0'+hv
		lst.append(hv)
	return reduce(lambda x,y:x+y, lst)

def pack(v):
	if v:
		print v, toHex(struct.pack("d", v))
		return struct.pack("d", v)
	else:
		return struct.pack("d", float("NaN"))

i  = 0 
for d in imap(lambda v : pack(v), data()):
	d = list(d)
	for v in d:
		linear.write(v)
	#hexdump.write(toHex(d))
	i  += 1
	#print toHex("".join(d))
	#print toHex("".join(mix(d)))
	# print "%024d\r" % i, 
linear.close()
#hexdump.close()
#vim: set ts=4
