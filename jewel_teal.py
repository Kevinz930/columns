from jewel import Jewel
import pygame


class TealJewel(Jewel):

    def __init__(self, r, c):
        """Initialize the jewel"""
        image = pygame.image.load('images/jewel_teal.png')
        Jewel.__init__(self, r, c, image)