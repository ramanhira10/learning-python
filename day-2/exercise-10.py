for i in range(1, 6, 1):
  for j in range (1, i + 1, 1):
    print(j, end="");
  for j in range (1, (12 - 2 * i), 1):
    print("-", end="");
  for j in range (1, i + 1, 1):
    print (j, end="");
  print();