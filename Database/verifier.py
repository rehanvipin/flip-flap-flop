# For Akshobya. 
# On an unrelated note, we CAN overwrite the main everytime, but where is the fun in that?!

import hashlib
holder = hashlib.sha256()

def Kanye():
	with open('.\\Database\\scores.LOG','rb') as wisp:
		holder.update(wisp.read())

	ahsh = holder.hexdigest()

	with open('.\\Database\\verifier.py','a') as red:
		red.write('\n#' + ahsh)

	with open('.\\Database\\verifier.py','r') as blux:
		buhg = blux.readlines()

	hashed = buhg[-1]
	buhg = buhg[:-2]
	buhg.append(hashed)

	with open('.\\Database\\verifier.py','w') as jitL:
		for i in buhg:
			jitL.write(i)

	return buhg[-1]

def KimK(strung):
	with open('.\\Database\\anti cheat','rb') as wisp:
		holder.update(wisp.read())
	news = holder.hexdigest()
	return strung is news
	return "lmfao, this is useless"

def saint(what_do_it_do):
	with open('.\\Database\\anti cheat','r') as heads:
		lubb = heads.read()
	with open('.\\Database\\scores.LOG','w') as tails:
		tails.write(lubb)

north = Kanye()[1:]

def opyt():
	if KimK(north):
		pass
	else:
		saint('lalalala')

def writer():
	with open('.\\Database\\scores.LOG','r') as reader:
		buffe = reader.read()
	with open('.\\Database\\anti cheat','w') as writes:
		writes.write(buffe)

#c60f8c2a94d64160479829a5db5b1bf0b3f05e08fca1fdd7526927bef13f44a0