from Würfelspiel import Gameboard
import random

class Dice:

    def __init__(self):
        self.__sides = [1, 2, 3, 4, 5, 6]
        self.__side_num = None

    def get_roll(self) -> int:
        return self.__side_num

    def roll(self):
        self.__side_num = random.choice(self.__sides)

def start_die(num_die: int) -> list:
    die = []
    for dice in range(num_die):
        die.append(Dice())
    return die

def roll_die(die: list) -> list:
    die_nums = []
    for x in die:
        x.roll()
        die_nums.append(x)
    return die_nums











