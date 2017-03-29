alphabet_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = {i: 1 for i in alphabet_str}

def listify_word_file(filename):
  file_obj = open(filename, 'r').read()
  word_list = file_obj.split("\n")
  return word_list

def get_numeronym_length(numeronym):
  numeronym_len = 0
  for i in numeronym:
    if alphabet.get(i) == 1:
      numeronym_len += 1
    else:
      try:
        number = int(i)
        print number
        numeronym_len += number
      except ValueError:
        continue
  return numeronym_len

def is_valid_numeronym(numeronym, word_list):
  numeronym_len = get_numeronym_length(numeronym)
  for i in numeronym:
    if i == "'":
      return False
  word_short_list = [word for word in word_list if len(word) == numeronym_len and numeronym[0] == word[0]]
  return word_short_list

print is_valid_numeronym("k9", listify_word_file("/usr/share/dict/words"))