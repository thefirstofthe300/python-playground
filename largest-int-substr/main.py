def largest_int_substr_sum(array_ints):
  if array_ints == []:
    return 0
  substr_sums = []
  for i in range(len(array_ints)):
    substr_sums.append(array_ints[i])
    for j in array_ints[i + 1:]:
      substr_sums.append(substr_sums[-1] + j)

  return max(substr_sums)