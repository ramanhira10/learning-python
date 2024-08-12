# A program to find the second largest number
a = 15;
b = 6;
c = 10;

if ((a > b and a < c) or (a < b and a > c)):
    print(a, "(a) is the second largest number");
elif ((b > a and b < c) or (b < a and b > c)):
    print (b, "(b) is the second largest number");
else:
    print(c,"(c) is the second largest number");
