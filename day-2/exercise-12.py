# A program to reverse the digits of given number
def reverse(n):
  r = 0;
  while (n > 0):
    r = (r * 10 + n % 10);
    n = n / 10;
  print (r);

reverse(1043);