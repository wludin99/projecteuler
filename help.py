def solution(B):
    # write your code in Python 3.6
    N = len(B)
    # locate Jafar's pawn
    for i in range(N):
        stop = False
        for j in range(N):
            if B[i][j] == 'O':
                stop = True
            break
        if stop == True:
            break
    ##check if move will hit end of board
    if i-2 < 0:
        return 0

    # check if left move is possible and update board
    if j-2 >= 0 :
        if B[i-1][j-1] == 'X' and B[i-2][j-2] == '.':
            row = list(B[i-2])
            row[j-2] = 'O'
            B[i-2] = ''.join(row)
            left = 1 + solution(B)
        else:
            left = 0
    else:
        left = 0
    # check if right move is possible and update board
    if j+2 <=  N-1:
        if B[i-1][j+1] == 'X' and B[i-2][j+2] == '.':
            row = list(B[i-2])
            row[j+2] = 'O'
            B[i-2] = ''.join(row)
            print(B)
            right = 1 + solution(B)
        else:
            right = 0
    else:
        right = 0

    return max(left,right)

B = ["..X...","......","....X.",".X....","..X.X.","...O.."]
print(solution(B))
