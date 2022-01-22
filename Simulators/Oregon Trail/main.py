def main(p1, p2, p3, p4, status, selected_c):
    while True:
        ...


CLASSES = {'Banker': [1200, 200], 'Farmer': [600, 600], 'Carpenter': [800, 400]}
SUPPLIES = ["100 Bullets", "Clothes", "200 pounds of food", "Wheel", "Axle", "Tongue", "Oxen"]
UH_OH = ["Dysentery", " Cholera", "Bad Water", "Broken Arm"]
TRAIL = ["River", "Fort", "Village", "Normal Bad", "Normal"]


if __name__ == '__main__':
    print("Welcome to Oregon Trail!\nEnter the names of your wagon mates")
    name1 = input('1. ')
    name2 = input('2. ')
    name3 = input('3. ')
    name4 = input('4. ')
    PEOPLE = {name1: [], name2: [], name3: [], name4: []}
    # Effects that they have
    while True:
        print("What class do you want to be (Enter number)\n1. Banker\n2. Farmer\n3. Carpenter")
        # Banker starts off with more money
        # Farmer starts off with more food
        # Carpenter have more spare parts and fix wagon easier
        s_class = input("Class: ")
        if s_class == '1' or s_class == '2' or s_class == '3':
            print("Good Choice!")
            break
        print("Class is not valid")
    print("Loading...")
    main(name1, name2, name3, name4, PEOPLE, s_class)
