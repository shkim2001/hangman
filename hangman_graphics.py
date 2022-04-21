from graphics import Line, Point, Text, Rectangle, Circle

class HangmanPoleGraphic:
  
    '''A pole created with Zelle's graphics library. Consists of a pole for the Hangman to be hanged which consists of 4 lines. '''

    def __init__(self, window):
      poles = [
        Line(Point(600,150), Point(600,100)),  # Pole noose 
        Line(Point(600,100), Point(700,100)),  # Top horizontal pole bar  
        Line(Point(700,100), Point(700,500)),  # Vertical pole bar 
        Line(Point(550,500), Point(750,500))   # Pole base 
      ]
      for pole in poles:
        pole.draw(window)

# How to draw the WrongLettersBox
class WrongLettersBoxGraphic:

  '''A box created with Zelle's graphics library. Consists of a rectangle and a text.'''

  def __init__(self, window):
    self.wrongLetters = []
    frame = Rectangle(Point(50, 150), Point(450, 500))
    title = Text(Point(250, 175), "Wrong Letters")
    frame.draw(window)
    title.draw(window)

  # Add wrong letters to the rectangle, so that the users can see their previous inputs
  def addLetter(self, letter, wordToGuess, window):
    if letter not in wordToGuess:
      self.wrongLetters.append(letter)
      for i in range(len(self.wrongLetters)):
        wrong = Text(Point(250, 220 + 50 * self.wrongLetters.index(letter)), letter)
        wrong.draw(window)
        return
    
# How to draw a hangman
class HangmanGraphic:
  '''A hangman created with Zelle's graphics library. Consists of a circle and 5 lines.'''

  def __init__(self, window):
    self.window = window
    self.bodyParts = [
      Circle(Point(600,200),50),  # Head
      Line(Point(600,250),Point(600,375)),  # Body
      Line(Point(600,275),Point(650,290)),  # Left arm
      Line(Point(600,275),Point(550,290)),  # Right arm 
      Line(Point(600,375),Point(625,450)),  # Left leg 
      Line(Point(600,375),Point(575,450)),  # Right leg
      ]

  # Draw the hangman and remove the part already drawn from the list
  def draw(self):
    if len(self.bodyParts) > 0:
      self.bodyParts[0].draw(self.window)
      self.bodyParts.remove(self.bodyParts[0])


class CurrentGuessGraphic:
  '''A number of blanks created with Zelle's graphics library. Consists of n number of blanks, n being the length of the random word.'''
  def __init__(self, window, wordToGuess):
    self.wordToGuess = wordToGuess
    self.window = window 
    self.blanks = []

    blank_width = 30 
    blank_margin = 40 
    blank_x = 50 
    blank_y = 100
    
    # Draw n number of blanks, n being the length of the random word
    for letter in wordToGuess:
      blank = Line(Point(blank_x, blank_y), Point(blank_x + blank_width, blank_y))
      blank.draw(self.window)
      blank_x += blank_margin
      self.blanks.append(blank)

  # If the input letter is in the random word, draw out the text on the correct place.
  def reveal(self, letterGuessed):
    for (index, letter) in enumerate(self.wordToGuess):
      if letter == letterGuessed:
        blankPoint = self.blanks[index].getP1()
        textPointX = blankPoint.getX() + 15
        textPointY = blankPoint.getY() - 20
        text = Text(Point(textPointX, textPointY), letter)
        text.setSize(24)
        text.draw(self.window)
