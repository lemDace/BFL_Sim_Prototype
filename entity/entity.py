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


