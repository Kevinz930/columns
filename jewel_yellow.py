from jewel import Jewel
import pygame


class YellowJewel(Jewel):

    def __init__(self, r, c):
        """Initialize the jewel"""
        image = pygame.image.load('images/jewel_yellow.png')
        Jewel.__init__(self, r, c, image)