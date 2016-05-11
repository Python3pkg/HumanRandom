import random
from difflib import SequenceMatcher

__int_history = []
__int_minmax = (0,0)

def shuffle(thelist, amt=1): # shuffle(items to shuffle[, randomness factor])
	if len(thelist) <= 1: return thelist
	random.shuffle(thelist)
	for h in range(0,int(amt)):
		i = 0
		while i < len(thelist):
			if type(thelist[i]) is str:
				if (SequenceMatcher(None, thelist[i], thelist[i-1]).ratio() * amt) > 0.5:
					thelist.insert(-1, thelist.pop(i))
			i += 1
	return thelist

def randint(min, max, amt=1): # randint(minimum value, maximum value[, randomness factor])
	global __int_history
	global __int_minmax

	if min != __int_minmax[0] or max != __int_minmax[1]:
		__int_minmax = (min,max)
		__int_history = []
	if len(__int_history) < 1:
		__int_history.append(random.randint(min,max))
		return __int_history[-1]
	j = random.randint(min,max)
	while (__int_history[-1] - (float(amt)/(max-min))) < j < (__int_history[-1] + (float(amt)/(max-min))):
		if random.random() < (1/float(amt)): break # Provide a random chance for this process to be skipped
		j = random.randint(min,max)
	__int_history.append(j)
	return j
