def ScoreOfLetter(letter):
	letter = letter.upper()
	score = {
		'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
		'D': 2, 'G': 2,
		'B': 3, 'C': 3, 'M': 3, 'P': 3,
		'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
		'K': 5,
		'J': 8, 'X': 8,
		'Q': 10, 'Z': 10
		}
	return score.get(letter, 0)


def ScoreOfWord(word):
	sum = 0
	for i in word:
		sum += ScoreOfLetter(i)
	return sum


def ScoreOfText(text):
	sum = 0
	text = text.split()
	for i in text:
		#one letter words are not allowed
		if len(i) > 1:
			sum += ScoreOfWord(i)
	return sum


def ScoreOfFile(filepath):
	FileRead = open(filepath, 'r')
	return ScoreOfText(FileRead.read())


def main():
	filepath = #insert file path here
	print(ScoreOfFile(filepath))
	return 0


if __name__ == '__main__':
	main()