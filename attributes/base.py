

class AttributeGroup:
    def __init__(self, **attributes):
        # **attributes collects any keyword arguments into a Python dict
        # Example call: AttributeGroup(speed=50, strength=60)
        # attributes will be {'speed': 50, 'strength': 60}
        self.values = attributes   # store the attributes in a dict

    def __getitem__(self, key):
        # Called when you do group[key], for example: group['speed']
        # We return the stored value if present, otherwise 0 (safe default)
        return self.values.get(key, 0)

    def __setitem__(self, key, value):
        # Called when you assign: group['speed'] = 70
        self.values[key] = value

    def as_dict(self):
        # Return a plain Python dict representing this group's data.
        # dict(self.values) makes a shallow copy, so callers won't be editing
        # the internal dict by accident.
        return dict(self.values)

    def __repr__(self):
        # This is the "official" string representation used by `print()` and the REPL.
        # Keep it simple and developer-focused.
        return f"{self.values}"
    
    # The Attributes container that groups multiple AttributeGroup objects
class Attributes:
    def __init__(self):
        # Create default groups with default values.
        # You can change these defaults, add new groups, or load from a template later.
        self.physical = AttributeGroup(
            speed=50,
            strength=50,
            stamina=50,
            agility=50,
        )
        self.mental = AttributeGroup(
            focus=50,
            willpower=50,
            composure=50,
        )
        self.technical = AttributeGroup(
            accuracy=50,
            kicking=50,
            passing=50,
        )

    def as_dict(self):
        # Convert the entire Attributes object to a nested dict suitable for JSON.
        return {
            'physical': self.physical.as_dict(),
            'mental': self.mental.as_dict(),
            'technical': self.technical.as_dict()
        }

    def get(self, attr_name):
        # Generic getter: search each group for the named attribute.
        # Returns the found value, or None if not found at all.
        for group in (self.physical, self.mental, self.technical):
            if attr_name in group.values:
                return group[attr_name]
        return None
