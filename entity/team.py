from typing import Tuple
from entity.player import Player

class Team:
    name: str
    players: list[Player]
    score: int
    color: Tuple[int, int, int]

    def __init__(self, name:str,color: Tuple[int,int,int],score:int=0) -> None:
        self.name = name
        self.score = score
        self.color = color
        self.players = []

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def get_active_players(self) -> list[Player]:
        return self.players
    