english_lowercase = 'abcdefghijklmnopqrstuvwxyz'
english_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = []
text = 'mama, papa, me'
text_s = []
marks = '" ! # @ $ ; % ^ : & ? * ( ) - + = , . / '.split(' ')
for i in range(len(text)):
	if text[i] not in marks:
		text_s.append(text[i])
text_s = ''.join(text_s)
text_s = text_s.split()
j = 0
for i in range(len(text)):	
	if text[i] in english_uppercase:
		s.append(english_uppercase[(english_uppercase.find(text[i]) + len(text_s[j]))%26])
	elif text[i] in english_lowercase:
		s.append(english_lowercase[(english_lowercase.find(text[i]) + len(text_s[j]))%26])
	else:
		s.append(text[i])
		if text[i] == ' ':
			j += 1

print(*s, sep = '')