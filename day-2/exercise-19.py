list = [1, 2, 3, 5, 6, 7, 22];
max = list[0];
min = list[0];

for i in range (1, len(list), 1):
  if (max < list [i]):
    max = list[i];
  if (min > list [i]):
    min = list [i];

print (max);
print (min);