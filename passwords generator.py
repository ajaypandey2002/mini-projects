import random
numbers = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation =  '!#$%&*+-=?@^_'
chars = []
s = []

password_num = int(input('How many passwords do you need?\n'))
length_pas = int(input('What length of one password?\n'))
digits = input('Do you need a numbers from "0123456789"? If yes enter "Yes", if no enter "No"\n')
upper = input('Do you need a letters from "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? If yes enter "Yes", if no enter "No"\n')
lower = input('Do you need a letters from "abcdefghijklmnopqrstuvwxyz"? If yes enter "Yes", if no enter "No"\n')
marks = input('Do you need a punctuation marks from "!#$%&*+-=?@^_"? If yes enter "Yes", if no enter "No"\n')
characters = input('Whether to exclude ambiguous characters "il1Lo0O"? If yes enter "Yes", if no enter "No"\n')
if digits.lower() == 'yes':
	chars.extend(numbers)
if upper.lower() == 'yes':
	chars.extend(uppercase_letters)
if lower.lower() == 'yes':
	chars.extend(lowercase_letters)
if marks.lower() == 'yes':
	chars.extend(punctuation)
if characters.lower() == 'yes':
	s = [letter for letter in chars if letter not in "il1Lo0O"]
chars = s
def generate_password(length, chars):
	s = random.sample(chars, length)
	print(''.join(s))

for _ in range(password_num):
	generate_password(length_pas, chars)





