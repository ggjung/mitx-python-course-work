# The 6.00 Word Game

# Code by g below helper code

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 3

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code

WORDLIST_FILENAME = "WK4_words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

# (end of helper code)
# -----------------------------------


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    # initialize score and make sure word is lowercase
    score = 0
    word.lower()
    
#    assertions on inputs, not used in course
#    assert len(word) != 0, "Word is blank"
#    assert type(n) == int, "Invalid hand size"
    
    # finds score of word based on letter
    for letter in word: 
        score += SCRABBLE_LETTER_VALUES[letter]
    
    # length multiplier
    score *= len(word)
    
    # all letters used bonus
    if n == len(word): 
        score +=50
        
    # return statement    
    return score

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # creates copy of hand to ensure hand is unchanged
    handResult = hand.copy()
    
    # deletes letters used in word from tempHand
    for letter in word: 
        handResult[letter] -= 1
        
    # return statement        
    return handResult
    
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # initializations
    inHand = False
    checkResult = False

    # make sure word is lower case
    word = word.lower()
    
    # check if word is in wordList and word in hand
    if wordList.count(word) == 1: 
        for letter in word: 
            if letter not in hand: 
                inHand = False
                break
            inHand = True
            
        if inHand: 
            convertedWord = getFrequencyDict(word)
            for key in convertedWord: 
                if convertedWord[key] > hand[key]: 
                    checkResult = False
                    break
                checkResult = True
                
    # return statement
    return checkResult

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # initializations
    handLength = 0
    
    # sums up total number of letters in hand
    for letter in hand: 
        handLength += hand[letter]
        
    # returns length of hand
    return handLength

#
# Game play
# 
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    totalScore = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:

        # Display the hand
        print("Current hand: ", end="")
        displayHand(hand)
        
        # Ask user for input
        userWord = input('Enter word, or a "." to indicate that you are finished: ')
        
        # If the input is a single period:
        if userWord == '.': 
        
            # End the game (break out of the loop)
            print("Goodbye! ", end="")
            break
            
        # Otherwise (the input is not a single period):
        else: 
            # If the word is not valid:
            if not isValidWord(userWord, hand, wordList):
            
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")
                print()

            # Otherwise (the word is valid):
            else: 
                userWordScore = getWordScore(userWord, n)
                totalScore += userWordScore
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                print('"' + userWord + '" earned ' + str(userWordScore) + ' points. Total: ' + str(totalScore) + ' points')
                print()
                
                # Update the hand 
                hand = updateHand(hand,userWord)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) == 0: 
        print("Run out of letters. ", end="")
        
    print("Total score: " + str(totalScore) + " points.")

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # initializations
    numberOfHands = 0

    # keep running game until break
    while True: 
        startFlag = False
        
        userChoice = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        
        # new game
        if userChoice == 'n': 
            while not startFlag: 
                playerChoice = input("Enter u to have yourself play, c to have the computer play: ")
                if playerChoice == 'u': 
                    userHand = dealHand(HAND_SIZE)
                    playHand(userHand,wordList,HAND_SIZE)
                    numberOfHands += 1
                    break
                elif playerChoice == 'c': 
                    userHand = dealHand(HAND_SIZE)
                    compPlayHand(userHand,wordList,HAND_SIZE)
                    numberOfHands += 1
                    break
                else: 
                    print("Invalid command.")
                
        # replay game
        elif userChoice == 'r': 
            if numberOfHands == 0: 
                print("You have not played a hand yet. Please play a new hand first!")
            else: 
                while not startFlag: 
                    playerChoice = input("Enter u to have yourself play, c to have the computer play: ")
                    if playerChoice == 'u': 
                        playHand(userHand,wordList,HAND_SIZE)
                        numberOfHands += 1
                        break
                    elif playerChoice == 'c': 
                        compPlayHand(userHand,wordList,HAND_SIZE)
                        numberOfHands += 1
                        break
                    else: 
                        print("Invalid command.")
        
        # end game
        elif userChoice == 'e': 
            break
        
        # catches invalid inputs
        else: 
            print("Invalid command.")    


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
