list = [1, 2, 3, 4, 5, 6, 7];
print (list[0]);
print (list[3]);
print (len(list));

for i in range (0, len(list), 1):
  print (list[i], end=" ");

#sum
print ()
sum = 0;
for i in range (0, len(list), 1):
  sum = sum + list[i];
print (sum);