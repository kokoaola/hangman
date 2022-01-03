import random

def hangman(word):
    wrong = 0
    stages = ["",
              "______________   ",
              "|                ",  
              "|       |        ",
              "|       O        ",
              "|      /|\       ",
              "|      / \       ",
              "|                "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        char = input("１文字を予測してね")
        if char in rletters:
            cind = rletters.index(char)
            #答えの中で打った文字が最初に出てくる位置がcindに入る
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}".format(word))

tango = ['koala', 'apple', 'cat', 'dog', 'panda', 'tree', 'hot', 'pen', 'cup', 'eye']
x = random.randint(0,10)
hangman(tango[x])




    
