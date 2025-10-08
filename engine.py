from euclid3 import Vector2
import json
import random
from entity import *

class GameEngine:
    field: Field
    home_team: Team
    away_team: Team
    ball: Ball
    gameLength: float

    #def __init__(self, field:Field,hometeam:Team,awayteam:Team) -> None:
    def __init__(self, field:Field) -> None:
        self.field = field
        self.gameLength = 30
        #self.home_team = hometeam
        #self.away_team = awayteam
        self.ball = Ball(self.field)
        self.log: list[str] = []
        self.tick_count: int = 0

        self.players = self.load_players("data/players/players_all.json")

        #prints all players loaded and their speed attribute
        print(f"Loaded {len(self.players)} players:")
        for p in self.players:
            print(f" - {p.name}: speed={p.attributes.get('physical', 'speed')}")

        #self.active_players = self.home_team.get_active_players() + self.away_team.get_active_players()

    def load_players(self, path: str):
        #Load player data from a JSON file into Player objects.
        #this loads general player data, not match specific data such as position on field

        with open(path,"r") as f:
            data = json.load(f) #loads the file into memory (data)

        players =[]

        for p in data['players']:
            player = Player(
                id=p['id'],
                name=p['name'],
                age=p['age'],
                started_playing=p['started_playing'],
                positionPlayed=p['position_played'],
                attributes=p['attributes']
            )
            players.append(player)
        
        return players #return the laoded list of player objects


    #return a list of all active players in this game
    def get_all_players(self) -> list[Player]:
        return self.home_team.get_active_players() + self.away_team.get_active_players()


    def update(self):
        self.tick_count += 1

        #find closest player to ball
        #active_players = self.get_all_players()
        closest_player_to_ball = min(self.active_players,key=lambda p: p.distance_to_ball(self.ball))

        #move closest player toward ball
        closest_player_to_ball.move_towards_target(self.ball.position)

        if closest_player_to_ball.distance_to_ball(self.ball) < 5:
            
            if closest_player_to_ball.has_ball == False:

                closest_player_to_ball.pick_up_ball(self.ball)
                self.log.append(f"Tick {self.tick_count}: {closest_player_to_ball.name} picked up the ball")

            if closest_player_to_ball.has_ball == True:

                closest_player_to_ball.kick_ball(self.ball,Vector2(random.randint(-350, 350),random.randint(-250,250)),10)
                self.log.append(f"Tick {self.tick_count}: {closest_player_to_ball.name} kicked the ball")

        self.ball.update()
            
        if self.tick_count % 65 == 0:
            self.log.append(f"Ball at ({self.ball.position.x:.1f},{self.ball.position.y:.1f})")
            self.log.append(f"{closest_player_to_ball.name} focus is: {closest_player_to_ball.get_attribute('focus')}")
