import random
from difflib import SequenceMatcher

_int_history = []
_int_minmax = (0,0)

def shuffle(thelist, amt=1): # shuffle(items to shuffle[, randomness factor])
	if len(thelist) <= 1: return thelist
	random.shuffle(thelist)
	for h in range(0,int(amt)):
		i = 0
		while i < len(thelist):
			if type(thelist[i]) is str: # todo: allow the use of any type within the list
				if (SequenceMatcher(None, str(thelist[i]), str(thelist[i-1])).ratio() * amt) > 0.5:
					thelist.insert(-1, thelist.pop(i))
			i += 1
	return thelist

def randint(min, max, amt=1): # randint(minimum value, maximum value[, randomness factor])
	global _int_history
	global _int_minmax

	if min != _int_minmax[0] or max != _int_minmax[1]:
		_int_minmax = (min,max)
		_int_history = []
	if len(_int_history) < 1:
		_int_history.append(random.randint(min,max))
		return _int_history[-1]
	j = random.randint(min,max)
	while (_int_history[-1] - (float(amt)/(max-min))) < j < (_int_history[-1] + (float(amt)/(max-min))):
		if random.random() < (1/float(amt)): break # Provide a random chance for this process to be skipped
		j = random.randint(min,max)
	_int_history.append(j)
	return j
