def revrse(n):
  if (n > 0):
    print (n % 10, end="");
    revrse(n//10);

revrse(1924);