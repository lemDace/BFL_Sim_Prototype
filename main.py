import pygame
from typing import Tuple
import euclid3
import entity
from entity import *
from engine import GameEngine

def run_game() -> None:
    
    screen_width: int = 800#1200#800
    screen_height: int = 600#800#600


    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    running: bool = True

    #define colors
    red: Tuple[int, int, int] = (255, 0, 0)
    blue: Tuple[int, int, int] = (0, 0, 255)
    white: Tuple[int, int, int] = (255, 255, 255)

    #field
    field: Field = Field("MCG",screen_width,screen_height)


    #teams
    home_team: Team = Team("Red", red)
    away_team: Team = Team("Blue", blue)

    for i in range(10):
        home_team.add_player(Player(f"R{i}",Vector2(500,100+i*50),random.randint(2,2)))
        away_team.add_player(Player(f"B{i}",Vector2(300,100+i*50),random.randint(2,2)))

    #ball
    ball: Ball = Ball(field)

    engine: GameEngine = GameEngine(field,home_team,away_team)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #update logic
        engine.update()
        #ball.update()

        #draw
        screen.fill(white)

        #draw current ball
        pygame.draw.circle(screen,(0,0,0),(int(engine.ball.position.x),int(engine.ball.position.y)), 5)

        # Draw players
        for team in (home_team, away_team):
            for player in team.players:
                pygame.draw.circle(screen, team.color, (int(player.position.x), int(player.position.y)), 10)

        pygame.display.flip()
        clock.tick(60)

        while engine.log:
            print(engine.log.pop(0))

    pygame.quit()
    


if __name__ == "__main__":
    run_game()