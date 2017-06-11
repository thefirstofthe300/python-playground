import logging

def insertion_sort(list_in):

  sorted_list = []

  for i in range(len(list_in)):

    if len(sorted_list) == 0:
      sorted_list.append(list_in[i])
      continue

    for j in range(len(sorted_list)):
      if list_in[i] < sorted_list[0]:
        sorted_list.insert(0, list_in[i])
        break
      elif list_in[i] > sorted_list[-1]:
        sorted_list.append(list_in[i])
        break
      elif list_in[i] <= sorted_list[j] and list_in[i] >= sorted_list[j - 1]:
        sorted_list.insert(j, list_in[i])
        break

  return sorted_list