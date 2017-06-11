def is_anagram(string_1, string_2):
  string_1 = sorted([x for x in string_1[:] if x.lower().isalpha()])
  string_2 = sorted([x.lower() for x in string_2[:] if x.lower().isalpha()])
  if string_1 == string_2:
    return True
  return False