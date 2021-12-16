from jewel import Jewel
import pygame


class PurpleJewel(Jewel):

    def __init__(self, r, c):
        """Initialize the jewel"""
        image = pygame.image.load('images/jewel_purple.png')
        Jewel.__init__(self, r, c, image)