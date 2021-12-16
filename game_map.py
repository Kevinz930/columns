import settings
from faller import Faller
import pygame


class GameMap:

    def __init__(self):
        """Initialize the board """
        self.rows = settings.board_height
        self.columns = settings.board_length
        self.board = [[None for r in range(settings.board_length)] for c in range(settings.board_height)]
        self.f = Faller()
        self.speed = "normal"

    def tick(self):
        # Check if the faller has landed
        if self.f.placed is True:
            # Create a new faller and delete the old one
            pygame.time.delay(500)
            self.f = Faller()
        else:
            self.f.fall(self.board, self.speed)
            #self.check_match()

    def check_match(self):
        """Check for matches"""
        # Add matched jewels to a list, return it
        matched = []
        for r in range(0, len(self.board)):
            for c in range(0, len(self.board[0])):
                if self.board[r][c] is not None:
                    # Vertical match
                    if (r + 1 < settings.board_height and self.board[r+1][c] is not None and
                            type(self.board[r][c]) is type(self.board[r+1][c])):
                            if (r + 2 < settings.board_height and self.board[r+2][c] is not None and
                                    type(self.board[r][c]) is type(self.board[r+2][c])):
                                    matched.append(self.board[r][c])
                                    matched.append(self.board[r+1][c])
                                    matched.append(self.board[r+2][c])
                            if (r - 1 >= 0 and self.board[r-1][c] is not None and
                                    type(self.board[r][c]) is type(self.board[r-1][c])):
                                    matched.append(self.board[r][c])
                                    matched.append(self.board[r+1][c])
                                    matched.append(self.board[r-1][c])
                    if (r - 1 >= 0 and self.board[r-1][c] is not None and
                            type(self.board[r][c]) is type(self.board[r-1][c])):
                            if (r + 1 < settings.board_height and self.board[r+1][c] is not None and
                                    type(self.board[r][c]) is type(self.board[r+1][c])):
                                    matched.append(self.board[r][c])
                                    matched.append(self.board[r-1][c])
                                    matched.append(self.board[r+1][c])
                            if (r - 2 >= 0 and self.board[r-2][c] is not None and
                                    type(self.board[r][c]) is type(self.board[r-2][c])):
                                    matched.append(self.board[r][c])
                                    matched.append(self.board[r-1][c])
                                    matched.append(self.board[r-2][c])
        if len(matched) > 0:
            self.match(matched)

    def match(self, matched = []):
        """Delete matched jewels"""
        for jewel in matched:
            self.board[jewel.r][jewel.c] = None
        pygame.time.delay(500)
        self.fall()

    def fall(self):
        pass

    def check_events(self):
        """Check event type"""
        for event in pygame.event.get():
            if event.type is pygame.KEYDOWN:
                self.keydown(event)
            if event.type is pygame.KEYUP and event.key == pygame.K_DOWN:
                self.speed = "normal"
            elif event.type is pygame.QUIT:
                pygame.quit()
                quit()

    def keydown(self, event):
        """Check keydown events"""
        if event.key == pygame.K_DOWN:
            self.speed = "fast"
        elif event.key == pygame.K_LEFT:
            self.f.move("left", self.board)
        elif event.key == pygame.K_RIGHT:
            self.f.move("right", self.board)
        elif event.key == pygame.K_SPACE:
            self.f.rotate()
        elif event.key == pygame.K_q:
            pygame.quit()
            quit()

    def draw(self, screen):
        """Draw the game"""
        # Draw the background
        screen.fill(settings.background_color)

        # Draw the horizontal lines
        for r in range(settings.board_height):
            pygame.draw.line(screen, settings.line_color,
                             [0, (int(settings.screen_height / settings.board_height)) * r],
                             [settings.screen_width, (int(settings.screen_height / settings.board_height) * r)])

        # Draw the vertical lines
        for c in range(settings.board_length):
            pygame.draw.line(screen, settings.line_color, [(int(settings.screen_width/settings.board_length) * c), 0],
                             [(int(settings.screen_width/settings.board_length) * c), settings.screen_height])

        # Draw the jewels
        for r in range(0, len(self.board)):
            for c in range(0, len(self.board[0])):
                if self.board[r][c] is not None:
                    self.board[r][c].draw(screen)

        # Draw the faller
        if self.f.placed is False:
            self.f.draw(screen)

        # Display the new screen
        pygame.display.flip()
