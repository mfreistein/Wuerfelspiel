from Würfelspiel import Dice

class Gameboard:

    def __init__(self, die_rolled: list):
        self.__die_rolled = die_rolled
        self.__die_taken = []

    def get_die_rolled(self):
        return self.__die_rolled

    def print_die_rolled(self):
        print("Die rolled: " +str(self.get_die_rolled_int_list()))

    def clear_gameboard(self):
        self.__die_rolled.clear()
        self.__die_taken.clear()

    def reroll_remaining(self):
        self.__die_rolled = Dice.roll_die(Dice.start_die(len(self.__die_rolled)))

    def complete_reroll(self):
        self.clear_gameboard()
        self.__die_rolled = Dice.roll_die(Dice.start_die(6))

    def get_dice(self, eye: int) -> Dice:
        for x in self.__die_rolled:
            if int(eye) is int(x.get_roll()):
                return x
        else:
            return None

    def update_gameboard_with_int_list(self, move: list):
        for x in move:
            dice = self.get_dice(x)
            self.__die_taken.append(dice)
            self.__die_rolled.remove(dice)

    def get_die_rolled_int_list(self) ->list:
        list = []
        for x in self.__die_rolled:
            list.append(x.get_roll())
        return list