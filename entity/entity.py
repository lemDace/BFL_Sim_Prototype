#entity.py
from euclid3 import Vector2
import uuid


class Entity:
    """
    Base class for all simulation entities (physical or abstract).
    Defines identity, lifecycle hooks, and shared utilities.
    """
    def __init__(self, name=None,active=True):
        self.id = uuid.uuid4()
        self.name = name or self.__class__.__name__
        self.active = active
        self.engine = None

        self.on_spawn()


    # ------------------------------------------------------------------
    # Core lifecycle
    # ------------------------------------------------------------------
   def on_spawn(self):
        """Called when the entity is created and added to the world."""
        pass

    def pre_update(self, dt):
        """Called before the main update logic. Useful for sensing/preparing state."""
        pass

    def on_update(self, dt):
        """Core update logic (AI, simulation, etc.)."""
        pass

    def post_update(self, dt):
        """Called after main update logic, often for cleanup or event triggers."""
        pass

    def on_remove(self):
        """Called when entity is removed from the simulation."""
        pass


    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------
    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} active={self.active}>"


class PhysicalEntity(Entity):
       
    """
    Extends Entity with spatial and physical properties.
    Used by all in-world entities with a position and velocity.
    """

    def __init__(self, position=None, velocity=None, orientation=0.0, radius=1.0, **kwargs):
        super().__init__(**kwargs)
        self.position = position or Vector2(0.0, 0.0)
        self.velocity = velocity or Vector2(0.0, 0.0)
        self.orientation = orientation
        self.radius = radius

    # ------------------------------------------------------------------
    # Physics helpers
    # ------------------------------------------------------------------
    def move(self, dt):
        """Updates position based on velocity."""
        self.position += self.velocity * dt

    def distance_to(self, other):
        """Returns distance to another PhysicalEntity or Vector2."""
        if isinstance(other, PhysicalEntity):
            return (self.position - other.position).magnitude()
        elif isinstance(other, Vector2):
            return (self.position - other).magnitude()
        else:
            raise TypeError(f"Cannot measure distance to type: {type(other)}")

    def direction_to(self, other):
        """Returns normalized direction vector toward another PhysicalEntity or Vector2."""
        if isinstance(other, PhysicalEntity):
            other_pos = other.position
        elif isinstance(other, Vector2):
            other_pos = other
        else:
            raise TypeError(f"Cannot compute direction to type: {type(other)}")

        direction = other_pos - self.position
        return direction.normalized() if direction.magnitude() != 0 else Vector2(0.0, 0.0)

    # ------------------------------------------------------------------
    # Overridden lifecycle hook
    # ------------------------------------------------------------------
    def on_update(self, dt):
        """Default behavior: move based on velocity."""
        self.move(dt)

    def __repr__(self):
        pos = f"({self.position.x:.2f}, {self.position.y:.2f})"
        return f"<{self.__class__.__name__} id={self.id} pos={pos} active={self.active}>"        