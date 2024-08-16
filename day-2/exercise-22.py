def binary_search (list, n):
  low = 0;
  high = len(list) - 1;
  mid = 0;
  while (low <= high):
    mid = (low + high) // 2;
    if (list[mid] < n):
      low = mid + 1;
    elif list[mid] > n:
      high = mid - 1;
    else:
      return mid;
  return -1;

list = [1, 2, 33, 44, 55, 66, 77, 88];
n = 44;
res = binary_search(list, n);
if (res == -1):
  print ("element not found");
else:
  print ("element found at: ", res);