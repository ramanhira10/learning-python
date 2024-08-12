# A program to demonstrate the tax calculated on the salary
salary = 9000;
tax = 0;
if (salary >= 12000):
    tax = (salary * (5 / 100));
    print (tax);
elif (salary >= 8000 and salary <= 12000):
    tax = (salary * (3 / 100));
    print (tax);
else:
    print ('tax is none');
