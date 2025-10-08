

class AttributeGroup:
    #Represents a single group of related attributes, e.g. 'physical' or 'mental'.

    def __init__(self, name: str, attributes: dict):
        self.name = name
        self.attributes = attributes  # dictionary: {attribute_name: value}

    def __getitem__(self, key):
        #Allows accessing attributes like: player.attributes.groups['physical']['speed']
        return self.attributes.get(key)

    def __setitem__(self, key, value):
        #Allows setting attributes like: player.attributes.groups['physical']['speed'] = 95
        self.attributes[key] = value

    def as_dict(self):
        #Convert group back to a plain dictionary (useful for saving to JSON)
        return self.attributes

    def __repr__(self):
        #Readable string version for debugging.
        return f"<AttributeGroup {self.name}: {self.attributes}>"
    
    
class Attributes:
    #Container for all attribute groups belonging to an entity (player, coach, etc.)

    def __init__(self, groups=None):
        self.groups = groups or {}
        

    @classmethod
    def from_dict(cls, data: dict):
        #Factory method to create an Attributes object from a JSON/dict structure.
        #Example input:
        #{
        #    "physical": {"speed": 90, "strength": 80},
        #    "mental": {"focus": 75}
        #}
        
        groups = {}
        for group_name, attrs in data.items():
            groups[group_name] = AttributeGroup(group_name, attrs)
        return cls(groups)
    
    def as_dict(self):
        #Convert all groups back into a JSON-friendly dictionary.

        return {name: group.as_dict() for name, group in self.groups.items()}

    def get(self, group_name, attribute_name):
        #Safely get a specific attribute value.
        
        group = self.groups.get(group_name)
        if group:
            return group[attribute_name]
        return None
    
    def set(self, group_name, attribute_name, value):
        #Safely update an attribute

        if group_name not in self.groups:
            self.groups[group_name] = AttributeGroup(group_name, {})
        self.groups[group_name][attribute_name] = value

    def __repr__(self):
        return f"<Attributes {', '.join(self.groups.keys())}>"
       
