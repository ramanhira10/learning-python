list = [1, 3, 5, 6, 6, 8, 8];

count = 0;
k = 6;
for i in range (0, len(list), 1):
  if (list[i] == k):
    count = count + 1;

print (count);