list = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
list1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
list2 = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
];

for i in range (0, 3, 1):
  for j in range (0, 3, 1):
    list2[i][j] = list[i][j] + list1[i][j];

for i in range (0, 3, 1):
  for j in range (0, 3, 1):
    print (list2[i][j], end=" ");
  print();