from ps4a import *
import time

    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)

    # Create a new variable to store the best word seen so far (initially None)  

    # For each word in the wordList

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly


    # return the best word you found.


#
#
# Problem #6: Computer chooses a word
#
#
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
    max_score = 0
    best_word = ''
    for word in wordList:
        if len(word) > n:
            continue
        if isValidWordInHand(word, hand):
            score = getWordScore(word,n)
        else:
            continue
        if score > max_score:
            max_score = score
            best_word = word
    if best_word == '':
        return None
    else:
        return best_word
def isValidWordInHand(word, hand):
    hand_copy = hand.copy()
    for s in word:
        if hand_copy.get(s, 0) > 0:
            hand[s] -= 1
        else:
            return False
    return True

#
# Problem #7: Computer plays a hand
#
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
    # TO DO ... <-- Remove this comment when you code this function
    total_score = 0
    word_score = 0
    hand_copy = hand.copy()
    while True:
        # here: display hand
        if calculateHandlen(hand_copy) == 0:
            break

        print 'Current Hand: ',
        displayHand(hand_copy)

        chosen_word = compChooseWord(hand_copy, wordList, n)
        if chosen_word == None:
            break
        else:
            hand_copy = updateHand(hand_copy, chosen_word)
            word_score = getWordScore(chosen_word, n)
            total_score += word_score
            print '\"' + chosen_word + '\"',
            print ' earned ',
            print word_score,
            print ' points. Total: ',
            print total_score,
            print ' points'
    print 'Total score: ', 
    print total_score,
    print ' points.'
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    aHand = {}
    while True:
        command = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if command == 'n':
            aHand = dealHand(HAND_SIZE)
            whoPlays(aHand, wordList, HAND_SIZE)
        elif command == 'r':
            if aHand == {}:
                print 'You have not played a hand yet. Please play a new hand first!\n'
            else:
                whoPlays(aHand,wordList, HAND_SIZE)
        elif command == 'e':
            break
        else:
            print 'Invalid command.\n'
def whoPlays(aHand, wordList, n):
    while True:
        subcmd = raw_input('Enter u to have yourself play, c to have the computer play: ')
        if subcmd == 'u': # player
            playHand(aHand, wordList, n)
            break
        elif subcmd == 'c': #computer
            compPlayHand(aHand, wordList, n)
            break
        else:
            print 'Invalid command.\n'



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


