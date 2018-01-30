def quick_sort(list_in):
   sorted_list = list_in

   if len(list_in) <= 1:
      return list_in

   pivot = list_in[len(list_in) / 2]

   list_in.remove(pivot)

   first = quick_sort([x for x in list_in if x <= pivot])
   second = quick_sort([x for x in list_in if x > pivot])

   sorted_list = first + [pivot] + second

   return sorted_list
