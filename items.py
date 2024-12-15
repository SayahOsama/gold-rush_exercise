from enum import Enum
from typing import Optional

class ItemType(Enum):
    COIN = ("coin", 10)
    GOLD_COIN = ("gold_coin", 30)
    DOUBLE_COINS = ("double_coins", 0)
    WALL = ("wall", 0)
    EMPTY = (".", 0)
    PLAYER1 = ("player1", 0)
    PLAYER2 = ("player2", 0)

    def __init__(self, symbol: str, points: int):
        self.symbol = symbol
        self.points = points
        
    def get_symbol(self) -> Optional[str]:
        symbol_map = {
            "coin": "$",
            "gold_coin": "G$",
            "double_coins": "D$",
            "wall": "W",
            ".": ".",
            "player1": "player1",
            "player2": "player2"
        }
        return symbol_map.get(self.symbol)

    def get_points(self) -> Optional[str]:
        points_map = {
            "coin": 10,
            "gold_coin": 30,
            "double_coins": 0,
            "wall": 0,
            ".": 0,
            "player1": 0,
            "player2": 0
        }
        return points_map.get(self.symbol)
    
    def is_coin(self) -> bool:
        return self.symbol in {"coin", "gold_coin"}

    def is_special_symbol(self) -> bool:
        return self.symbol in {"double_coins", "gold_coin"}
    
    def is_blocking_type(self) -> bool:
        return self.symbol in {"wall", "player1", "player2"}