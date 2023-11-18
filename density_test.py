import random
import time

field = [[random.randint(0, 100) for i in range(10)] for j in range(10)]


def is_possible(moves, i, j):
    new_moves = []
    if i != len(field)-1:
        new_moves.append(moves[0])
    if i != 0:
        new_moves.append(moves[1])
    if j != len(field)-1:
        new_moves.append(moves[2])
    if j != 0:
        new_moves.append(moves[3])
    
    return new_moves
    


def transfer():
    for i in range(len(field)):
        for j in range(len(field)):
            possibles = is_possible([(1, 0), (-1, 0), (0, 1), (0, -1)], i, j)
            lowest = field[i][j]
            l_index = [i, j]
            for k, l in possibles:
                #print(k, l)
                if field[i+k][j+l] < lowest:
                    lowest = field[i+k][j+l]
                    l_index = [i+k, j+l]
            field[i][j] -= 1
            field[l_index[0]][l_index[1]] += 1


for i in range(50):
    for j in field:
        print(j)
    print("\n")
    transfer()
    time.sleep(0.5)