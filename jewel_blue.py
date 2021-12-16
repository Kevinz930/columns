from jewel import Jewel
import pygame


class BlueJewel(Jewel):

    def __init__(self, r, c):
        """Initialize the jewel"""
        image = pygame.image.load('images/jewel_blue.png')
        Jewel.__init__(self, r, c, image)