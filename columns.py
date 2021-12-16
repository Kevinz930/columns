import settings
from game_map import GameMap
import pygame
import os


class Columns:

    def __init__(self):
        # Initialize pygame
        pygame.init()
        pygame.display.set_caption("Columns")
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

        # Start the game
        self.g = GameMap()
        self.run_game()

    def run_game(self):
        # Create a timer
        timer = pygame.time.Clock()
        time = 0
        while True:
            self.g.check_events()
            while self.g.f.check_game_over(self.g.board) is False:
                time += timer.tick()
                self.g.check_events()

                # Update the game every tick
                if time % settings.tick_duration == 0:
                    self.g.tick()
                    self.g.draw(self.screen)

                # Restart the game after losing
                if self.g.f.check_game_over(self.g.board) is True:
                    pygame.time.delay(1000)
                    self.g = GameMap()


c = Columns()
