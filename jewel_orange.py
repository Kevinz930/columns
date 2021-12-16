from jewel import Jewel
import pygame


class OrangeJewel(Jewel):

    def __init__(self, r, c):
        """Initialize the jewel"""
        image = pygame.image.load('images/jewel_orange.png')
        Jewel.__init__(self, r, c, image)