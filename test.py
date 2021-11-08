from moonday.boards import Board
from moonday.columns import Column
from dotenv import dotenv_values

config = dotenv_values(".env") 

# monday = Board(config['MONDAY_API_KEY'])

# print(monday.get_boards())
# print(monday.get_board_id("BIG TEST"))
# print(monday.get_board_data("1877148777"))
# print(monday.get_board_permissions("1877148777"))
# print(monday.get_board_updates("1877148777"))
# print(monday.get_board_subscribers("1877148777"))
# print(monday.get_board_workspace("1877148777"))

# monday.create_board("Hello World", monday.PUBLIC)
# print(monday.duplicate_board("1877148777", monday.WITH_PULSES, ("PIzza BoArD",monday.FALSE)))

columns = Column(config['MONDAY_API_KEY'], "1877148777")

print(columns.get_columns())
print(columns.get_columns_settings())
# columns.create_column("Test", columns.HOUR)


