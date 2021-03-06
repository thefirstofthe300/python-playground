def parse_numeronym(numeronym):
  parsed_numeronym = []
  offset = 0

  for i in range(len(numeronym)):
    if numeronym[i].isalpha():
      parsed_numeronym.append((numeronym[i], (i + offset)))
    else:
      try:
        offset = int(numeronym[i])
      except:
        continue

  return parsed_numeronym

def get_numeronym_length(numeronym):
  length = 0
  number_pos = 0
  for x in range(len(numeronym) - 1, -1, -1):
    if numeronym[x].isalpha():
      length += 1
    elif numeronym[x].isdigit():
      length += int(numeronym[x]) * (10 ** number_pos)
      number_pos += 1
  return length


def compare_word_to_numeronym(word, numeronym):
  for letter_pos in numeronym:
    try:
      if letter_pos[0] == word[letter_pos[1]]:
        continue
      else:
        return False
    except IndexError:
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
  counter = 0
  parsed_numeronym = parse_numeronym(numeronym)
  for word in word_list:
    if compare_word_to_numeronym(word, parsed_numeronym):
      counter += 1
      if counter > 1:
        return False
  return True
