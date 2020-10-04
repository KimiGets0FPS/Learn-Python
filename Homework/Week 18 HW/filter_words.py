def filter_the_words():
    new_list = []
    user_input = input("Enter anything you want and I'll give you the numbers and nothing else: ")
    word_list = user_input.split()
    for word in word_list:
        try:
            word = int(word)
        except ValueError:
            pass
        else:
            new_list.append(word)
    print(new_list)


filter_the_words()
