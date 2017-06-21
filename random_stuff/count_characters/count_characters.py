def count_characters(string):
  counted = {}
  for character in string:
    character = character.lower()
    if character.isalpha():
      if character not in counted:
        counted[character] = 1
      else:
        counted[character] += 1

  return counted