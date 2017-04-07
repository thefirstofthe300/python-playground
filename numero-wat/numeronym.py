alphabet_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = {i: 1 for i in alphabet_str}

def listify_word_file(filename):
  file_obj = open(filename, 'r').read()
  word_list = file_obj.split("\n")
  return word_list

def parse_numeronym(numeronym):
  parsed_numeronym = []
  current_pos = 0
  while alphabet.get(numeronym[current_pos]) == 1:
    parsed_numeronym.append(numeronym[current_pos])
    current_pos += 1
  parsed_numeronym.append(int(numeronym[current_pos]))
  current_pos += 1
  parsed_numeronym.append(numeronym[current_pos:])
  return parsed_numeronym

'''
Return length of numeronym's underlying word.

Args:
  numeronym: numeronym to get length
Return:
  int: numeronym length
'''
def get_numeronym_length(numeronym):
  numeronym_len = 0
  for i in numeronym:
    if alphabet.get(i) == 1:
      numeronym_len += 1
    else:
      try:
        number = int(i)
        numeronym_len += number
      except ValueError:
        numeronym_len += 1
        continue
  return numeronym_len

def gen_numeronyms(word, dropped_letter):
  dropped_letters = int(dropped_letter)
  #if len(word) <= dropped_letters:
  #  raise ValueError("Word is too short for number of dropped letters.")
  remaining_letters = len(word) - dropped_letters
  numeronyms = []
  for i in range(remaining_letters):
    numeronym = []
    numeronym.append(word[:i + 1])
    numeronym.append(int(dropped_letters))
    if (dropped_letters + 1) == len(word):
      numeronym.append("")
    else:
      numeronym.append(word[i + dropped_letters])
    numeronyms.append(numeronym)
  return numeronyms



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
  numeronym = parse_numeronym(numeronym)
  numeronym_len = get_numeronym_length(numeronym)
  for i in numeronym:
    if i == "'":
      return False
  word_short_list = [word for word in word_list if len(word) == numeronym_len and numeronym[0] == word[0]]
  print(word_short_list)
  for i in word_short_list:
    compare = gen_numeronyms(i, numeronym[1])
    for i in compare:
      if numeronym == i:
        return False
  return True

print is_valid_numeronym("k9", listify_word_file("/usr/share/dict/words"))