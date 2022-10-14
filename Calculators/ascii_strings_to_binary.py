import os


def clear():
    os.system('cls' if os.name == "nt" else "clear")


def ascii_to_binary():
    while True:
        binary = []
        value = input()
        if not value:
            return
        value = ord(value)
        print(f"Ascii: {value}")
        while value != 0:
            if value % 2 != 0:
                value -= 1
                binary.append('1')
            else:
                binary.append('0')
            value /= 2
        if len(binary) < 8:
            for _ in range(8 - len(binary)):
                binary.append('0')
        binary.reverse()
        print(f"Binary: {''.join(binary)}")
        input("Enter to Continue...")
        clear()


def binary_to_ascii():
    while True:
        binary = input().split()
        if not binary:
            return
        value = []
        ascii_code = []
        for i in range(0, len(binary)//2, 2):
            j = binary[i] + binary[i+1]
            ascii_code.append(int(j, 2))
            value.append(chr(int(j, 2)))
        print(f"Ascii: {ascii_code}")
        print(f"Character: {''.join(str(value))}")
        input("Enter to Continue...")
        clear()


if __name__ == "__main__":
    ascii_to_binary()
    binary_to_ascii()
