from entity import PhysicalEntity
from euclid3 import Vector2
from attributes import Attributes,AttributeGroup

#newPlayer class to eventually replace the Player class.
#this class will inherit from physicalEntity()

class NewPlayer(PhysicalEntity):
    
    #new class def

    team: str
    started_playing: int
    position_played: str
    has_ball: bool

    def __init__(self, id: int, name: str, age: int, started_playing: int, 
                 team:str, positionPlayed: str, attributes: dict):
        super().__init__(id=id, name=name,**kwargs)
        
        self.team = team
        self.position_played = positionPlayed
        self.started_playing = started_playing
        self.age = age
        self.has_ball = False
        self.attributes = Attributes.from_dict(attributes)         # 'attributes' is expected to be a dictionary loaded from json

    def get_attribute(self, name):
        # Convenience wrapper around Attributes.get
        return self.attributes.get(name)

    def __repr__(self):
        # Developer-friendly summary of a player (name + attributes)
        #return f"<Player {self.name}: {self.attributes.as_dict()}>" 
        return f"<Player {self.name} ({self.team}), age={self.age}>"       

    def as_dict(self):
        #Convert back to a JSON-friendly dictionary, e.g. for saving updated player data.
    
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "started_playing": self.started_playing,
            "position_played": self.positionPlayed,
            "team": self.team,
            "attributes": self.attributes.as_dict()
        }

    def get_effective_attr(self, group:str, attr:str):
        base = self.attributes[group].attributes[attr]
        modifier = 1.0
        return base * modifier       
    
        #moves in direction given, scaled by speed
    def move(self, direction: Vector2):
        pass

    def distance_to_ball(self, ball: Ball):
        return (ball.position - self.position).magnitude()

    #moves in the direction of the given target, scaled by speed
    def move_towards_target(self, target: Vector2):
        direction = target - self.position
        direction = direction.normalized()
        movement = direction * (self.attributes.get('physical','speed')/35)
        self.position = self.position + movement



    #picks up a ball
    def pick_up_ball(self, ball: Ball):
        self.has_ball = True


    #kicks the ball if they have it in the direction given, scaled by kick_strength
    def kick_ball(self, ball: Ball, direction: Vector2):
        ball.kick(direction,(self.attributes.get('physical','strength'))/5)
        self.has_ball = False
        