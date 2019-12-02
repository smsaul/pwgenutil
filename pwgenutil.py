# pwgenutil - a simple password generation utility
# seth saulnier, december 2019
#
# this is a utility to quickly make a multi-word password ala xkcd. each time it is run, a new password is generated.
# pass 2, 3, or 4 to pick length

import random, sys

masterwordlist = [line.strip() for line in open("wordlist.txt", 'r')]
words = []


if len(sys.argv) == 1: #default no argument to full length
	for i in range(4):
		words.append(random.choice(masterwordlist))
	print("{}-{}-{}-{}".format(*words))
elif sys.argv[1] == "2":
	for i in range(2):
		words.append(random.choice(masterwordlist))
	print("{}-{}".format(*words))
elif sys.argv[1] == "3":
	for i in range(3):
		words.append(random.choice(masterwordlist))
	print("{}-{}-{}".format(*words))
else: #if not 2 or 3, you get 4
	for i in range(4):
		words.append(random.choice(masterwordlist))
	print("{}-{}-{}-{}".format(*words))
