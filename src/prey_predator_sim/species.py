"""Module with definitions of considered species"""
import random

class Creature:

    alive: bool = True

    def __init__(self, p_death: float, p_reproduce: float):
        self.p_death = p_death
        self.p_reproduce = p_reproduce

    def kill(self):
        '''kills the creature with probablity p_death'''
        if random.random() < self.p_death:
            self.alive = False

    def reproduce(self):
        '''returns new instance of creature with probablity p_reproduce (otherwise: None)'''

        # to do: change creature class to different one

        if self.alive and  (random.random() < self.p_reproduce):
            return Creature(p_death=self.p_death, p_reproduce=self.p_reproduce)

        return None
