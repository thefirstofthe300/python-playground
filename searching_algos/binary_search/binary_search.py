from math import ceil

def binary_search(haystack, needle):
  begin_index = 0
  last_index = len(haystack) - 1
  while last_index - begin_index != 1:
    middle_index = last_index - int(ceil((float(last_index) - begin_index) / 2))
    if haystack[begin_index] == needle:
      return (begin_index + 1) #Add one because humans use 1 indexed arrays
    elif haystack[last_index] == needle:
      return (last_index + 1) #Add one for same reason as above
    elif haystack[middle_index] == needle:
      return (middle_index + 1)
    elif haystack[middle_index] <= needle:
      begin_index = middle_index
    else:
      last_index = middle_index

  return -1