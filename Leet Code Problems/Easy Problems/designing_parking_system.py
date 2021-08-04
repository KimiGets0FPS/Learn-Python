# TODO: FINISH THIS PROBLEM
# LINK: https://leetcode.com/problems/design-parking-system/


# big: 3; medium: 2; small: 1;


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def add_car(self, car_type: int) -> bool:
        ...


if __name__ == '__main__':
    solution = ParkingSystem
