from items import ItemType
from constants import DOUBLE_COINS_ROUNDS
class Player:
    def __init__(self, name, coordinates):
        self.name = name
        self.score = 0
        self.double_coins_rounds = 0
        self.coordinates = coordinates
        
    def add_score(self, cell):
        if cell == ItemType.DOUBLE_COINS:
            self.activate_double_coins(DOUBLE_COINS_ROUNDS)
            return
        
        points = cell.get_points()
        if self.double_coins_rounds > 0:
            points *= 2
            self.double_coins_rounds -= 1
        self.score += points

    def activate_double_coins(self, rounds):
        self.double_coins_rounds = rounds
    
    def update_coordinates(self,row,col):
        self.coordinates = (row,col)
    
    def get_coordinates(self):
        return self.coordinates
