def show (n):
  if ( n <= 5):
    show (n + 1);
    print (n);

show (1);

# why 5, 4, 3, 2, 1 is printing