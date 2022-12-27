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

def check_board(board, symbol):
   return board[0] == board[1] == board [2] == symbol or board[3] == board[4] == board [5] == symbol or \
      board[6] == board[7] == board [8] == symbol or board[0] == board[3] == board [6] == symbol or \
         board[1] == board[4] == board [7] == symbol or board[2] == board[5] == board [8] == symbol or \
            board[0] == board[4] == board [8] == symbol or board[2] == board[4] == board [6] == symbol 
            
def user_choice(player):
   # Could add a vector of possible values as game progresses
   position = 'wrong'
   within_range = False
   while position.isdigit() == False or within_range == False:
      position = input(f'{player} choose a number between 0 and 8: ')
      
      if position.isdigit() == False: 
         print('Sorry, but you did not enter a valid positon for the board.\nPlease try again.')
      
      else:
         if int(position) in range(0,9): within_range = True
         else: 
            within_range = False
            print('Sorry, but you did not enter a valid positon for the board.\nPlease try again.')
   
   return int(position)

def symbol_choice():
   symbol = 'wrong'
   players = {}
   while symbol not in ['x','o']:
      symbol = input('Player 1, pick x or o: ')
      if symbol not in ['x','o']:
         print("Sorry, but you did not enter a valid symbol to play with.\nPlease make sure to choose x or o.")
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
   gameover = False
   available_options = list(range(0,9))
   while gameover == False:
      position1 = 'wrong'
      position2 = 'wrong'
      while position1 not in available_options:
         position1 = user_choice(players_keys[0])
         print('Choose an available option')
      available_options.pop(available_options.index(position1))
      board[position1] = players['player1']
      display_game(board)
      if check_board(board, players['player1']):
         gameover = True
         print(f'{players_keys[0]} is the tic tac toe master!')
         continue
      while position2 not in available_options:
         position2 = user_choice(players_keys[1])
         print('Choose an available option')
      available_options.pop(available_options.index(position2))
      board[position2] = players['player2']
      clear()
      display_game(board)
      if check_board(board, players['player2']):
         gameover = True
         print(f'{players_keys[1]} is the tic tac toe master!')
         continue

      
   
def gameon_choice():
   choice = 'wrong'
   while choice not in ['y', 'n']:
      choice = input('Would you like to keep playing? y or n.\n')
      if choice not in ['y', 'n']:
         clear()
         print("Sorry, but you did not enter a valid answer.\nPlease make sure to choose y(es) or n(o).")
      if choice == 'y': return True
      else: return False



# Game logic altogether
game_on = True
while game_on:
   clear()
   gameon()
   game_on = gameon_choice()
print('Thanks for playing.')
