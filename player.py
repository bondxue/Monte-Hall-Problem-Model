'''
Purpose: This program is create Monty Hall game player class
Author: Mengheng
Date: 11/22/2018
'''

import random


class Player(object):
    def __init__(self, choice=None, switch_decision=None):
        self._choice = choice
        self._switch_decision = switch_decision

    # function to chose a door
    def choose_door(self, options):
        self._choice = random.choice(options)
        return self._choice

    # function to decide whether or not switch a door
    # switch_choice = 1: switch
    # switch_choice = 2: not switch
    def switch(self, switch_choice):
        self._switch_decision = switch_choice

    @property
    def switch_decision(self):
        return self._switch_decision

    @property
    def choice(self):
        return self._choice

    @switch_decision.setter
    def switch_decision(self, iswitch_decision):
        self._switch_decision = iswitch_decision

    @choice.setter
    def choice(self, ichoice):
        self._choice = ichoice
