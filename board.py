import random
from Matrix import Matrix
from items import ItemType
import constants

class Board(Matrix):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.rows = rows
        self.cols = cols
        self.total_coins = 0

    def load(self):
        element_weights = {
            ItemType.COIN: 2,  # 20% probability
            ItemType.EMPTY: 4,  # 40% probability
            ItemType.WALL: 2,  # 20% probability
            ItemType.GOLD_COIN: 1,  # 10% probability
            ItemType.DOUBLE_COINS: 1  # 10% probability
        }
        
        weighted_elements = [element for element, weight in element_weights.items() for _ in range(weight)]
        self.matrix = []
        coins = 0

        for i in range(self.rows):
            row = []
            
            for _ in range(self.cols):
                element = random.choice(weighted_elements)
                row.append(element)
                if element.is_special_symbol():
                        weighted_elements.remove(element)
                if element.is_coin():
                    coins += 1
                        
            self.matrix.append(row)
            
        if self.matrix[0][0].is_coin():
            coins -= 1
        if self.matrix[self.rows - 1][self.cols - 1].is_coin():
            coins -= 1
            
        # Place players
        self.matrix[0][0] = ItemType.PLAYER1
        self.matrix[self.rows - 1][self.cols - 1] = ItemType.PLAYER2

        # Retry if insufficient coins
        if coins < constants.MIN_ALLOWED_COINS:
            return self.load()
        self.total_coins = coins
        return self.matrix
    
    def get_coins(self):
        return self.total_coins

    def reduce_coins(self):
        self.total_coins -= 1