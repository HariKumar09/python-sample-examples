def mutate(word):
    out_list = []

    letters = 'abcdefghijklmnopqrstuvwxyz'
    # insert a character
    for i in range(len(word) + 1):
        for j in range(26):
            out_list.append(word[:i] + letters[j] + word[i:])

    # deleting a character
    for i in range(len(word)):
        out_list.append(word[:i] + word[i + 1:])

    # replace a character
    for i in range(len(word)):
        for j in range(26):
            out_list.append(word[:i] + letters[j] + word[i + 1:])

    # swapping a characters
    current_word = []
    out_word = ''
    for i in range(len(word) - 1):
        for j in range(i + 1, len(word)):
            current_word = []
            for symbol in word:
                current_word.append(symbol)
            current_word[i], current_word[j] = current_word[j], current_word[i]
            for symbol in current_word:
                out_word += symbol
            out_list.append(out_word)
            out_word = ''
            return out_list
