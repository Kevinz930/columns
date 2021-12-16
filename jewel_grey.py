from jewel import Jewel
import pygame


class GreyJewel(Jewel):

    def __init__(self, r, c):
        """Initialize the jewel"""
        image = pygame.image.load('images/jewel_grey.png')
        Jewel.__init__(self, r, c, image)