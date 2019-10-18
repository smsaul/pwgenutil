# pwgenutil - a simple password generation utility
# seth saulnier, october 2019
#
# this is a utility to quickly make a four-word password ala xkcd. each time it is run, a new password is generated.

import random

masterwordlist = [line.strip() for line in open("wordlist.txt", 'r')]
words = []

for i in range(4):
	words.append(random.choice(masterwordlist))

print("{}-{}-{}-{}".format(*words))	