# For Akshobya. 
# On an unrelated note, we CAN overwrite the main everytime, but where is the fun in that?!

import hashlib
holder = hashlib.sha256()

def Kanye():
	with open('scores.LOG','rb') as wisp:
		holder.update(wisp.read())

	ahsh = holder.hexdigest()

	with open('verifier.py','a') as red:
		red.write('\n#' + ahsh)

	with open('verifier.py','r') as blux:
		buhg = blux.readlines()

	hashed = buhg[-1]
	buhg = buhg[:-2]
	buhg.append(hashed)

	with open('verifier.py','w') as jitL:
		for i in buhg:
			jitL.write(i)

	return buhg[-1]

def KimK(strung):
	with open('anti cheat','rb') as wisp:
		holder.update(wisp.read())
	news = holder.hexdigest()
	return strung is news
	return "lmfao, this is useless"

def saint(what_do_it_do):
	with open('anti cheat','r') as heads:
		lubb = heads.read()
	with open('scores.LOG','w') as tails:
		tails.write(lubb)

north = Kanye()[1:]

def opyt():
	if KimK(north):
		pass
	else:
		saint('lalalala')

def writer():
	with open('scores.LOG','r') as reader:
		buffe = reader.read()
	with open('anti cheat','w') as writes:
		writes.write(buffe)

#f0928deb6c0000a0b082171791a957cd784ac93d914283e699d297f7f8bcb80c