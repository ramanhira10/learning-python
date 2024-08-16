def linear_search (list, n, key):
  for i in range (0, n):
    if (list[i] == key):
      return i;
  return -1

list = [12, 4, 3, 5, 4, 6, 44, 7];
n = len(list);
key = 5;
res = linear_search(list, n, key);
if (res == -1):
  print ("element not found");
else:
  print ("element found at: ", res);