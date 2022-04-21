import random
from hangman_game import HangmanGame

# import all words from the file twl98.txt
def getWords(filename):
  with open(filename, 'r') as f:
    return f.read().splitlines() 

def main():
  # Get all the words in the 'twl98.txt'
  words = getWords('twl98.txt')
  # Get a random word from the word list 
  wordToGuess = random.choice(words)
  # Create a game 
  game = HangmanGame(wordToGuess)
  # While the game is still running...
  while not game.isGameOver():
    currentWord = game.getCurrentWord()
    print("HANGMAN: %s" % currentWord)
    # Get a letter from the user 
    letter = input("Guess a letter, or type hint if you would like a hint!")
    # If the user inputs hint, the game returns a correct letter for the user.
    if letter == 'hint':
      game.getHint()
    else:
      # Capitalize the inputs since the words in the txt file are all capitalized.
      game.guess(letter.upper())

main()