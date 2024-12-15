import constants
from board import Board
from player import Player
from items import ItemType

class GoldRush:

    def __init__(self, rows, cols):
        self.board = Board(rows, cols)
        self.players = {"player1": Player("player1",(0,0)), "player2": Player("player2",(rows-1,cols-1))}
        self.winner = None

    def load_board(self):
        return self.board.load()

    def move_player(self, player_name, direction):
        player = self.players[player_name]
        curr_row, curr_col = player.get_coordinates()

        delta_row, delta_col = self._direction_to_delta(direction)
        new_row, new_col = curr_row + delta_row, curr_col + delta_col

        if not self._is_within_bounds(new_row, new_col):
            return  # Invalid move

        cell = self.board.matrix[new_row][new_col]

        if cell.is_blocking_type():
            return  # Cannot move into a wall or other player
        if cell.is_coin():
            self.board.reduce_coins()
            
        player.add_score(cell)
        
        # Update the board
        self.board.matrix[curr_row][curr_col] = ItemType.EMPTY
        self.board.matrix[new_row][new_col] = ItemType.PLAYER1 if player_name == "player1" else ItemType.PLAYER2
        player.update_coordinates(new_row,new_col)

        if player.score >= constants.WINNING_SCORE:
            self.winner = player_name


    def _direction_to_delta(self, direction):
        deltas = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        return deltas.get(direction, (0, 0))

    def _is_within_bounds(self, row, col):
        return 0 <= row < self.board.rows and 0 <= col < self.board.cols
    
    def check_if_player_has_won(self, player_name):
        return self.winner == player_name
    
    def check_if_game_is_tied(self):
        return self.board.get_coins() == 0
    
    def print(self):
        self.board.print()
