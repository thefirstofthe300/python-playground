vowels = {vowel: 1 for vowel in "aeiouy"}

def is_beautiful_word(word):
  for i in range(1, len(word)):
    if word[i].lower() == word[i - 1].lower():
      return "No"
    elif vowels.get(word[i]) == 1 and vowels.get(word[i - 1]) == 1:
      return "No"
  return "Yes"
