board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
turn = 0
player = 0
count_all = 0

while turn <= 9:
    turn += 1
    print("Možnosti:\n[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]")
    print("Hrací plocha:\n" + str(board[0]) + "\n" + str(board[1]) + "\n" + str(board[2]))

    if turn % 2 != 0:
        player = 1
        print("Hraje hráč číslo 1.")
        player_input = input("Vyber číslo 1-9. ")
        player_input = int(player_input)

    if turn % 2 == 0:
        player = 2
        print("Hraje hráč číslo 2.")
        player_input = int(input("Vyber číslo 1-9. "))

    if player_input == 1:
        board[0][0] = player
    elif player_input == 2:
        board[0][1] = player
    elif player_input == 3:
        board[0][2] = player
    elif player_input == 4:
        board[1][0] = player
    elif player_input == 5:
        board[1][1] = player
    elif player_input == 6:
        board[1][2] = player
    elif player_input == 7:
        board[2][0] = player
    elif player_input == 8:
        board[2][1] = player
    elif player_input == 9:
        board[2][2] = player
    else:
        print("Jsi čurák.")

    if board[0][0] == board[0][1] == board[0][2] == player:
        print("Vyhrál hráč číslo " + str(player))
        break
    elif board[1][0] == board[1][1] == board[1][2] == player:
        print("Vyhrál hráč číslo " + str(player))
        break
    elif board[2][0] == board[2][1] == board[2][2] == player:
        print("Vyhrál hráč číslo " + str(player))
        break
    elif board[0][0] == board[1][0] == board[2][0] == player:
        print("Vyhrál hráč číslo " + str(player))
        break
    elif board[0][1] == board[1][1] == board[2][1] == player:
        print("Vyhrál hráč číslo " + str(player))
        break
    elif board[0][2] == board[1][2] == board[2][2] == player:
        print("Vyhrál hráč číslo " + str(player))
        break
    elif board[0][0] == board[1][1] == board[2][2] == player:
        print("Vyhrál hráč číslo " + str(player))
        break
    elif board[0][2] == board[1][1] == board[2][0] == player:
        print("Vyhrál hráč číslo " + str(player))
        break

else:
    print("Remíza.")
