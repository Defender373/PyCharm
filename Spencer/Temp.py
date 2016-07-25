import random


def letter_score(letter):
    scrabble_dict = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
                     'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
                     'y': 4, 'z': 10}
    return scrabble_dict[letter]


def hangman():
    print("Welcome to Hangman")
    # num_players = int(input("1 or 2 players?: "))
    # get user word
    difficulty_string = input("Type in a difficulty between 0.0 and 1.0: ")
    difficulty = float(difficulty_string)
    strikes = int(input("How many strikes before the game ends?: "))
    word = input("Type a word: ")
    # print(len(str(difficulty_string)) - 1, (difficulty*(10**(len(str(difficulty_string))-1))),
    #      10 ** (len(str(difficulty_string))-1),
    #      word)

    # generate and print initial word bank
    bank = ''
    # use difficulty to determine how many characters to initially display to the user
    digits = len(str(difficulty_string)) - 1
    d_temp = difficulty * (10 ** digits)
    for i in range(len(word)):
        rand = random.randrange(1, 10 ** digits)
        # print(rand, rand<d_temp, i)
        # display character if the random number is in our bound, display blank if not.
        if rand > d_temp:
            bank += word[i]
            # print(bank)
        else:
            bank += '_'
    print(bank)

    # start playing the game
    playing = True
    strike_list = []
    score = 0
    while playing:
        guess = input("Guess a letter: ")

        # determine if letter is in the word
        strike = True
        won = True
        temp_bank = ''
        for space, letter in zip(bank, word):
            # print(guess, letter, letter is guess)
            if letter is guess:
                temp_bank += letter
                # print(guess, temp_bank)
                score += letter_score(guess)
                # print(score)
                strike = False
            else:
                temp_bank += space
            if temp_bank[len(temp_bank) - 1] is '_':
                won = False
        bank = temp_bank
        # update strike list and determine if the game should end
        if strike:
            strike_list.append(guess)
            print("STRIKE # %d" % (int(len(strike_list))))
            if len(strike_list) >= strikes:
                playing = False
                print("GAME OVER!!!")
                replay = input("Play again? 1-Yes 2-No : ")
                if replay is '1':
                    hangman()
        # determine if you won
        if won:
            playing = False
            print("YOU WIN!, The word was %s and your score is %d" % (word, score))
            replay = input("Play again? 1-Yes 2-No : ")
            if replay is '1':
                hangman()

        if playing:
            print(bank, '\nstrikes: ' + str(strike_list), 'Score: ' + str(score))


hangman()
