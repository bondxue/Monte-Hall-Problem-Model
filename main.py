'''
6.2.1
Purpose: This program is to test Monty Hall game using multi-processing
Author: Mengheng
Date: 11/23/2018
'''

from game import Game
from player import Player
from timer import Timer
import multiprocessing


# doWork function can be any function with any argument
def doWork(input, output):
    while (True):
        try:
            f, args = input.get(timeout=1)
            res = f(*args)
            output.put(res)
        except:
            output.put('Done')
            break


# run Monte Carlo function of Monty Hall game
# strategy = 2:always switch
# strategy = 1: always not switch
def runMC(trails, strategy):
    # create player1 that always switch
    player = Player()
    player.switch(strategy)

    game_res = []  # store the wining cases for player 1

    for t in range(trails):
        game = Game(player)

        if game.playGame():  # game.playGame() is true
            game_res.append(1)
    return game_res


def main():
    num_trails = 10000000
    num_processes = 5  # number of processes

    # strategy = 2:always switch
    # strategy = 1: always not switch
    strategy = 2

    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    # add 5 runMC function items into input_queue
    for i in range(num_processes):
        input_queue.put((runMC, (num_trails / num_processes, strategy)))

    # use Timer context manager to record running time of MC
    with Timer('MC time cost: '):
        # create 5 child processes
        for i in range(num_processes):
            p = multiprocessing.Process(target=doWork, args=(input_queue, output_queue))
            p.start()

        res = []  # result
        # return the result list
        while True:
            r = output_queue.get()
            if r != 'Done':
                res.append(r)
            else:
                break

    # since res is a list of list, we need to flatten it to a single list first
    flattened_res = [item for sublist in res for item in sublist]

    if strategy == 1:
        print 'strategy to always stay winning probability: {}'.format(float(len(flattened_res)) / float(num_trails))
    if strategy == 2:
        print 'strategy to always switch winning probability: {}'.format(float(len(flattened_res)) / float(num_trails))

    '''
    (d) the running time is improved from the previous level 
    (e) choose strategy to always stay and record MC running time cost with different number of processes:
        num_processes = 1:  93.6119999886 s
        num_processes = 5:  12.996999979 s
        num_processes = 10: 11.8120000362 s
        num_processes = 15: 10.9649999142 s
        num_processes = 17: 11.1519999504 s
        num_processes = 20: 11.9139997959 s
        num_processes = 25: 11.5650000572 s
    Based on my simulation test, the optimal running time number of processes is 15. 
    '''


if __name__ == '__main__':
    main()
