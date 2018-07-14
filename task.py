import os
from collections import Counter

FILENAME = 'mbox.txt'

def parse(filename):
	letters = []
	date_string = 'Date:'
	from_string = 'From:'
	subj_string = 'Subject:'
	current_letter_sender = ''
	current_letter_date = ''
	with open(filename, 'r') as f:
		for line in f:
			if line.startswith(date_string):
				current_letter_date = line.lstrip(date_string).strip()
			if line.startswith(from_string):
				current_letter_sender = line.lstrip(from_string).strip()
			if line.startswith(subj_string):
				letters.append([current_letter_sender, current_letter_date, line.lstrip(subj_string).strip()])	
	return letters


def output(letters):
	print('Letters:')
	for letter in letters:
		print('{0} ({1}): {2}'.format(*letter))
	print('Senders:')
	senders = dict(Counter(letter[0] for letter in letters))
	for key, value in senders.items():
		print('{0} : {1}'.format(key, value))


def test_task(filename):
	letters = parse(FILENAME)
	output(letters)

test_task(FILENAME)
