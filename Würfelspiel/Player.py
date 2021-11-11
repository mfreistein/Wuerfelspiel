class Player:

    def __init__(self):
        self.__total_points = 0
        self.__prelim_points = 0

    def get_points(self) -> int:
        return self.__total_points

    def lock_prelim_points(self):
        self.__total_points += self.__prelim_points
        self.__prelim_points = 0

    def add_prelim_points(self, points: int):
        self.__prelim_points += points

    def get_prelim_points(self):
        return self.__prelim_points

    def clear_prelim_points(self):
        self.__prelim_points = 0

    def print_prelim_points(self):
        print("Preliminary Points: " +str(self.__prelim_points))

    def print_total_points(self):
        print("Total Points: " + str(self.__total_points))

