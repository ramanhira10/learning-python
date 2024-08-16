# find the sum of diagonal elements
list = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
sum = 0;
for i in range (0, 3, 1):
  for j in range (0, 3, 1):
    if (i == j):
      sum = sum + list[i][j];
print (sum)