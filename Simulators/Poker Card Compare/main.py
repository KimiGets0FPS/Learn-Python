import random


numbers = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
symbols = list("♦♣♥♠")


cards = []
for i in numbers:
    for j in range(len(symbols)):
        cards.append(f"{symbols[j]}{i}")

random.shuffle(cards)  # Shuffle the cards

player1 = cards[len(cards)//2:]  # Player 1 takes the 1st half
player2 = cards[:len(cards)//2]  # Player 2 takes the 2nd half

print(player1)
print(player2)

count1, count2 = 25, 25
win1, win2, neither = 0, 0, 0
neutral = 0
i = 0
limit = 104
while True:
    if count1 == 0 or count2 == 0 or neutral > limit:
        break
    if i > min(count1, count2):
        i = 0
    if numbers[player1[i][1:]] == numbers[player2[i][1:]]:
        print(f"Tie Player 1:{player1[i]}  Player 2:{player2[i]}")
        neither += 1
        neutral += 1
    elif numbers[player1[i][1:]] > numbers[player2[i][1:]]:
        print("Player 1 wins")
        player1.append(player2[i])
        player2.remove(player2[i])
        count1 += 1
        count2 -= 1
        win1 += 1
        neutral = 0
    else:
        print("Player 2 wins")
        player2.append(player1[i])
        player1.remove(player1[i])
        count1 -= 1
        count2 += 1
        win2 += 1
        neutral = 0
    i += 1

print(f"\nTotal Games competed: {win1+win2+neither}\nPlayer 1 wins: {win1}\nPlayer 2 Wins: {win2}\nTie: {neither}")

if neutral >= limit:
    print("\nNeither Wins!!!")
if count1 == 0:
    print("\n\nPlayer 2 WINS!!!!!")
if count2 == 0:
    print("\n\nPlayer 1 WINS!!!!!")
