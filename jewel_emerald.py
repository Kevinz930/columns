from jewel import Jewel
import pygame


class EmeraldJewel(Jewel):

    def __init__(self, r, c):
        """Initialize the jewel"""
        image = pygame.image.load('images/jewel_emerald.png')
        Jewel.__init__(self, r, c, image)