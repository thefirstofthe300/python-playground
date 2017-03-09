words = ["hello", "world", "what", "is", "up"]
words_dict = {key: True for key in words}

print words_dict

def splitting_words(word, words):
    for x in range(len(word)):
        if words_dict.get(word[:x]) and words_dict.get(word[x:]):
            return True
    return False
    
print splitting_words("helloworld", words_dict)