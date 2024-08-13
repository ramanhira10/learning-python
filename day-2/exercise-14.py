def table (i, n):
  if (i <= 10):
    print (str(n), " x ", str(i), " = ", n * i);
    table (i + 1, n);

table(1, 5);