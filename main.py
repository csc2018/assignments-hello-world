from random import randint

#Read words in text file
print('Loading word list from file...')
f = open("words.txt", "r")
words = f.read()
f.close()
wordList = words.split()
wordNo = len(wordList)
print(wordNo, 'words loaded')

word = wordList[randint(0, wordNo - 1)]
result = "_" * len(word)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
guessNo = 10

def guess_character(character):
  global result
  global guessNo
  inWord = False
  for i in range(len(result)):
    if character == word[i]:
      result = result[0:i] + character + result[i+1:len(word)]
      inWord = True
  if not inWord:
    guessNo -= 1
    print("This letter is not in the word!")
    print("You have", guessNo, "guess(es) left.")
  else:
    print("Great guess!")
  print(result)

print("This word contains", len(word), "letters.")
while True:
  inputLetter = input("Enter a letter:")
  if len(inputLetter) == 1 and inputLetter in ALPHABET:
    guess_character(inputLetter)
  
  if word == result:
    print("You guessed the word!!11!1!!!!1!")
    break
  
  if guessNo == 0:
    print("You ran out of guesses...")
    print("The word is", word)
    break