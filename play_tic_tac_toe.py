import random
import sys

def main():
	"""The main function. Takes user input (whether x/o, and move firsy y/n. Calls start_game()) """
	print "Welcome to Tic Tac Toe 1.0"

	user_sign = raw_input("Choose x or o. x/o: ").upper()
	while user_sign != 'X' and user_sign != 'O':
		print "Invalid input. Please read carefully"
		user_sign = raw_input("Choose x or o. x/o: ").upper()

	if user_sign == 'X':
		computer_sign = 'O'
	else:
		computer_sign = 'X'

	first_move_choice = raw_input("Would you like to move first? y/n: ").upper()
	while first_move_choice != 'Y' and first_move_choice != 'N':
		print "Invalid input. Please read carefully"
		first_move_choice = raw_input("Would you like to move first? y/n: ").upper()

	if first_move_choice == 'Y':
		computer_moves_first = False
	else:
		computer_moves_first = True

	start_game(user_sign, computer_sign, computer_moves_first)

def start_game(user_sign, computer_sign, computer_moves_first):
	""" Runs the main game loop. Calls helper functions to draw the board, check for win/draw, makes moves etc
	Maintains a list of unfilled tiles to help the computer make a random move."""
	tile_list = [i for i in range(1,10)]
	sign_to_player_map = {user_sign: "User", computer_sign: "Computer"}
	unfilled_tile_list = [i for i in range(1, 10)]
	#These are the only possible winning patterns in tic-tac-toe
	winning_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

	draw_board(tile_list)

	while True:
		if computer_moves_first:
			make_computer_move((tile_list, computer_sign, unfilled_tile_list))
			print "Computer move:"
		else:
			accept_user_move((tile_list, user_sign, unfilled_tile_list))
			print "Your move:"



		draw_board(tile_list)

		check_for_win_or_draw((tile_list, computer_sign, user_sign, winning_patterns, unfilled_tile_list))
		
		if computer_moves_first:
			accept_user_move((tile_list, user_sign, unfilled_tile_list))
			print "Your move:"
		else:
			make_computer_move((tile_list, computer_sign, unfilled_tile_list))
			print "Computer move:"

		draw_board(tile_list)

		check_for_win_or_draw((tile_list, computer_sign, user_sign, winning_patterns, unfilled_tile_list))


def draw_board(tile_list):
	"""Responsible for drawing the board. Takes in the tile_list and renders it as a board"""
	print
	print "*********"
	for tile_index, tile_value in enumerate(tile_list):
		print tile_value, " ",
		if tile_index == 2 or tile_index == 5 or tile_index == 8:
			print
	print "*********"
	print

def accept_user_move(arg_tuple):
	"""Accepts valid user input, and makes corresponding move."""
	tile_list = arg_tuple[0]
	user_sign = arg_tuple[1]
	unfilled_tile_list = arg_tuple[2]
	tile_index = int(raw_input("Square number? "))

	while tile_list[tile_index - 1] == 'X' or tile_list[tile_index - 1] == 'O':
		tile_index = int(raw_input("Invalid square!"))

	tile_list[tile_index - 1] = user_sign
	unfilled_tile_list.remove(tile_index)

def make_computer_move(arg_tuple):
	"""Currently this is the naive version. The computer just makes a random selection from the unfilled squares"""
	tile_list = arg_tuple[0]
	computer_sign = arg_tuple[1]
	unfilled_tile_list = arg_tuple[2]
	tile_index = random.choice(unfilled_tile_list)

	tile_list[tile_index - 1] = computer_sign
	unfilled_tile_list.remove(tile_index)

def check_for_win_or_draw(arg_tuple):
	"""Checks the board for a win/draw. Prints appropriate messages"""
	tile_list = arg_tuple[0]
	computer_sign = arg_tuple[1]
	user_sign = arg_tuple[2]
	winning_patterns = arg_tuple[3]
	unfilled_tile_list = arg_tuple[4]

	if not unfilled_tile_list:
		print "Its a draw!"
		sys.exit(0)

	user_win_tuple = (user_sign, user_sign, user_sign)
	computer_win_tuple = (computer_sign, computer_sign, computer_sign)

	for pattern in winning_patterns:
		pattern_tuple = (tile_list[pattern[0]], tile_list[pattern[1]], tile_list[pattern[2]])
		if pattern_tuple == user_win_tuple:
			print "User wins!"
			sys.exit(0)
		elif pattern_tuple == computer_win_tuple:
			print "Computer wins!"
			sys.exit(0)

if __name__ == "__main__":
	main()