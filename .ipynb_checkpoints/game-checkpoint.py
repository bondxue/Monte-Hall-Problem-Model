'''
Purpose: This program is create Monty Hall game class
Update:  11/22/2018 hide the user inputs to run Monte Carlo simulation
Author: Mengheng
Date: 11/22/2018
'''

import random
from player import Player


class Game(object):
    def __init__(self, player):
        self._player = player
        self._options = [1, 2, 3]

    def playGame(self):
        true = random.choice(self._options)  # randomly place prize behind one of three doors
        wrong = [x for x in self._options if x != true]  # rest are all goats
        # self._player.choice = int(raw_input('Please enter your door choice (1/2/3): '))  # ask player to choose a door
        self._player.choose_door(self._options)

        # reveal a false door with goat in it
        if self._player.choice not in wrong:
            reveal = random.choice(wrong)
        else:
            reveal = [x for x in wrong if x != self._player._choice][0]

        # the rest door options after revealing one door with goat
        updated_options = [x for x in self._options if x != reveal]

        # self._player.switch_decision = int(raw_input('Would you like to switch the door(1: NO/ 2: YES)? '))
        # switch_decision = 1: keep same door choice
        # switch_decision = 2: Switching your door choice to another randomly selected door (that is not your original door)

        if self._player.switch_decision == 1:
            strategy = self._player.choice
        else:
            strategy = random.choice([x for x in updated_options if x != self._player.choice])

        # check the final chosen door result and return a Boolean result
        if strategy == true:
            # print 'You win.'
            return True
        else:
            # print 'You lose.'
            return False
