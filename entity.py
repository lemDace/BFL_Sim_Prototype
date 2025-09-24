import euclid3
from euclid3 import Vector2

class Player:
    
    def __init__(self, name:str,team:str,speed:float, position:Vector2):
        self.name = name
        self.team = team
        self.speed = speed
        self.position = position



class Team:

    def __init__(self, name:str):
        self.name = name




class Ball:

    def __init__(self, position:Vector2):
        self.position = position        


