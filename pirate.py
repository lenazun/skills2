
VOCABULARY = {'sir': 'matey', 
			'hotel': 'feabag inn',
			'student': 'swabbie',
			'boy': 'matey',
			'madam': 'proud beauty',
			'professor': 'foul blaggart',
			'restaurant': 'galley',
			'your': 'yer',
			'excuse': 'arr',
			'students': 'swabbies',
			'are': 'be',
			'lawyer': 'foul blaggart',
			'the': 'th\'',
			'restroom': 'head',
			'my': 'me',
			'hello': 'avast',
			'is': 'be',
			'man': 'matey'
		}



def pirate_translator(sentence):

	sentence = sentence.lower()
	sentence = sentence.split()
	returned = []

	for i in sentence:
		if i in VOCABULARY:
			returned.append(VOCABULARY[i])
		else:
			returned.append(i)

	print ' '.join(returned)



def main():
	print "What's your sentence matey?"
	sentence = raw_input('>')

	pirate_translator(sentence)


if __name__ == "__main__":
	main()
	