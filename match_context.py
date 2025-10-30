# match_context.py
from typing import List
from entity import Ball

class MatchContext:
    def __init__(self, ball: Ball, players: List, field_bounds=None, clock=None):
        self.ball = ball
        self.players = players
        self.field_bounds = field_bounds
        self.clock = clock

    def teammates_of(self, player):
        return [p for p in self.players if p.team == player.team and p is not player]

    def opponents_of(self, player):
        return [p for p in self.players if p.team != player.team]

    def nearest_opponent(self, player):
        opponents = self.opponents_of(player)
        if not opponents:
            return None
        return min(opponents, key=lambda p: p.position.distance(player.position))