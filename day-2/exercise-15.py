def show (k, n):
  if ( n <= 5):
    show1 (k, n);
    print ();
    show (k, n + 1);

def show1 (k, n):
    if (n == 0):
      return;
    else:
      print(k, end=" ");
      show1(k + 1, n - 1);

show(1, 1);
