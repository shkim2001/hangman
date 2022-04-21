Game of Hangman
Sunny Kim & Nic Berry
Time Taken : 5 hours

The user needs to guess the word that is randomly chosen from the list of words saved in the twl98.txt file. If the user inputs a letter, the program will respond whether or not the letter is in the randomly chosen word. If the letter is in the word, the program will print out the letter on the correct blank given on the upper side of the window. If the letter is not in the word, the program would print out the letter in the rectangle of wrong letters, and draw a section of the hangman. The user each gets 6 lives, and when it is all used, the user loses, and the game ends. If the user manages to guess the word within 6 lives, the user wins, and the game ends. If the user needs a hint, the user is allowed to type in 'hint', which would give them one of the letters that are not yet revealed. 

In order to draw the window and choose a random word, we used the graphics.py file and twl98.txt file given to us during the course.

There are no bugs that we know of, but some improvements can be made by limiting the number of hints that the users can use or by giving them more lives by adding more strokes to the hangman(examples might be face or clothes on the hangman). Also, when one game is over, the program ends so the user needs to run the program again. When the user runs the program again, it might take some time for the window to reset back to its initial window.