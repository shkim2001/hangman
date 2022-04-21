# CS 111 Intro to Computer Science Final Project - Hangman

## Description

This program is a simple hangman game created in Python.

### Syntax: 

* python3 main.py

### Details

The user needs to guess the word that is randomly chosen from the list of words saved in the twl98.txt file. 
<br> If the user inputs a letter, the program will respond whether or not the letter is in the randomly chosen word. 
<br> If the letter is in the word, the program will print out the letter on the correct blank given on the upper side of the window. 
<br> If the letter is not in the word, the program would print out the letter in the rectangle of wrong letters, and draw a section of the hangman. 
<br> The user each gets 6 lives, and when it is all used, the user loses, and the game ends. 
<br> If the user manages to guess the word within 6 lives, the user wins, and the game ends. 
<br> If the user needs a hint, the user is allowed to type in 'hint', which would give them one of the letters that are not yet revealed. 

### Example 

#### Terminal Output
---------------------------------

HANGMAN: __________
<br> Guess a letter, or type hint if you would like a hint!hint
<br> I've revealed the letter 'C' for you
<br> HANGMAN: C_________
<br> Guess a letter, or type hint if you would like a hint!e
<br> 'E' was a correct guess!
<br> HANGMAN: C___E__E__
<br> Guess a letter, or type hint if you would like a hint!w
<br> 'W' was an incorrect guess! 5 lives remaining.
<br> HANGMAN: C___E__E__
<br> Guess a letter, or type hint if you would like a hint!q
<br> 'Q' was an incorrect guess! 4 lives remaining.
<br> HANGMAN: C___E__E__
<br> Guess a letter, or type hint if you would like a hint!hint
<br> I've revealed the letter 'O' for you
<br> HANGMAN: CO__E__E__
<br> Guess a letter, or type hint if you would like a hint!n
<br> 'N' was a correct guess!
<br> HANGMAN: CON_EN_EN_
<br> Guess a letter, or type hint if you would like a hint!c
<br> You've already guessed the letter 'C'!
<br> HANGMAN: CON_EN_EN_
<br> Guess a letter, or type hint if you would like a hint!t
<br> 'T' was a correct guess!
<br> HANGMAN: CON_EN_ENT
<br> Guess a letter, or type hint if you would like a hint!j
<br> 'J' was an incorrect guess! 3 lives remaining.
<br> HANGMAN: CON_EN_ENT
<br> Guess a letter, or type hint if you would like a hint!hint
<br> I've revealed the letter 'V' for you
<br> HANGMAN: CONVEN_ENT
<br> Guess a letter, or type hint if you would like a hint!i
<br> 'I' was a correct guess!
<br> Game over - you won! The word was 'CONVENIENT'

#### Graphics Output 

<img src="https://github.com/shkim2001/hangman/blob/main/exampleWin.png?raw=true" width="128"/>

#### Terminal Output
---------------------------------

<br> HANGMAN: ____
<br> Guess a letter, or type hint if you would like a hint!h
<br> 'H' was an incorrect guess! 5 lives remaining.
<br> HANGMAN: ____
<br> Guess a letter, or type hint if you would like a hint!a
<br> 'A' was an incorrect guess! 4 lives remaining.
<br> HANGMAN: ____
<br> Guess a letter, or type hint if you would like a hint!hint
<br> I've revealed the letter 'R' for you
<br> HANGMAN: R___
<br> Guess a letter, or type hint if you would like a hint!i
<br> 'I' was an incorrect guess! 3 lives remaining.
<br> HANGMAN: R___
<br> Guess a letter, or type hint if you would like a hint!e
<br> 'E' was an incorrect guess! 2 lives remaining.
<br> HANGMAN: R___
<br> Guess a letter, or type hint if you would like a hint!hint
<br> I've revealed the letter 'U' for you
<br> HANGMAN: RU__
<br> Guess a letter, or type hint if you would like a hint!n
<br> 'N' was an incorrect guess! 1 lives remaining.
<br> HANGMAN: RU__
<br> Guess a letter, or type hint if you would like a hint!g
<br> 'G' was an incorrect guess! 0 lives remaining.
<br> Game over - you lost! The word was 'RUMP'

#### Graphics Output 

<img src="https://github.com/shkim2001/hangman/blob/main/exampleLose.png?raw=true" width="128"/>

---------------------------------