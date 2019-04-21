'''
Purpose: This program is to test Monty Hall game
Author: Mengheng
Date: 11/23/2018
'''

from game import Game
from player import Player
from timer import Timer


def main():
    # create player1 that always switch
    player1 = Player()
    player1.switch(2)

    # create player2 that always not switch
    player2 = Player()
    player2.switch(1)

    game1_res = []  # store the wining cases for player 1
    game2_res = []  # store the wining cases for player 2

    trails = 10000000

    with Timer('Monty Hall game time cost: '):
        for t in range(trails):
            game1 = Game(player1)
            game2 = Game(player2)

            if game1.playGame():  # game1.playGame() is true
                game1_res.append(1)
            if game2.playGame():  # game2.playGame() is true
                game2_res.append(1)

    print 'strategy to switch winning probablity: {}'.format(float(len(game1_res)) / float(trails))
    print 'strategy to stay wining probablity: {}'.format(float(len(game2_res)) / float(trails))


'''
my hypothesis is switching will increase the probability to win in Monty Hall game and Monte Carlo simulation
proves I am right. 
Simulation results:
Monty Hall game time cost: : 67.7960000038 s
strategy to switch winning probablity: 0.66661
strategy to stay wining probablity: 0.3334279
'''

if __name__ == '__main__':
    main()
