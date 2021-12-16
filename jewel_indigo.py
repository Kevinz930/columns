from jewel import Jewel
import pygame


class IndigoJewel(Jewel):

    def __init__(self, r, c):
        """Initialize the jewel"""
        image = pygame.image.load('images/jewel_indigo.png')
        Jewel.__init__(self, r, c, image)