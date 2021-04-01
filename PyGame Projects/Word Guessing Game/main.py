import random


words = open('C:/Users/zhewe/OneDrive/Documents/Coding Projects/Learn-Python/PyGame Projects/Word Guessing '
             'Game/words.txt', 'r')


class Main:
    def __init__(self):
        self.word = ''
        self.replacement = ''

    def word_gen(self):
        possibility = [True, False, False]
        for word in words.readlines():
            if random.choice(possibility):
                self.word = word.rstrip()
                self.replacement = '-' * len(self.word)
        if self.word:
            return True
        return False

    def guess_word(self, guess):
        if guess == self.word:
            return True
        return False

    def guess_letter(self, guess):
        if guess not in self.word:
            return False
        return True

    def guess_letters(self, guess):
        for i in list(guess):
            if i not in self.word:
                return False
        return True  # For now...

    def current_words(self):
        return self.replacement   # Just to show the current letters that the user got and missed

    def give_up(self):
        return f'The word was: {self.word}'


if __name__ == '__main__':
    main = Main()
    main.word_gen()
    print(main.current_words())
    print(main.give_up())
