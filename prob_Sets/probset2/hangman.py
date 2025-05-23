# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

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
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    flag = True
    for i in secret_word:
        if i not in ''.join(letters_guessed):
            flag = False
    return flag


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    final = ["*"]*len(secret_word)
    for idx,i in enumerate(secret_word):
        if i in letters_guessed:
            final[idx] = i
            
    return ''.join(final)

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_available = 'abcdefghijklmnopqrstuvwxyz'
    list_let_available = list(letters_available)
    
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i in letters_guessed:
            list_let_available.remove(i)
            
    return ''.join(list_let_available)


def help(secret_word, avaliable):
    # reveal_letter
    choose_from = ""
    for i in unique(secret_word):
        if i in avaliable:
            choose_from += i
            
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter
            

def unique(secret_word):
     Lnew = []
     for a in secret_word:
         if a not in Lnew:
             Lnew.append(a)
     return Lnew
        
        


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to Hangman!\nI am thinking of a word that is",len(secret_word)," letters long.")
    letters_guessed = []
    i = 10

    while i > 0 and not(has_player_won(secret_word, letters_guessed)):
        print("------------------------")
        print("you have",i,"guesses left.")
        print("Available letters: ", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ")
        
        if guess.isalpha():
            #we check whether guess is in letter_guessed
            if guess in ''.join(letters_guessed):
                print("Oops! You've already guessed that letter: ",get_word_progress(secret_word, letters_guessed))
            else: 
                letters_guessed.append(guess.lower())
            
            #we check whether guess is in secret_word
            if guess in secret_word:
                print("Good guess: ", get_word_progress(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word:", get_word_progress(secret_word, letters_guessed))
                if guess in "aeiou":
                    i -= 2  
                else: 
                    i -= 1
        
        elif guess == "!" and with_help == True:
            if i >= 3:
                revealed_letter =help(secret_word, get_available_letters(letters_guessed))
                
                letters_guessed.append(revealed_letter.lower())               
                print("Letter revealed: ", revealed_letter)
                print( get_word_progress(secret_word, letters_guessed))
                i -= 3
            else:
                print("Oops! Not enough guesses left:",get_word_progress(secret_word, letters_guessed))
            
        
        else:
            print("Oops! That is not a valid letter. Please input a letter from")
            
          
    print("------------------------")
    if has_player_won(secret_word, letters_guessed):
        print("Congratulations, you won!")
        #making list of unique chars in secret_word

        total_score = (i + 4*len(unique(secret_word))) + (3*len(secret_word))
        print("Your total score for this game is: ", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)
            




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

