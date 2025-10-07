from euclid3 import Vector2
#from entity.field import Field
from entity import Field


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