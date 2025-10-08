from engine import GameEngine
from entity.field import Field

if __name__ == "__main__":
    field = Field("Test Field", 1000, 500)
    engine = GameEngine(field)

    # Access player data
    krizzler = engine.players[2]
    print(krizzler.name, "speed:", krizzler.attributes.get("physical", "speed"))
    print(krizzler.attributes.groups["technical"]["accuracy"])
        















