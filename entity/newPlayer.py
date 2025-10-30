# player.py
from euclid3 import Vector2
from entity import PhysicalEntity, Ball
from attributes import Attributes
from effects import Status
from match_context import MatchContext


class PlayerV2(PhysicalEntity):
    def __init__(self, id, name, age, team, position_played, attributes, position=(0, 0)):
        super().__init__(id=id, position=Vector2(position))
        self.name = name
        self.age = age
        self.team = team
        self.position_played = position_played

        self.attributes = Attributes.from_dict(attributes)
        self.statuses: list[Status] = []
        self.has_ball = False

        # --- AI placeholders ---
        self.state = "idle"          # e.g. 'idle', 'chasing', 'holding', etc.
        self.intent = None           # the immediate action/goal
        self.target = None           # a position or object to act upon

    # ---------------- Core update loop ---------------- #

    def update(self, dt: float, context: MatchContext):
        """Called every frame/tick by the simulation."""
        self.update_statuses(dt)
        self.decide(context)
        self.act(dt)

    # ---------------- Decision layer ---------------- #

    def decide(self, context: MatchContext):
        """
        Decide what to do next.
        Later this can be replaced by: self.brain.decide(context)
        """
        ball = context.ball

        # Example basic logic:
        if self.has_ball:
            self.state = "holding"
            self.intent = "kick"  # placeholder
        elif self.is_close_to(ball, radius=10):
            self.state = "picking_up"
            self.intent = "pickup"
        else:
            self.state = "chasing"
            self.intent = "move_to"
            self.target = ball.position

    # ---------------- Action execution ---------------- #

    def act(self, dt: float):
        """Perform the action decided upon."""
        if self.intent == "move_to" and self.target is not None:
            self.move_towards(self.target, dt)
        elif self.intent == "pickup":
            self.pick_up_ball()
        elif self.intent == "kick":
            self.kick_ball()  # direction & logic TBD

    # ---------------- Movement & Interaction ---------------- #

    def move_towards(self, target: Vector2, dt: float):
        direction = (target - self.position).normalized()
        speed = self.attributes.get("physical", "speed")
        self.velocity = direction * speed
        self.position += self.velocity * dt

    def is_close_to(self, other_entity, radius: float) -> bool:
        return (self.position - other_entity.position).magnitude() <= radius

    def pick_up_ball(self):
        self.has_ball = True

    def kick_ball(self):
        # Placeholder: could use self.target or context later
        pass

    def update_statuses(self, dt):
        for status in self.statuses:
            status.tick(dt)