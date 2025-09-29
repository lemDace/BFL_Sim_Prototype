from euclid3 import Vector2
from typing import Tuple
import random


class Field:
    location: str
    length: float
    width: float

    def __init__(self, location:str, length:float=1000, width:float=500) -> None:
        self.location = location
        self.length = length
        self.width = width
        
class Ball:
    position: Vector2
    velocity: Vector2
    friction: float #how much speed is kept each update
    min_speed: float #stop the ball if slower than this
    field: Field #the field the ball is on. used to get field size and boundaries

    def __init__(self, field: Field, velocity:Vector2=Vector2(0,0)) -> None:
        self.field = field
        print(type(field), repr(field))
        self.position = Vector2(self.field.length/2,self.field.width/2)
        self.velocity = velocity
        self.friction = 0.95
        self.min_speed = 0.1

    #updates position of ball based on velocity (notes: things like weather can effect its slowdown speed
    def update(self) -> None:
        #move ball
        self.position = self.position + self.velocity #could also do self.position+= self.velocity

        #apply friction/drag
        self.velocity = self.velocity * self.friction

        if self.position.x < 0 or self.position.x > self.field.length:
            self.velocity = -self.velocity

        if self.position.y < 0 or self.position.y > self.field.width:
            self.velocity = -self.velocity

        #stop ball if going too slow
        if self.velocity.magnitude() < self.min_speed:
            self.velocity = Vector2(0,0)

    #applies velocity to the ball
    def kick(self, direction: Vector2, power: float):
        #new_pos = (self.position + direction) * power
        self.velocity = direction.normalized() * power

    def set_velocity(self, velocity: Vector2):
        self.velocity = velocity
        


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
        ball.kick(direction,power)
        self.has_ball = False
        


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
    



