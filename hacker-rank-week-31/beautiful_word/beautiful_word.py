'''My solution to https://www.hackerrank.com/contests/w31/challenges/beautiful-word'''

VOWELS = {vowel: 1 for vowel in "aeiouy"}

'''Returns yes if the word is beautiful, no if not

A beautiful word is defined as one in which a vowel (a,e,i,o,u,y in this case)
does not appear next to another vowel and no consonant is repeated.

Args:
  word: string to test for beauty
Return:
  String "Yes" or "No"
'''
def is_beautiful_word(word):
  for i in range(1, len(word)):
    if word[i].lower() == word[i - 1].lower():
      return 'No'
    elif VOWELS.get(word[i]) == 1 and VOWELS.get(word[i - 1]) == 1:
      return 'No'
  return 'Yes'
