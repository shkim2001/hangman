# CS 111 Intro to Computer Science Final Project - Hangman

## Description

This program is a simple hangman game created in Python.

### Syntax: 

* python3 main.py

### Details

The user needs to guess the word that is randomly chosen from the list of words saved in the twl98.txt file. 
If the user inputs a letter, the program will respond whether or not the letter is in the randomly chosen word. 
If the letter is in the word, the program will print out the letter on the correct blank given on the upper side of the window. 
If the letter is not in the word, the program would print out the letter in the rectangle of wrong letters, and draw a section of the hangman. 
The user each gets 6 lives, and when it is all used, the user loses, and the game ends. 
If the user manages to guess the word within 6 lives, the user wins, and the game ends. 
If the user needs a hint, the user is allowed to type in 'hint', which would give them one of the letters that are not yet revealed. 

### Example 

#### Terminal Output
---------------------------------

HANGMAN: __________
Guess a letter, or type hint if you would like a hint!hint
I've revealed the letter 'C' for you
HANGMAN: C_________
Guess a letter, or type hint if you would like a hint!e
'E' was a correct guess!
HANGMAN: C___E__E__
Guess a letter, or type hint if you would like a hint!w
'W' was an incorrect guess! 5 lives remaining.
HANGMAN: C___E__E__
Guess a letter, or type hint if you would like a hint!q
'Q' was an incorrect guess! 4 lives remaining.
HANGMAN: C___E__E__
Guess a letter, or type hint if you would like a hint!hint
I've revealed the letter 'O' for you
HANGMAN: CO__E__E__
Guess a letter, or type hint if you would like a hint!n
'N' was a correct guess!
HANGMAN: CON_EN_EN_
Guess a letter, or type hint if you would like a hint!c
You've already guessed the letter 'C'!
HANGMAN: CON_EN_EN_
Guess a letter, or type hint if you would like a hint!t
'T' was a correct guess!
HANGMAN: CON_EN_ENT
Guess a letter, or type hint if you would like a hint!j
'J' was an incorrect guess! 3 lives remaining.
HANGMAN: CON_EN_ENT
Guess a letter, or type hint if you would like a hint!hint
I've revealed the letter 'V' for you
HANGMAN: CONVEN_ENT
Guess a letter, or type hint if you would like a hint!i
'I' was a correct guess!
Game over - you won! The word was 'CONVENIENT'

#### Graphics Output 

<img src="hangman/exampleWin.png" width="128"/>

#### Terminal Output
---------------------------------

HANGMAN: ____
Guess a letter, or type hint if you would like a hint!h
'H' was an incorrect guess! 5 lives remaining.
HANGMAN: ____
Guess a letter, or type hint if you would like a hint!a
'A' was an incorrect guess! 4 lives remaining.
HANGMAN: ____
Guess a letter, or type hint if you would like a hint!hint
I've revealed the letter 'R' for you
HANGMAN: R___
Guess a letter, or type hint if you would like a hint!i
'I' was an incorrect guess! 3 lives remaining.
HANGMAN: R___
Guess a letter, or type hint if you would like a hint!e
'E' was an incorrect guess! 2 lives remaining.
HANGMAN: R___
Guess a letter, or type hint if you would like a hint!hint
I've revealed the letter 'U' for you
HANGMAN: RU__
Guess a letter, or type hint if you would like a hint!n
'N' was an incorrect guess! 1 lives remaining.
HANGMAN: RU__
Guess a letter, or type hint if you would like a hint!g
'G' was an incorrect guess! 0 lives remaining.
Game over - you lost! The word was 'RUMP'

#### Graphics Output 

<img src="hangman/exampleLose.png" width="128"/>

---------------------------------