from hangman_graphics_controller import HangmanGraphicsController

class HangmanGame:
  
  '''A class for the hangman game which onsists of methods like guess, getHint, getCurrentWord, isGameOver, and _isValidGuess. These methods are used as logical ways to determine what to output, depending on the user input.'''

  def __init__(self, wordToGuess):
    self.graphicsController = HangmanGraphicsController(wordToGuess)
    self.wordToGuess = wordToGuess  
    self.alreadyGuessed = set()  
    self.lives = 6
  
  # Guess function to check if the user input is correct or not
  def guess(self, letter):
    if self._isValidGuess(letter):
      if letter in self.wordToGuess:  # Correct guess 
        self.graphicsController.correctGuess(letter)
        print("'%s' was a correct guess!" % letter)
      else:  # Incorrect guess 
        self.graphicsController.incorrectGuess(letter,self.wordToGuess)
        self.lives -= 1
        print("'%s' was an incorrect guess! %s lives remaining." % (letter, self.lives))
      # Add the letter to 'already guessed'
      self.alreadyGuessed.add(letter)
  
  # Reveals the first letter among the letters that are not yet revealed
  def getHint(self):
    for letter in self.wordToGuess:
      if letter not in self.alreadyGuessed:
        print("I've revealed the letter '%s' for you" % letter)
        self.graphicsController.correctGuess(letter)
        self.alreadyGuessed.add(letter)
        return 
  
  # Determines the word based on the correct inputs that the user has made
  def getCurrentWord(self):
    currentWord = ""
    for letter in self.wordToGuess:
      if letter in self.alreadyGuessed:
        currentWord += letter
      else:
        currentWord += "_"
    return currentWord

  def isGameOver(self):
    # 1. When the user runs out of lives 
    if self.lives <= 0:
      print("Game over - you lost! The word was '%s'" % self.wordToGuess)
      return True 
    # 2. When the user gets the correct answer 
    for i in range(len(self.wordToGuess)):
      if self.wordToGuess[i] not in self.alreadyGuessed:
        return False
    print("Game over - you won! The word was '%s'" % self.wordToGuess)
    return True

  # Determines whether the user input is a valid input
  def _isValidGuess(self, letter):
    # the user cannot input a word, except for hint
    if len(letter) != 1:
      print("You can only guess a single letter at a time!")
      return False 
    # The user cannot input the same letter more than once
    if letter in self.alreadyGuessed:
      print("You've already guessed the letter '%s'!" % letter)
      return False 
    return True
