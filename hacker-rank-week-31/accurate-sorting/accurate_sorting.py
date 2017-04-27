def is_sortable(in_list):
  sortable = True
  if len(in_list) <= 1:
    return None
  for i in range(1, (len(in_list) - 1), 2):
    print "Subtracting", in_list[i - i], "from", in_list[i]
    if abs(in_list[i] - in_list[i - 1]) == 1 or abs(in_list[i] - in_list[i + 1]):
      continue
    else:
      sortable = False

  if not sortable:
    return N
  return "No"