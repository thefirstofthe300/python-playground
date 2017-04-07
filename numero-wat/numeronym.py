alphabet_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = {i: 1 for i in alphabet_str}

def listify_word_file(filename):
  file_obj = open(filename, 'r').read()
  word_list = file_obj.split("\n")
  return word_list

def parse_numeronym(numeronym):
  parsed_numeronym = []
  offset = 0

  for i in range(len(numeronym)):
    if alphabet.get(numeronym[i]):
      parsed_numeronym.append((numeronym[i], (i + offset)))
    else:
      try:
        offset = int(numeronym[i])
      except:
        continue

  print "parse_numeronym:", parsed_numeronym
  return parsed_numeronym

def get_numeronym_length(numeronym):
  length = 0
  for letter in numeronym:
    if alphabet.get(letter) == 1:
      length += 1
    else:
      if type(letter) == int:
        length += letter
  return length


def compare_word_to_numeronym(word, numeronym):
  if type(numeronym[0]) != tuple:
    numeronym = parse_numeronym(numeronym)
  for letter_pos in numeronym:
    if letter_pos[0] == word[letter_pos[1]]:
      continue
    else:
      return False
  return True

'''
Determine if, given a dictionary of words, the numeronym is valid for that group
or words

Args:
  numeronym: numeronym to validate
  word_list: list of words to validate against
Return:
  boolean:
'''
def is_valid_numeronym(numeronym, word_list):
  numeronym_len = get_numeronym_length(numeronym)
  word_short_list = [word for word in word_list if len(word) == numeronym_len and numeronym[0] == word[0]]
  parsed_numeronym = parse_numeronym(numeronym)
  for word in word_list:
    print "is_valid_numeronym:", [word, numeronym, compare_word_to_numeronym(word, numeronym)]
    if compare_word_to_numeronym(word, numeronym):
      return False
  return True
