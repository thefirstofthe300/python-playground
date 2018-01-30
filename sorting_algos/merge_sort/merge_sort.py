def merge_sort(list_in):
  sorted_list = []

  first_half = list_in[:len(list_in) / 2]
  second_half = list_in[len(list_in) / 2:]

  if len(list_in) > 2:

    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)

  while len(first_half) > 0 or len(second_half) > 0:
    if len(first_half) == 0 and len(second_half) > 0:
      sorted_list.extend(second_half)
      second_half = []
    elif len(second_half) == 0 and len(first_half) > 0:
      sorted_list.extend(first_half)
      first_half = []
    elif len(second_half) == 0 and len(first_half) == 0:
      break
    elif first_half[0] < second_half[0]:
      sorted_list.append(first_half[0])
      first_half.remove(sorted_list[-1])
    else:
      sorted_list.append(second_half[0])
      second_half.remove(sorted_list[-1])

  return sorted_list
