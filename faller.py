import settings
from jewel_blue import BlueJewel
from jewel_emerald import EmeraldJewel
from jewel_grey import GreyJewel
from jewel_indigo import IndigoJewel
from jewel_orange import OrangeJewel
from jewel_pink import PinkJewel
from jewel_purple import PurpleJewel
from jewel_red import RedJewel
from jewel_teal import TealJewel
from jewel_yellow import YellowJewel
import random


class Faller:

    def __init__(self, ):
        """Initialize the faller"""
        self.jewels = []
        self.generate()
        self.placed = False

    def generate(self):
        """Add three random jewels to the faller"""
        c = random.randint(0, 5)
        for r in range(-1, -4, -1):
            n = random.randint(1, 10)
            if n == 1:
                self.jewels.append(BlueJewel(r, c))
            elif n == 2:
                self.jewels.append(EmeraldJewel(r, c))
            elif n == 3:
                self.jewels.append(GreyJewel(r, c))
            elif n == 4:
                self.jewels.append(IndigoJewel(r, c))
            elif n == 5:
                self.jewels.append(OrangeJewel(r, c))
            elif n == 6:
                self.jewels.append(PinkJewel(r, c))
            elif n == 7:
                self.jewels.append(PurpleJewel(r, c))
            elif n == 8:
                self.jewels.append(RedJewel(r, c))
            elif n == 9:
                self.jewels.append(TealJewel(r, c))
            elif n == 10:
                self.jewels.append(YellowJewel(r, c))

    def fall(self, board, speed):
        """Make the faller fall"""
        if self.placed is False:
            for jewel in self.jewels:
                jewel.fall(board, speed)

        # Place the faller after it has landed
        if self.jewels[0].placed is True:
            self.placed = True
            self.place(board)

    def place(self, board):
        """Add the jewels to the board after they have fallen"""
        for jewel in self.jewels:
            if jewel.r >= 0:
                board[jewel.r][jewel.c] = jewel
                # Correct the jewel's coordinates
                jewel.rect.y = jewel.r * jewel.height

    def move(self, direction, board):
        """Move the faller horizontally"""
        if self.check_move(direction, board):
            for jewel in self.jewels:
                jewel.move(direction)

    def check_move(self, direction, board):
        """Check if the faller can be moved in a direction"""
        if direction == "left":
            for jewel in self.jewels:
                if jewel.r > 0 and jewel.c > 0 and board[jewel.r][jewel.c-1] is not None:
                    return False
        if direction == "right":
            for jewel in self.jewels:
                if jewel.r > 0 and jewel.c < settings.board_length - 1 and board[jewel.r][jewel.c+1] is not None:
                    return False
        return True

    def rotate(self):
        """Rotatae the faller"""
        self.jewels[0].r -= 2
        self.jewels[0].rect.y -= self.jewels[0].height*2
        self.jewels[1].r += 1
        self.jewels[1].rect.y += self.jewels[1].height
        self.jewels[2].r += 1
        self.jewels[2].rect.y += self.jewels[2].height
        self.jewels.append(self.jewels.pop(0))

    def check_game_over(self, board):
        """Check if the game has been lost"""
        for jewel in self.jewels:
            if jewel.placed is True and jewel.r < 0:
                return True
        return False

    def draw(self, screen):
        """Draw the faller"""
        for jewel in self.jewels:
            jewel.draw(screen)
