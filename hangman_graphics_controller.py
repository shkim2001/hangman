from graphics import GraphWin 
from hangman_graphics import HangmanPoleGraphic, WrongLettersBoxGraphic, HangmanGraphic, CurrentGuessGraphic

class HangmanGraphicsController:
  
    '''A class which has the methods correctGuess and incorrectGuess, which is used to determine where to draw the letter that the user inputted, depending on whether the letter is in the randomWord '''

    def __init__(self, wordToGuess):
      # Set the window size and draw the graphics which are set in another class called hangman_graphics beforehand
      self.window = GraphWin("HangmanFrame", 1000, 1000)
      self.hangmanPole = HangmanPoleGraphic(self.window)
      self.wrongLetterBox = WrongLettersBoxGraphic(self.window)
      self.hangman = HangmanGraphic(self.window)
      self.currentGuessWindow = CurrentGuessGraphic(self.window, wordToGuess)

    # If the guess is correct, the letter will be drawn in the currentGuessWindow
    def correctGuess(self, letter):
      self.currentGuessWindow.reveal(letter)

    # If the guess is incorrect, the letter will be drawn in the wrongLetterBox
    def incorrectGuess(self, letter, wordToGuess):
      self.wrongLetterBox.addLetter(letter,wordToGuess,self.window)
      self.hangman.draw()
