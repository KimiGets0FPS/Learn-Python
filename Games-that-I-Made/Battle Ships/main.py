from termcolor import cprint
import json


class Game:
    def __init__(self):
        self.user_board = _get_board()[0]
        self.letters = list("ABCDEFGHIJK")

    def _gen_computer_side(self):
        b = []
        return b

    def _check_valid(self, ship, choice, place):
        current_board = self.user_board
        if ...:
            return True
        return False

    def _get_user_side(self):
        ships = {'Carrier': 5, 'BattleShip': 4, 'Submarine': 3, 'Cruiser': 3, 'Destroyer': 2}
        for s in ships:
            while True:
                print(f"Current ship type: {s}")
                choice = input("1. Head on Top\n2. Head on Bottom\n3. Head on Left\n4. Head on Right\nChoice:")
                place = list(input(f"Coordinates for {s} (Letter and Number): "))
                user_letter, number = place[0], int(''.join(place[1:]))
                for letter in range(len(self.letters)):
                    if letter == self.letters[letter]:
                        user_letter = letter
                if choice:
                    # UP and DOWN is looping through the NUMBERS
                    # LEFT and RIGHT is looping through LETTERS
                    if choice == "1":  # If Ship Going Down
                        validness = self._check_valid(s, choice, [user_letter, number])
                        if validness is True:
                            for column in range(len(self.user_board)):
                                if column == number:
                                    for columns in range(column, len(s)):
                                        self.user_board[user_letter][columns] = s[0]
                                    break
                    elif choice == "2":  # If Ship Going Up
                        validness = self._check_valid(s, choice, [user_letter, number])
                        if validness is True:
                            ...
                        else:
                            ...
                    elif choice == "3":  # If Ship Going Right
                        validness = self._check_valid(s, choice, [user_letter, number])
                        if validness is True:
                            ...
                        else:
                            ...
                    elif choice == "4":  # If Ship Going Left
                        validness = self._check_valid(s, choice, [user_letter, number])
                        if validness is True:
                            ...
                        else:
                            ...
        b = []
        return b

    def run(self, name):
        cprint(f"Welcome {name.title()}!", color='green')
        computer_board = self._gen_computer_side()
        user_board = self._get_user_side()


def main():
    while True:
        opt = input("1. Play Game\n2. Scores\nYour Choice (Press Enter to Exit): ")
        if opt:
            if opt == '1':
                game = Game()
                game.run(name=input("Your Name: "))
            elif opt == '2':
                ...
            else:
                print("Not an option!")
        else:
            return


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def store_score(name, score):  # Score is how many ships are left
    with open("scores.json", 'r') as s:
        scores = json.load(s)
        with open("scores.json", 'w') as sc:
            new_scores = {}
            for _score in range(len(scores)):
                ...
            json.dump(new_scores, sc, indent=4)


def _get_board() -> list[list[any], list[any]]:
    characters = ['  ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    numbers = ['1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', '11']
    fancy_board = [characters]  # First Row
    normal_board = []
    for c in range(len(characters)-1):
        r = [numbers[c]]
        for n in range(len(numbers)):
            r.append("~")
        fancy_board.append(r)
        normal_board.append(r)
    return [normal_board, fancy_board]


if __name__ == "__main__":
    board = _get_board()
    for i in range(len(board)):
        print(' '.join(board[i]))
