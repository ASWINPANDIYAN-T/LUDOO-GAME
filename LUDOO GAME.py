path = [(0,0),(0,1),(0,2),(1,2),(2,2),(2,1),(2,0),(1,0),(1,1)]
p1 = 0
p2 = 0

while True:

    board = [[" "," "," "],[" "," "," "],[" "," "," "]]

    r1,c1 = path[p1]
    r2,c2 = path[p2]

    if p1 == p2:
        board[r1][c1] = "P "
    else:
        board[r1][c1] = "A"
        board[r2][c2] = "B"

    print("\nBoard")
    for i in board:
        print(i)

    if p1 == 8:
        print("Player 1 Wins")
        break

    if p2 == 8:
        print("Player 2 Wins")
        break

    print("\nPlayer 1 Turn")
    d = int(input("Enter (1-6): "))
    if d == 1 or d == 2:
        p1 = p1 + d
        if p1 > 8:
            p1 = 8
    else:
        print("Chance Skipped")

    board = [[" "," "," "],[" "," "," "],[" "," "," "]]

    r1,c1 = path[p1]
    r2,c2 = path[p2]
    
    if p1 == p2:
        board[r1][c1] = "P"
    else:
        board[r1][c1] = "A"
        board[r2][c2] = "B"

    print("\nBoard")
    for i in board:
        print(i)

    if p1 == 8:
        print("Player 1 Wins")
        break

    print("\nPlayer 2 Turn")
    d = int(input("Enter (1-6): "))
    if d == 1 or d == 2:
        p2 = p2 + d
        if p2 > 8:
            p2 = 8
    else:
        print("Chance Skipped")

    if p2 == 8:
        print("Player 2 Wins")
        break
