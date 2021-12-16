import settings
import pygame

class Jewel(pygame.sprite.Sprite):

    def __init__(self, r, c, image):
        """Initialize the jewel"""
        super(Jewel, self).__init__()

        # Set dimensions
        self.width = int(settings.screen_width / settings.board_length)
        self.height = int(settings.screen_height / settings.board_height)

        # Scale image and initialize rectangle
        self.image = pygame.transform.scale(image, (self.width, self.height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = c * self.width
        self.rect.y = r * self.height

        # Initialize coordinates and variables
        self.r = r
        self.c = c
        self.placed = False
        self.falling = False

    def move(self, direction):
        """Move the jewel left or right"""
        if direction == "left" and self.c > 0:
            self.c -= 1
            self.rect.x -= self.width
        elif direction == "right" and self.c < settings.board_length - 1:
            self.c += 1
            self.rect.x += self.width

    def fall(self, board, speed):
        """Make the jewel fall"""
        if self.check_fall(board):
            self.rect.y += int(settings.screen_height/500)
            if speed == "fast":
                self.rect.y += int(settings.screen_height/500)*2
            if speed == "drop":
                self.rect.y += int(settings.screen_height / 500) * 2
            # Increase r if the jewel has fallen into the space below
            if self.rect.y >= (self.r + 1) * self.height:
                self.r += 1
        else:
            self.placed = True

    def check_fall(self, board):
        """Check if the space below the jewel is empty"""
        if (self.r < settings.board_height - 1 and ((board[self.r+1][self.c] is None) or
                 self.rect.bottom < board[self.r+1][self.c].rect.top)):
            return True
        return

    def draw(self, screen):
        """Draw the jewel"""
        screen.blit(self.image, self.rect)