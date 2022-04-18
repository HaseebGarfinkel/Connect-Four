connect_four = []
end = 0
for row in range(6):
  connect_four.append(["|___|"] * 7)

def drop_piece(column, piece):
  if piece.lower() == "x" or piece.lower() == "o":
    if column in range(1, 8):
      if (connect_four[0][column - 1] == ("|___|")):
        if (connect_four[5][column - 1] == "|___|"):
          connect_four[5][column - 1] = ("|_" + piece + "_|")
        elif (connect_four[4][column - 1] == "|___|"):
          connect_four[4][column - 1] = ("|_" + piece + "_|")
        elif (connect_four[3][column - 1] == "|___|"):
          connect_four[3][column - 1] = ("|_" + piece + "_|")
        elif (connect_four[2][column - 1] == "|___|"):
          connect_four[2][column - 1] = ("|_" + piece + "_|")
        elif (connect_four[1][column - 1] == "|___|"):
          connect_four[1][column - 1] = ("|_" + piece + "_|")
        elif (connect_four[0][column - 1] == "|___|"):
          connect_four[0][column - 1] = ("|_" + piece + "_|")
      else:
        print("Column is full")
    else:
      print("Not a valid column")
  else:
    print("Not a valid piece")

def game_over(pieces):
  global end
  if ((connect_four[0][0] == ("|_" + pieces + "_|")) and (connect_four[0][1] == ("|_" + pieces + "_|")) and (
          connect_four[0][2] == ("|_" + pieces + "_|")) and (connect_four[0][3] == ("|_" + pieces + "_|")) and (
          connect_four[0][4] == ("|_" + pieces + "_|")) and (connect_four[0][5] == ("|_" + pieces + "_|")) and (
          connect_four[0][6] == ("|_" + pieces + "_|"))):
    end = 2
  else:
    for y, row in enumerate(connect_four):
      for x, item in enumerate(row):
        if item == f"|_{pieces}_|":
          if (x-1) <= 6 and (x-1) >= 0:
            if connect_four[y][x-1] == f"|_{pieces}_|":
              if (x-2) <= 6 and (x-2) >= 0:
                if connect_four[y][x-2] == f"|_{pieces}_|":
                  if (x-3) <= 6 and (x-3) >= 0:
                    if connect_four[y][x-3] == f"|_{pieces}_|":
                      end = 1
          if (y+1) <= 5 and (y+1) >= 0:
            if connect_four[y+1][x] == f"|_{pieces}_|":
              if (y+2) <= 5 and (y+2) >= 0:
                if connect_four[y+2][x] == f"|_{pieces}_|":
                  if (y+3) <= 5 and (y+3) >= 0:
                    if connect_four[y+3][x] == f"|_{pieces}_|":
                      end = 1
          if (y+1) <= 5 and (y+1) >= 0 and (x-1) <= 6 and (x-1) >= 0:
            if connect_four[y+1][x-1] == f"|_{pieces}_|":
              if (y+2) <= 5 and (y+2) >= 0 and (x-2) <= 6 and (x-2) >= 0:
                if connect_four[y+2][x-2] == f"|_{pieces}_|":
                  if (y+3) <= 5 and (y+3) >= 0 and (x-3) <= 6 and (x-3) >= 0:
                    if connect_four[y+3][x-3] == f"|_{pieces}_|":
                      end = 1



def play_game():
  global x_col, o_col
  print("""
   ____                            _     _____                
  / ___|___  _ __  _ __   ___  ___| |_  |  ___|__  _   _ _ __ 
 | |   / _ \| '_ \| '_ \ / _ \/ __| __| | |_ / _ \| | | | '__|
 | |__| (_) | | | | | | |  __/ (__| |_  |  _| (_) | |_| | |   
  \____\___/|_| |_|_| |_|\___|\___|\__| |_|  \___/ \__,_|_|   
                                                              """)
  print_board(connect_four)
  print("  1    2    3    4    5    6    7")
  columns = ["1", "2", "3", "4", "5", "6", "7"]
  while True:
    valid_x = 0
    while valid_x == 0:
      x_col = input("x's turn: Choose a column (1-7)")
      if (x_col) in columns:
        if connect_four[0][int(x_col) - 1] == "|___|":
          valid_x = 1
        else:
          print("That column is full!")
      else:
        print("Not a valid column.")
    drop_piece(int(x_col), "x")
    game_over("x")
    print_board(connect_four)
    print("  1    2    3    4    5    6    7")
    if end == 1:
      print("X wins! Game over.")
      input("Press enter to exit...")
      exit()
    elif end == 2:
      print("Tie. Game over.")
      input("Press enter to exit...")
      exit()
    valid_o = 0
    while valid_o == 0:
      o_col = input("o's turn: Choose a column (1-7)")
      if o_col in columns:
        if connect_four[0][int(o_col) - 1] == "|___|":
          valid_o = 1
        else:
          print("That column is full!")
      else:
        print("Not a valid column.")
    drop_piece(int(o_col), "o")
    game_over("o")
    print_board(connect_four)
    print("  1    2    3    4    5    6    7")
    if end == 1:
      print("O wins! Game over.")
      input("Press enter to exit...")
      exit()
    elif end == 2:
      print("Tie. Game over.")
      input("Press enter to exit...")
      exit()

def print_board(board):
  for row in board:
    print("".join(row))



play_game()
