# A program to find the smallest number from 5 numbers
a=20;
b=30;
c=40;
d=10;

if (a < b and a < c and a < d):
    print(a, "(a) is the smallest number");
elif (b < a and b < c and b < d):
    print(b, "(b) is the smallest number");
elif (c < a and c < b and c < d):
    print(c, "(c) is the smallest number");
else:
    print(d, "(d) is the smallest number");
