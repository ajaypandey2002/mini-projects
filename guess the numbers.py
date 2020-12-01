import random

print('Welcome to the guess the numbers! I thought of a number, and your task is to guess it.')
your_num = int(input('Enter the maximum number up to which we can play: '))
random_number = random.randint(1, your_num)
attempts = 0


def is_valid(num):
	if num.isdigit() == False:
		return False
	else:
		num = int(num)
		if num in range(1, 101):
			return True
		else:
			return False

while True:
	print('Enter an integer from 1 to', your_num, ': ')
	number = input()
	
	if is_valid(number) == False:
		print('Can you still enter an integer from 1 to 100?')
		continue
	else:
		number = int(number)
		if number < random_number:
			print('Your number is less than the guessed one, please try again')
			attempts += 1
			print('Attempts:', attempts)
			continue
		elif number > random_number:
			print('Your number is greater than the guessed one, please try again')
			attempts += 1
			print('Attempts:', attempts)
		else:
			print('You guessed it, congratulations!')
			attempts += 1
			print('Attempts:', attempts)
			answer = input('Do you want to play again? ("Yes", if you want or "No", if not)\n')
			if answer.lower() == 'no':
				break
			else:
				random_number = random.randint(1, 100)
				attempts = 0
				continue 

		



