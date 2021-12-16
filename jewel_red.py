from jewel import Jewel
import pygame


class RedJewel(Jewel):

    def __init__(self,r, c):
        """Initialize the jewel"""
        image = pygame.image.load('images/jewel_red.png')
        Jewel.__init__(self, r, c, image)