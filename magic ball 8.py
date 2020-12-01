import random
answers = ["Undoubtedly", "It seems to me - yes", "It is not clear yet, try again", "Don't even think",
"A foregone conclusion", "Most likely", "Ask later", "My answer is no",
"No doubt", "Good prospects", "Better not to tell",
"According to my information - no", "Definitely yes", "Signs say - yes", "Now it is impossible to predict",
"Prospects are not very good", "You can be sure of this", "Yes", "Concentrate and ask again", "Very doubtful"]
print("Hello World! I'm a magic ball and i know every answer for all your questions")
name = input('What is your name, bruh?\n')
print('Hello,', name)
while True:
	question = input('Ask me a question, and i will say what i think about it:\n')
	print(random.choice(answers))
	question = input('Do you wanna ask me again? Tell me "Yes", if you want, or "No", if not:\n')
	if question.lower() == 'yes':
		continue 
	else:
		print('Ok, bye-bye. Come back if you will have any questions')
		break 