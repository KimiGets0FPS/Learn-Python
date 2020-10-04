def how_many_vowels():
    while True:
        count_a = 0
        count_e = 0
        count_i = 0
        count_o = 0
        count_u = 0
        not_vowel = 0
        a = 'a'
        e = 'e'
        i = 'i'
        o = 'o'
        u = 'u'
        user_input = input("Give me a word and I'll tell you how much vowels is in that word(enter 'q' to quit): ")
        user_input = user_input.lower()
        if user_input == 'q':
            break
        else:
            for vowel in user_input:
                if a is vowel:
                    count_a += 1
                elif e is vowel:
                    count_e += 1
                elif i is vowel:
                    count_i += 1
                elif o is vowel:
                    count_o += 1
                elif u is vowel:
                    count_u += 1
                else:
                    not_vowel += 1
            print(f"\n'A' count:{count_a}\n'E' count:{count_e}\n'I' count:{count_i}\n'O' count:{count_o}")
            print(f"'U' count:{count_u}\nThe letters that are not vowels:{not_vowel}")


how_many_vowels()
