def bubble_sort (list):
  for i in range (0, len(list) - 1):
    for j in range (len(list) - 1):
      if (list[j] > list [j + 1]):
        temp = list[j];
        list[j] = list [j + 1];
        list[j + 1] = temp;
  return list;

list = [12, 3, 55, 1, 4, 6];
print (bubble_sort(list));