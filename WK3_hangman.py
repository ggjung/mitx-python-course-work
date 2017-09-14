# Hangman game
#

# Code written by g
# comes after helper code
# requires list of words to play game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "WK3_words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    flag = True
    lettersInWord = []
    for char in secretWord: 
        if char not in lettersInWord: 
            lettersInWord.append(char)
    for i in range(len(lettersInWord)):
        if lettersInWord[i] not in lettersGuessed: 
            flag = False
    return flag


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''    
    lettersFlag = ""
    for char in secretWord: 
        if char in lettersGuessed: 
            lettersFlag += char
        else: 
            lettersFlag += "_ "
    return lettersFlag
        

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet = string.ascii_lowercase
    availableLetters = ""
    for char in alphabet: 
        if char not in lettersGuessed:
            availableLetters += char
    return availableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    guessesLeft = 8
    letter = ""

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    
    while not isWordGuessed(secretWord, lettersGuessed): 
        
        print ("-----------")
        print("You have " + str(guessesLeft) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        letter = input("Please guess a letter: ")     
        
        if letter in lettersGuessed: 
            print("Oops! You've already guessed that letter: ", end="")
        
        elif letter in secretWord: 
            print("Good guess: ", end="")
            lettersGuessed.append(letter)
                
        elif letter not in secretWord: 
            guessesLeft -= 1
            print("Oops! That letter is not in my word: ", end="")
            lettersGuessed.append(letter)
            
        elif letter not in getAvailableLetters(lettersGuessed): 
            print("Invalid character. Try again: ", end="")
            
        print (getGuessedWord(secretWord, lettersGuessed))
        
        if guessesLeft == 0: 
            print("Sorry, you ran out of guesses. The word was " + secretWord)
            break
        
    if guessesLeft != 0: 
        print("Congratulations, you won!")
        

# running the game...
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
