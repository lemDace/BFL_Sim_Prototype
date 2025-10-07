class Field:
    location: str
    length: float
    width: float
    away_team_score: int
    home_team_score: int

    def __init__(self, location:str, length:float=1000, width:float=500) -> None:
        self.location = location
        self.length = length
        self.width = width
        self.away_team_score = 0
        self.home_team_score = 0