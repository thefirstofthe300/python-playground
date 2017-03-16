def splitting_words(word, words):
    words_dict = {key: True for key in words}
    size = len(word)
    if size == 0:
        return False
    indexes = [False for x in range(size + 1)]
    for x in range(len(word)):
        if indexes[x] == False and words_dict.get(word[:x]):
            indexes[x] = True

        if indexes[x] == True:
            if x == size:
                return True

            for y in range(x, size + 1):
                if indexes[y] == False and words_dict.get(word[x:y]):
                    indexes[y] = True

                if y == size and indexes[y] == True:
                    return True


    return False
