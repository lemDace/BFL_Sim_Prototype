from entity import *

class GameEngine:
    field: Field
    home_team: Team
    away_team: Team
    ball: Ball
    gameLength: int

    def __init__(self, field:Field,hometeam:Team,awayteam:Team) -> None:
        self.field = field
        self.gameLength = 30
        self.home_team = hometeam
        self.away_team = awayteam
        self.ball = Ball(Vector2(self.field.length/2, self.field.width/2))
        self.log: list[str] = []
        self.tick_count: int = 0

    #return a list of all active players in this game
    def get_all_players(self) -> list[Player]:
        return self.home_team.get_active_players() + self.away_team.get_active_players()


    def update(self):
        self.tick_count += 1

        #find closest player to ball
        active_players = self.get_all_players()
        closest_player_to_ball = min(active_players,key=lambda p: p.distance_to_ball(self.ball))

        #move closest player toward ball
        closest_player_to_ball.move_towards_target(self.ball.position)

        if closest_player_to_ball.distance_to_ball(self.ball) < 5:
            closest_player_to_ball.pick_up_ball(self.ball)
            self.log.append(f"Tick {self.tick_count}: {closest_player_to_ball.name} picked up the ball")
            closest_player_to_ball.kick_ball(self.ball,Vector2(random.randint(50, 750),random.randint(50,550)),10)
            self.log.append(f"Tick {self.tick_count}: {closest_player_to_ball.name} kicked the ball")
            
        if self.tick_count % 20 == 0:
            self.log.append(f"Ball at ({self.ball.position.x:.1f},{self.ball.position.y:.1f})")
