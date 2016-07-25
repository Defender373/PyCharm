import string

lettersGuessed = []


def replaceGuessed(x):
    if x in lettersGuessed:
        return x
    else:
        return '_'


def getGuessedWord(secretWord, lettersGuessed):
    return ''.join([replaceGuessed(x) for x in secretWord])


def filterGuessed(x):
    return not (x in lettersGuessed)


def getAvailableLetters(lettersGuessed):
    return str(list(filter(filterGuessed, string.ascii_lowercase)))


def hangman(secretWord):
    won = False
    mistakes = 0
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
    # FILL IN YOUR CODE HERE...

    print("Number of letters in the word: " + str(len(secretWord)))

    while (won != True):
        print("Total Mistakes " + str(mistakes))
        answer = input("Choose a letter")
        print(answer)
        if (secretWord.find(answer) == -1):
            print("Strike!")
            mistakes += 1
        lettersGuessed.append(answer)
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
        print(getGuessedWord(secretWord, lettersGuessed))
        if (secretWord == getGuessedWord(secretWord, lettersGuessed)):
            won = True
            print("you won!")


hangman("tact")
