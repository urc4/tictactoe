import os 
#os.system('clear')
def clear():
   os.system('cls')

def start_game():
   '''
   Initializes board
   '''
   board = {}
   for position in range(0,9):
      board[position] = ''
   return board

def display_game(board):
   '''
   Display current state of board
   '''
   x_patterns = {0:'* *', 1:' * ', 2:'* *'}
   o_patterns = {0:'***', 1:'* *', 2:'***'}
   
   div = 0
   for line in range(0,9):

      for pos in range(3*div,3 + 3*div):
         if board[pos] == 'x': print(x_patterns[line%3], end='')
         elif board[pos] == 'o': print(o_patterns[line%3], end='')
         else: 
            if line%3==1:
               print(f' {pos} ', end='')
            else: print('   ',end='')
         if pos != (2 + 3*div):
            print('|', end='')
      
      print('')
      
      if line%3==2: 
         print('------------')
         div += 1

def check_board(board, choice):
   return board[0] == board[1] == board [2] == choice or board[3] == board[4] == board [5] == choice or \
      board[6] == board[7] == board [8] == choice or board[0] == board[3] == board [6] == choice or \
         board[1] == board[4] == board [7] == choice or board[2] == board[5] == board [8] == choice or \
            board[0] == board[4] == board [8] == choice or board[2] == board[4] == board [6] == choice 
            
def user_choice(player):
   # Could add a vector of possible values as game progresses
   position = 'wrong'
   within_range = False
   while position.isdigit() == False or within_range == False:
      position = input(f'{player} choose a number between 0 and 8: ')
      if position.isdigit() == False: 
         clear()
         print('Sorry, but you did not enter a valid positon for the board.\nPlease try again.')
      else:
         if int(position) in range(0,9): within_range = True
         else: within_range = False
   return int(position)

def symbol_choice():
   symbol = 'wrong'
   players = {}
   while symbol not in ['x','o']:
      symbol = input('Playuh 1, pick x or o: ')
      if symbol not in ['x','o']:
         clear()
         print("Sorry, I didn't understand. Please make sure to choose x or o.")
   if symbol == 'x':
      players['player1'] = 'x'
      players['player2'] = 'o'
   else:
      players['player1'] = 'o'
      players['player2'] = 'x'
   return players

def gameon():
   board = start_game()
   players = symbol_choice()
   display_game(board)
   players_keys = list(players.keys())
   print(players_keys)
   gameover = False
   while gameover == False:
      position1 = user_choice(players_keys[0])
      board[position1] = players['player1']
      display_game(board)
      gameover = check_board(board, players['player1'])

      position2 = user_choice(players_keys[1])
      board[position2] = players['player2']
      clear()
      display_game(board)
      gameover = check_board(board, players['player2'])

      
   
def gameon_choice():
   choice = 'wrong'
   while choice not in ['y', 'n']:
      choice = input('Would you like to keep playing? y or n.\n')
      if choice not in ['y', 'n']:
         clear()
         print("Sorry, I didn't understand. Please make sure to choose y(es) or n(o).")
      if choice == 'y': return True
      else: return False





game_on = True

while game_on:
   clear()
   gameon()
   game_on = gameon_choice()

