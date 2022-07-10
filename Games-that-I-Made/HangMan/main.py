import random
import os
from termcolor import cprint
import json
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def replace_(word, good_guess):
    output = []
    for i in range(len(word)):
        flag = True
        for j in range(len(good_guess)):
            if word[i] == good_guess[j]:
                output.append(good_guess[j])
                flag = False
                break
        if flag:
            output.append('_')
    return output


def check(word, guess):
    for i in range(len(word)):
        if word[i] == guess:
            return True
    return False


def game():
    clear()
    with open("words.txt", 'r') as w:
        words = w.read().split("\n")
        word = random.choice(words)
    good_guess, bad_guess = [], []
    tries = 9
    while tries > 0:
        print(' '.join(replace_(word, good_guess)))
        if check(replace_(word, good_guess), '_'):
            user_guess = input("Your Guess: ")
            if user_guess:
                if len(user_guess) > 1:
                    if user_guess == word:
                        return [True, word, 9-tries]
                    else:
                        cprint("Incorrect word!", color='red')
                        tries -= 1

                else:
                    if check(good_guess, user_guess) or check(bad_guess, user_guess):
                        cprint("You've already tried that!", color='yellow')
                    else:
                        flag = check(word, user_guess)
                        if flag is True:
                            cprint("That's a letter in the word!", color='green')
                            good_guess.append(user_guess)
                        else:
                            cprint("That's not a letter in the word!", color='red')
                            bad_guess.append(user_guess)
                            tries -= 1
                print(f"You have {tries} tries!")
                input("Press Enter to Continue...")
            clear()
        else:  # Getting every letter correctly without guessing the actual word
            return [True, word, 9-tries]
    return [False, word]


name = ""


def main():
    global name
    while True:
        opt = input("1. Play Game\n2. View Score\nYour Choice (Enter to exit): ")
        if opt:
            if opt == "1":
                results = game()
                if results[0] is True:
                    with open("score.json", 'r') as s:
                        scores = json.load(s)
                    print(f"You Won! The word was: {results[1]}")
                    flag = True
                    while flag:
                        name = input("Your name: ")
                        ct = 0
                        for names in scores:
                            if names == name:
                                ct += 1
                                clear()
                                print("Enter a different name!")
                                break
                        if ct == 0:
                            flag = not flag
                    i, new_scores, prev_score = 0, {}, 0
                    if scores:
                        if len(scores) == 1:
                            f_name = ""
                            for i in scores:
                                f_name = i
                            if int(scores[f_name]) <= int(results[2]):
                                new_scores[f_name] = scores[f_name]
                                new_scores[name] = int(results[2])
                            else:
                                new_scores[name] = int(results[2])
                                new_scores[f_name] = scores[f_name]
                        else:
                            for f_name in scores:
                                if int(scores[f_name]) <= int(results[2]) <= int(prev_score):
                                    new_scores[name] = int(results[2])
                                    new_scores[f_name] = scores[f_name]
                                else:
                                    new_scores[f_name] = scores[f_name]

                                i += 1
                                prev_score = scores[f_name]

                    else:
                        new_scores[name] = int(results[2])
                    print("Score Updating...")
                    with open("score.json", 'w') as s:
                        print(new_scores)
                        json.dump(new_scores, s, indent=4)
                        s.close()
                    s.close()

                else:
                    print(f"You lost! The word was: {results[1]}")

            elif opt == "2":
                clear()
                with open("score.json", 'r') as s:
                    scores = json.load(s)
                if scores:
                    print("Top 10 Scores (Lower the Better):")
                    i = 1
                    for name in scores:
                        if i <= 10:
                            print(f"{i}. {name}: {scores[name]}")
                        i += 1
                else:
                    print("There's no Records!")
                input("Press Enter to Continue...")
                clear()
            else:
                cprint("Not an option!", color="red")
        else:
            return


if __name__ == "__main__":
    clear()
    main()
    print("Thank you for playing!")
    time.sleep(2)
    clear()
