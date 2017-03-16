def largest_int_substr_sum(array_ints):
  if array_ints == []:
    return 0
  substr_sums = []
  for i in range(len(array_ints)):
    print "array_ints[i] ==", array_ints[i]
    substr_sums.append(array_ints[i])
    print "Appended array_ints[i]"
    for j in array_ints[i + 1:]:
      print "j ==", j
      substr_sums.append(array_ints[i] + j)
      print "Appended array_ints[i] + j", array_ints[i] + j

  print substr_sums
  return max(substr_sums)