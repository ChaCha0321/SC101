"""
File: coin_flip_runs.py
Name:CHA_CHU WAN CHI
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random


def main():
	"""
	User input a number
	This program will print the answer about we flip the coin
	We will count when we flip to the same way, but repeat same way don't count
	until count to the run number
	"""
	print("Let's flip a coin!")
	run = int(input('Number of runs: '))
	# how many times you want to flip to same way
	time = 0
	check = 1
	a = random.randrange(1, 3)
	# random 1 or 2
	if a == 1:
		# 1 means front print H
		ans = 'H'
	else:
		# 2 means back print T
		ans = 'T'
	while time != run:
		# flip a coin until the time
		b = random.randrange(1, 3)
		if b == 1:
			ans += 'H'
		else:
			ans += 'T'
		if a == b and check == 1:
			time += 1
			check = -1
		elif a != b:
			check = 1
		a = b
	print(str(ans))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
