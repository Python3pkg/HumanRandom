Human Random
============

This Python module aims to provide a way to allow programmers to "randomize" lists and generate "random" integers that feel random to humans. It is not statistically random. Many people express discontent with random lists because they get distracted with the patterns they find in repeating or sequential values. For example, if a die rolls a certain number a few times in a row the user will feel like it is rigged or unfairly balanced. Another example is in shuffling playlists; many times the same artist will play twice in a row, and many people dislike that.

##Usage

``` py
	HumanRandom.randint(min, max[, humanness_factor])
```

Return a "random" integer *N* such that `a <= N <= b`. You may also specify a "human-ness factor", which specifies how sparse you wish repeats to be.

``` py
	HumanRandom.shuffle(list[, humanness_factor])
```

Shuffle a list of items so that repeats are uncommon. Human-ness factor is the same as above. Tip: Use tuples to keep track of string IDs during the shuffling process.
