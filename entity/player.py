from euclid3 import Vector2
from typing import Tuple
from entity import Ball
from attributes import Attributes,AttributeGroup
from effects import Status


# Defines the Player entity
# Each palyer has indentifying ifo, a position, and an Attributes object

class Player:
    id: int
    name: str
    age: int
    started_playing: int
    position_played: str
    position: Vector2


    def __init__(self, id: int, name: str, age: int, started_playing: int, 
                 positionPlayed: str, attributes: dict):
        #Creates new palyer instance
        # 'attributes' is expected to be a dictionary loaded from json
        self.id = id
        self.name = name
        self.position_played = positionPlayed
        self.age = age
        self.started_playing = started_playing
        self.attributes = Attributes.from_dict(attributes)


        #self.statuses = []

    def get_attribute(self, name):
        # Convenience wrapper around Attributes.get
        return self.attributes.get(name)

    def __repr__(self):
        # Developer-friendly summary of a player (name + attributes)
        #return f"<Player {self.name}: {self.attributes.as_dict()}>" 
        return f"<Player {self.name} ({self.position}), age={self.age}>"       

    def as_dict(self):
        #Convert back to a JSON-friendly dictionary, e.g. for saving updated player data.
    
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "started_playing": self.started_playing,
            "position_played": self.positionPlayed,
            "attributes": self.attributes.as_dict()
        }

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
        