import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        # brains = 0
        # while diceRollResults is not None:
        #     brains += diceRollResults['brains']

        #     if brains >= 2:
        #         diceRollResults = zombiedice.roll() # roll again
        #     else:
        #         break
# construct A bot that, after the first roll, randomly decides if it will continue or stop
# use rantint(0,1) if 0, stop, if 1 continue
        # turn = 0
        # coin_flip = 1
        # while diceRollResults is not None:
        #     diceRollResults = zombiedice.roll() # roll again
        #     turn += 1
        #     print str(turn) + " is turn number"
        #     coin_flip = random.randint(0,1) # 0 means stop
        #     if coin_flip == 0:
        #         print "flip is 0, stopping"
        #         diceRollResults = None
# A bot that initially decides it will roll the dice one to four times, but will stop early if it rolls two shotguns
# main logic: stop at 2 shotguns
# sublogic, roll 1 to 4 times only
        # one roll has already happened
        # shotguns = 0
        # rolls = 1
        # rolls_to_try = random.randint(1,4)
        # # print rolls_to_try
        # print "max of {} rolls".format(rolls_to_try)
        # while diceRollResults is not None: # while not dead
        #     shotguns += diceRollResults['shotgun']
        #     print "this is the {} roll".format(rolls+1)
        #     if shotguns >= 2:
        #         if rolls < rolls_to_try:
        #             print "rolling again"
        #             rolls += 1 # start next roll
        #             diceRollResults = zombiedice.roll() # roll again
        #         else:
        #             break
        #     else:
        #         break
            # infinte loop on something
# A bot that stops rolling after it has rolled more shotguns than brains
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']


            if brains >= shotguns: 
                print "rolling"
                diceRollResults = zombiedice.roll() # roll again
            else:
                break


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
