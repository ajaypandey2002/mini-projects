
russian_lowercase = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
russian_uppercase = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
english_lowercase = 'abcdefghijklmnopqrstuvwxyz'
english_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encryption(ans, lan, k, t):
	s = []
	if ans == 1:
		if lan == 1:
			for i in range(len(t)):
				if t[i] in russian_uppercase:
					s.append(russian_uppercase[(russian_uppercase.find(text[i]) + k)%32])
				elif t[i] in russian_lowercase:
					s.append(russian_lowercase[(russian_lowercase.find(text[i]) + k)%32])
				else:
					s.append(t[i])
		if lan == 2:
			for i in range(len(t)):	
				if t[i] in english_uppercase:
					s.append(english_uppercase[(english_uppercase.find(text[i]) + k)%26])
				elif t[i] in english_lowercase:
					s.append(english_lowercase[(english_lowercase.find(text[i]) + k)%26])
				else:
					s.append(t[i])
	print(*s, sep = '')
def decryption(ans, lan, k, t):
	s = []
	if ans == 2:
		if lan == 1:
			for i in range(len(t)):
				if t[i] in russian_uppercase:
					s.append(russian_uppercase[(russian_uppercase.find(text[i]) - k)%32])
				elif t[i] in russian_lowercase:
					s.append(russian_lowercase[(russian_lowercase.find(text[i]) - k)%32])
				else:
					s.append(t[i])
		if lan == 2:
			for i in range(len(t)):	
				if t[i] in english_uppercase:
					s.append(english_uppercase[(english_uppercase.find(text[i]) - k)%26])
				elif t[i] in english_lowercase:
					s.append(english_lowercase[(english_lowercase.find(text[i]) - k)%26])
				else:
					s.append(t[i])
	print(*s, sep = '')

while True:
	answer = int(input('Что вас интересует? 1 - шифрование, 2 - дешифрование\n'))
	lang = int(input('На каком языке? 1 - русский, 2 - английский\n'))
	key = int(input('Укажите шаг сдвига (со сдвигом вправо):\n'))
	text = input('Введите текст:\n')
	if answer == 1:
		encryption(answer ,lang, key, text)
	else:
		decryption(answer, lang, key, text)
	loop = int(input('Нужно ли вам ещё что-то? 1 - да, 2 - нет\n'))
	if loop == 1:
		continue
	else:
		break




