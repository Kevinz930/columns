from jewel import Jewel
import pygame


class PinkJewel(Jewel):

    def __init__(self, r, c):
        """Initialize the jewel"""
        image = pygame.image.load('images/jewel_pink.png')
        Jewel.__init__(self, r, c, image)