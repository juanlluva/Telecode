# from nltk.corpus import stopwords

def rot13(phrase):
	abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	out_phrase = ""
	for rot in range(1,27):
		for char in phrase:
			out_phrase += abc[(abc.find(char)+rot)%27]
		splitted = out_phrase.split()
		# if splitted(1) in stopwords.words('spanish'):
			print(out_phrase)
			break

N = int(input())
for _ in range(N):
	phrase = input()
	rot13(phrase)

	
