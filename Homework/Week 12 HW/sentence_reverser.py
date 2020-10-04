def sentence_reverse():
    sentence = input("Give me a sentence and I'll reverse it: ")
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    print(reverse_sentence)


sentence_reverse()


def fullout_sentnce_reverser():
    i = 0
    word = input("Type in a sentence ")
    characters = list(word)
    for _ in characters:
        list.append(characters[i-1])
        i -= 1
    print(list)


fullout_sentnce_reverser()
