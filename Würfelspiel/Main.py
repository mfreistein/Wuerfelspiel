from Würfelspiel import Gameboard, Dice, Player

class Game:

    def __init__(self):
        self.p = Player.Player()
        self.g = Gameboard.Gameboard(Dice.roll_die(Dice.start_die(6)))

    def main(self):
        while True:
            if self.check_null_points(list(self.g.get_die_rolled_int_list())): self.clear_prelim_points_and_complete_reroll()
            decision = self.get_move()
            if int(decision) is 7: self.lock_prelim_points_and_complete_reroll([])
            else:
                self.check_input(list(map(int, decision)))
                move_points = self.calculate_max_points(list(map(int, decision)))
                print("The chosen numbers could be worth " + str(self.p.get_prelim_points() + move_points) +" points")
                confirm = int(self.confirm_move())
                if confirm is 1: continue
                elif confirm is 2: self.lock_prelim_points_and_roll_remaining(list(map(int, decision)))
                elif confirm is 3: self.lock_prelim_points_and_complete_reroll(list(map(int, decision)))
                else: print("Incorrect input! Please try again!") and self.get_move()

    def get_move(self) -> str:
        self.p.print_total_points()
        self.p.print_prelim_points()
        self.g.print_die_rolled()
        return input("Choose your numbers or press 7 to lock your points: \n")

    def confirm_move(self) -> str:
        return input("Please choose next action: \n"
                     "1. Undo choice\n"
                     "2. Confirm choice and roll remaining die\n"
                     "3. Confirm choice and points to total\n")

    def check_input(self, move: list):
        if self.check_valid_input(move) is False:
            print("Numbers taken were not rolled! Please try again!")
            self.get_move()
        if (self.check_valid_move(move) is False) or (self.check_null_points(move) is True):
            print("This is not a valid move! Please try again!")
            self.get_move()

    def check_valid_input(self, die_taken: list) -> bool:
        return all(item in self.g.get_die_rolled_int_list() for item in die_taken)

    def check_null_points(self, die_taken: list) -> bool:
        if self.calculate_max_points(die_taken) is 0:
            return True
        return False

    def check_valid_move(self, die_taken: list) -> bool:
        for x in set(die_taken):
            if (self.calculate_non_special_points(int(x), int(die_taken.count(x))) is 0) and (len(die_taken) is not 6):
                return False
        return True

    def calculate_max_points(self, die_taken: list) -> int:
        points = 0
        distinct_nums = set(die_taken)
        for x in distinct_nums:
            points += self.calculate_non_special_points(int(x), int(die_taken.count(x)))
        if len(die_taken) is 6:
            if self.check_street(die_taken):
                points = max(2000, points)
            if self.check_triple_double(die_taken):
                points = max(1500, points)
        return points

    def calculate_non_special_points(self, eye: int, quantity: int) -> int:
        if (eye is 1) and (quantity < 3):
            return (eye * 100) * quantity
        elif (eye is 5) and (quantity < 3):
            return (eye * 10) * quantity
        elif (eye is 1) and quantity > 2:
            return (eye * 1000) * 2 ** (quantity - 3)
        elif quantity > 2:
            return (eye * 100) * 2 ** (quantity - 3)
        else:
            return 0

    def check_street(self, die_taken: list) -> bool:
        eyes = sorted(list(map(int, die_taken)))
        return all(eyes[i] < eyes[i + 1] for i in range(len(eyes) - 1))

    def check_triple_double(self, die_taken: list) -> bool:
        eyes = sorted(list(map(int, die_taken)))
        if eyes[0] == eyes[1] and eyes[2] == eyes[3] and eyes[4] == eyes[5]:
            return True
        return False

    def lock_prelim_points_and_complete_reroll(self, move: list):
        self.g.update_gameboard_with_int_list(move)
        self.p.add_prelim_points(self.calculate_max_points(move))
        self.p.print_prelim_points()
        self.p.lock_prelim_points()
        self.p.print_total_points
        self.g.complete_reroll()

    def lock_prelim_points_and_roll_remaining(self, move: list):
        self.g.update_gameboard_with_int_list(move)
        self.p.add_prelim_points(self.calculate_max_points(move))
        self.p.print_prelim_points()
        self.g.reroll_remaining()

    def clear_prelim_points_and_complete_reroll(self):
        print(str(self.p.get_prelim_points())+ " Nüscht!")
        self.p.clear_prelim_points()
        self.g.complete_reroll()

