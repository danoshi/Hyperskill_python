# write your code here
lines = '---------'
first_row = [" ", " ", " "]
second_row = [" ", " ", " "]
third_row = [" ", " ", " "]


def main():

    _grid_first_row(first_row)
    _grid_second_row(second_row)
    _grid_third_row(third_row)
    x = 0
    a = True
    while a:

        move = input("Enter the coordinates: ")
        new_move = move.split()
        if x == 0:
            if new_move[0] == '1':
                if new_move[1] == '1' and first_row[0].startswith(" "):
                    first_row[0] = "X"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x + 1
                    if win_X(first_row, second_row, third_row) == "x":
                        print("X wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("X wins")
                        a = False
                    else:
                        continue

                elif new_move[1] == '2' and first_row[1].startswith(" "):
                    first_row[1] = "X"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x + 1
                    if win_X(first_row, second_row, third_row) == "x":
                        print("X wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                elif new_move[1] == '3' and first_row[2].startswith(" "):
                    first_row[2] = "X"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x + 1
                    if win_X(first_row, second_row, third_row) == "x":
                        print("X wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                else:
                    print("This cell is occupied! Choose another one!")
            elif new_move[0] == '2':
                if new_move[1] == '1' and second_row[0].startswith(" "):
                    second_row[0] = "X"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x + 1
                    if win_X(first_row, second_row, third_row) == "x":
                        print("X wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                elif new_move[1] == '2' and second_row[1].startswith(" "):
                    second_row[1] = "X"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x + 1
                    if win_X(first_row, second_row, third_row) == "x":
                        print("X wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                elif new_move[1] == '3' and second_row[2].startswith(" "):
                    second_row[2] = "X"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x + 1
                    if win_X(first_row, second_row, third_row) == "x":
                        print("X wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                else:
                    print("This cell is occupied! Choose another one!")
            elif new_move[0] == '3':
                _grid_first_row(first_row)
                _grid_second_row(second_row)
                _grid_third_row(third_row)
                if new_move[1] == '1' and third_row[0].startswith(" "):
                    third_row[0] = "X"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x + 1
                    if win_X(first_row, second_row, third_row) == "x":
                        print("X wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                elif new_move[1] == '2' and third_row[1].startswith(" "):
                    third_row[1] = "X"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x + 1
                    if win_X(first_row, second_row, third_row) == "x":
                        print("X wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                elif new_move[1] == '3' and third_row[2].startswith(" "):
                    third_row[2] = "X"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x + 1
                    if win_X(first_row, second_row, third_row) == "x":
                        print("X wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                else:
                    print("This cell is occupied! Choose another one!")
        elif x == 1:
            if new_move[0] == '1':
                if new_move[1] == '1' and first_row[0].startswith(" "):
                    first_row[0] = "O"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x - 1
                    if win_O(first_row, second_row, third_row) == "o":
                        print("O wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                elif new_move[1] == '2' and first_row[1].startswith(" "):
                    first_row[1] = "O"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x - 1
                    if win_O(first_row, second_row, third_row) == "O":
                        print("O wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                elif new_move[1] == '3' and first_row[2].startswith(" "):
                    first_row[2] = "O"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x - 1
                    if win_O(first_row, second_row, third_row) == "O":
                        print("O wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                else:
                    print("This cell is occupied! Choose another one!")
            elif new_move[0] == '2':
                if new_move[1] == '1' and second_row[0].startswith(" "):
                    second_row[0] = "O"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x - 1
                    if win_O(first_row, second_row, third_row) == "o":
                        print("O wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                elif new_move[1] == '2' and second_row[1].startswith(" "):
                    second_row[1] = "O"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x - 1
                    if win_O(first_row, second_row, third_row) == "o":
                        print("O wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                elif new_move[1] == '3' and second_row[2].startswith(" "):
                    second_row[2] = "O"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x - 1
                    if win_O(first_row, second_row, third_row) == "o":
                        print("O wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                else:
                    print("This cell is occupied! Choose another one!")
            elif new_move[0] == '3':
                if new_move[1] == '1' and third_row[0].startswith(" "):
                    third_row[0] = "O"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x - 1
                    if win_O(first_row, second_row, third_row) == "o":
                        print("O wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                elif new_move[1] == '2' and third_row[1].startswith(" "):
                    third_row[1] = "O"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x - 1
                    if win_O(first_row, second_row, third_row) == "o":
                        print("O wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue

                elif new_move[1] == '3' and third_row[2].startswith(" "):
                    third_row[2] = "O"
                    _grid_first_row(first_row)
                    _grid_second_row(second_row)
                    _grid_third_row(third_row)
                    x = x - 1
                    if win_O(first_row, second_row, third_row) == "o":
                        print("O wins")
                        a = False
                    elif draw(first_row, second_row, third_row) == "draw":
                        print("Draw")
                        a = False
                    else:
                        continue
                else:
                    print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")


def _grid_first_row(first_row):
    print(lines)
    print('| ' + first_row[0] + ' ' + first_row[1] + ' ' + first_row[2] + ' |')


def _grid_second_row(second_row):
    print('| ' + second_row[0] + ' ' + second_row[1] + ' ' + second_row[2] + ' |')


def _grid_third_row(third_row):
    print('| ' + third_row[0] + ' ' + third_row[1] + ' ' + third_row[2] + ' |')
    print(lines)


def win_X(row_1, row_2, row_3):
    if row_1.count("X") == 3 or row_2.count("X") == 3 or row_3.count("X") == 3:
        return "x"
    elif row_1[0] == "X" and row_2[0] == "X" and row_3[0] == "X":
        return "x"
    elif row_1[1] == "X" and row_2[1] == "X" and row_3[1] == "X":
        return "x"
    elif row_1[2] == "X" and row_2[2] == "X" and row_3[2] == "X":
        return "x"
    elif row_1[0] == "X" and row_2[1] == "X" and row_3[2] == "X":
        return "x"
    elif row_1[2] == "X" and row_2[1] == "X" and row_3[0] == "X":
        return "x"


def win_O(row_1, row_2, row_3):
    if row_1.count("O") == 3 or row_2.count("O") == 3 or row_3.count("O") == 3:
        return "o"
    elif row_1[0] == "O" and row_2[0] == "O" and row_3[0] == "O":
        return "o"
    elif row_1[1] == "O" and row_2[1] == "O" and row_3[1] == "O":
        return "o"
    elif row_1[2] == "O" and row_2[2] == "O" and row_3[2] == "O":
        return "o"
    elif row_1[0] == "O" and row_2[1] == "O" and row_3[2] == "O":
        return "o"
    elif row_1[2] == "O" and row_2[1] == "O" and row_3[0] == "O":
        return "o"


def draw(row_1, row_2, row_3):
    if " " not in row_1[0:3] and " " not in row_2[0:3] and " " not in row_3[0:3]:
        return "draw"


def impossible(row_1, row_2, row_3):
    row_1_x = row_1.count("X")
    row_2_x = row_2.count("X")
    row_3_x = row_3.count("X")

    row_1_o = row_1.count("O")
    row_2_o = row_2.count("O")
    row_3_o = row_3.count("O")

    sum_x = row_1_x + row_2_x + row_3_x
    sum_o = row_1_o + row_2_o + row_3_o
    erg_x = sum_x - sum_o
    erg_o = sum_o - sum_x
    if erg_x > 1:
        return "Impossible"
    elif erg_o > 1:
        return "Impossible"


def empty(row_1, row_2, row_3):
    row_1_ = row_1.count("_")
    row_2_ = row_2.count("_")
    row_3_ = row_3.count("_")

    sum_ = row_1_ + row_2_ + row_3_
    return sum_


main()
