def selection_sort(list_in):
  sorted_list = []
  while len(list_in) > 0:
    sorted_list.append(min([x for x in list_in]))
    list_in.remove(sorted_list[-1])

  return sorted_list