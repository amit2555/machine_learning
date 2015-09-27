#!/usr/bin/python

#Probability of both girls on the condition atleast one child is a girl

import random

def random_kid():
	return random.choice(['boy','girl'])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)
for _ in range(10000):
	older = random_kid()
	younger = random_kid()
	if older == 'girl':
		older_girl+=1
	if older == 'girl' and younger == 'girl':
		both_girls+=1
	if older == 'girl' or younger == 'girl':
		either_girl+=1

print "P(both | older):%5f"%(both_girls/older_girl)
print "P(both | either):%5f"%(both_girls/either_girl)
