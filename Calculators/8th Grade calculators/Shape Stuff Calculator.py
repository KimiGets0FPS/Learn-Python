import math
import os
import time


def find_circle_area(radius):
    return (radius**2) * math.pi


def find_sphere_volume(radius):
    return ((radius ** 3) * math.pi * 4) / 3


def find_half_sphere_volume(radius):
    return find_sphere_volume(radius) / 2


def find_cylinder_volume(radius, height):
    return find_sphere_volume(radius) * height


def find_cone_volume(radius, height):
    return ((radius**2) * math.pi * height) / 3


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        print(
            # Circle Related
            "1. Area of Circle"
            "\n2. Volume of Sphere"
            "\n3. Volume of Half Sphere"
            "\n4. Volume of Cylinder"
            "\n5. Volume of Cone"
            
            # Square and Rectangles
            "\n6. "
              )
        choice = input("Enter the choice by number: ")

        if choice:
            choice = int(choice)

            if choice <= 5:  # Circle related calculations
                radius = input("Enter value for radius: ")
                if radius:

                    if choice == 1:
                        print(find_circle_area(float(radius)))

                    elif choice == 2:
                        print(find_sphere_volume(float(radius)))

                    elif choice == 3:
                        print(find_half_sphere_volume(float(radius)))

                    elif choice == 4:
                        height = input("Enter value for height: ")
                        if height:
                            print(find_cylinder_volume(float(radius), float(height)))

                    elif choice == 5:
                        height = input("Enter value for height: ")
                        if height:
                            print(find_cone_volume(float(radius), float(height)))

            input("Press enter to continue...")
            clear()

        else:
            return


if __name__ == "__main__":
    clear()
    main()
    print("Thank you for using my calculator!")
    time.sleep(2)
    clear()
