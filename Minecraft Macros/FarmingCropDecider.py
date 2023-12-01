"""
This script was written by KimiGets0FPS_YT

Does not actually do anything useful, just helps me decide what crop to farm

PROFIT MARGINS WITH 920~ FARMING FORTUNE:
- Bountiful reforge + Mooshroom Cow + Cropie/Squash/Fermento
1. Cactus 470 speed (12.45m/h)
2. Mushroom 232 speed (10.56m/h)
3. Melon 280 speed (10.53m/h)
4. Pumpkin 280 speed (10.41m/h)
5. Cocoa Beans 155 speed (10.40m/h)
6. Carrot 93 speed (8.72m/h)
7. Netherwart 93 speed (8.67m/h)
8. Wheat 93 speed (8.40m/h)
9. Potato 93 speed (8.05m/h)
10. Sugarcane 328 speed (7.97m/h)

"""


import random


def main():
    print("""
1. Cactus 470 speed (12.45m/h)
2. Mushroom 232 speed (10.56m/h)
3. Melon 280 speed (10.53m/h)
4. Pumpkin 280 speed (10.41m/h)
5. Cocoa Beans 155 speed (10.40m/h)
6. Carrot 93 speed (8.72m/h)
7. Netherwart 93 speed (8.67m/h)
8. Wheat 93 speed (8.40m/h)
9. Potato 93 speed (8.05m/h)
10. Sugarcane 328 speed (7.97m/h)
        """)
    print(f"You will be farming: {random.choice(['Wheat', 'Carrots', 'Potato', 'Netherwart','Mushrooms','Melon','Pumpkin','Sugar Cane', 'Cocoa Beans'])}")


if __name__ == "__main__":
    main()
