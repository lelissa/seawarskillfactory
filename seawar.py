from random import randint

board = []

for x in range(6):
    board.append(["O"] * 6)


def print_board(board):
    for row in board:
        print((" ").join(row))  # создаётся игровое поле


def random_row(board):
    return randint(0, len(board) - 1)  # фунцкия загадывания корабля по строке


def random_col(board):
    return randint(0, len(board[0]) - 1)  # фунцкия загадывания корабля по столбцу


print("Начнем игру в Морской бой!")
print_board(board)

ship_row = random_row(board)  # загадываем корабль по строке
ship_col = random_col(board)  # загадываем корабль по столбцу

for turn in range(10):  # 10 попыток
    print("Ход: ", turn)
    guess_row = int(input("Строка 0-5:"))  # ввод строки
    guess_col = int(input("Столбец 0-5:"))  # ввод столбца

    if guess_row == ship_row and guess_col == ship_col:  # если попал
        print("Поздравляю, ты потопил мой корабль!")
        break
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):  # если мимо игрового поля
            print("Oops, эти координаты не в нашем океане.")
        elif (board[guess_row][guess_col] == "X"):  # если назвал повторно координаты
            print("Эти координаты вы уже называли.")
        else:
            print("Мимо!")
            board[guess_row][guess_col] = "X"  # если не попал по кораблю ставлю Х
    if turn == 9:
        print("Игра окончена! Я уплываю в закат!")  # конец игры
    # turn =+ 1
    print_board(board)