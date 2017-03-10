
def splitting_words(word, words):
    words_dict = {key: True for key in words}
    for x in range(len(word)):
        if words_dict.get(word[:x]) and words_dict.get(word[x:]):
            return True
    return False