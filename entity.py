from euclid3 import Vector2
import random

class Ball:
    position: Vector2
    velocity: Vector2
    #carrier: 'Player'

    def __init__(self, position: Vector2, velocity:Vector2=Vector2(0,0)) -> None:
        self.position = position
        self.velocity = velocity
        self.carrier = None

    #updates position of ball based on velocity (notes: things like weather can effect its slowdown speed
    def update(self) -> None:
        self.position = self.position + self.velocity

    #applies velocity to the ball
    def kick(self, direction: Vector2, power: float):
        new_pos = (self.position + direction) * power
        self.position = new_pos
        


    #ball is no longer held. Apply when ball is kicked
    def drop(self) -> None:
        self.carrier = None

class AttributeGroup:
    def __init__(self, name: str, attributes: dict):
        self.name = name
        self.attributes = attributes

class Status:
    def __init__(self, name: str, duration: int, effects: dict):
        self.name = name
        self.duration = duration
        self.effects = effects

    def tick(self):
        self.duration -=1
        return self.duration > 0 # return true if still active

class Player:
    name: str
    position: Vector2
    speed: float
    kick_strength: float
    stamina: float
    has_ball: bool

    def __init__(self, name: str, position: Vector2, speed: float = 1.0, kickStrength : float = 2.0, stamina: float = 10.0):
        self.name = name
        self.position = position
        self.speed = speed
        self.kick_strength = kickStrength
        self.stamina = stamina
        self.has_ball = False
        self.attributes = {
            "physical": AttributeGroup("physical", {"speed":5, "stamina": 10}),
            "technical": AttributeGroup("technical", {"accuracy": 6})

        }
        self.statuses = []

    def get_effective_attr(self, group:str, attr:str):
        base = self.attributes[group].attributes[attr]
        modifier = 1.0
        return base * modifier

    def add_status(self, status: Status):
        self.statuses.append(status)

    
    def tick_statuses(self, status: Status):
        pass


    #moves in direction given, scaled by speed
    def move(self, direction: Vector2):
        pass

    def distance_to_ball(self, ball: Ball):
        return (ball.position - self.position).magnitude()

    #moves in the direction of the given target, scaled by speed
    def move_towards_target(self, target: Vector2):
        direction = target - self.position
        direction = direction.normalized()
        movement = direction * self.speed
        self.position = self.position + movement



    #picks up a ball
    def pick_up_ball(self, ball: Ball):
        self.has_ball = True


    #kicks the ball if they have it in the direction given, scaled by kick_strength
    def kick_ball(self, ball: Ball, direction: Vector2, power: float):
        ball.kick(direction.normalize(),power)
        self.has_ball = False
        


class Team:
    name: str
    players: list[Player]
    score: int

    def __init__(self, name:str,score:int=0) -> None:
        self.name = name
        self.score = score
        self.players = []

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def get_active_players(self) -> list[Player]:
        return self.players
    

class Field:
    location: str
    length: float
    width: float

    def __init__(self, location:str, length:float=1000, width:float=500) -> None:
        self.location = location
        self.length = length
        self.width = width
        


