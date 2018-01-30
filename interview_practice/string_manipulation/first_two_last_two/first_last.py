def first_last(string):
  counter = 0
  sanitized_string = []
  for i in range(len(string)):
    if string[i].isalpha():
      counter += 1
      sanitized_string.append(string[i])
  if counter < 4:
    return ''
  else:
    return ''.join(sanitized_string[0:2]) + ''.join(sanitized_string[-2:])