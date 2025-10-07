class Status:
    def __init__(self, name: str, duration: int, effects: dict):
        self.name = name
        self.duration = duration
        self.effects = effects

    def tick(self):
        self.duration -=1
        return self.duration > 0 # return true if still active