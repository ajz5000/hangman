import random

words = ["cute bean", "hungry", "cuddlebutt"] 

ind = random.randint(0,(len(words)-1))


def hangman(word):
    wrong = 0
    stages = ["",
              "_______       ",
              "|      |      ",
              "|      |      ",
              "|      O      ",
              "|     /|\     ",
              "|     / \     ",
              "|             ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!!!!!!!")

    while wrong < len(stages)-1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        #print(stages[0:e])

        if "_" not in board:
            print("You win, dummy")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Ya lost. It was {}.".format(word))



hangman(words[ind])
