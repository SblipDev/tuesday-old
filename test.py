from tuesday.boards import Board
from tuesday.groups import Group
from tuesday.columns import Column
from dotenv import dotenv_values

config = dotenv_values(".env") 

monday = Board(config['MONDAY_API_KEY'])

# print(monday.get_boards())
# print(monday.get_board_id("BIG TEST"))
# print(monday.get_board_data("1877148777"))
# print(monday.get_board_permissions("1877148777"))
# print(monday.get_board_updates("1877148777"))
# print(monday.get_board_subscribers("1877148777"))
# print(monday.get_board_workspace("1877148777"))

# monday.create_board("Hello World", monday.PUBLIC)
# print(monday.duplicate_board("1877148777", monday.WITH_PULSES, ("PIzza BoArD",monday.FALSE)))

groups = Group(config['MONDAY_API_KEY'], monday.get_board_id("BIG TEST"))
groups.create_group('haw haw')


