# Calculation of charges on elecricity consumed units
originalConsumedUnits = 500;
totalUnits = originalConsumedUnits;
firstFifty = 50;
nextHundred = 100;
restUnits = 0;

chargesOnUnits = 0;


if (totalUnits > firstFifty):
    totalUnits = totalUnits - firstFifty;
else:
    firstFifty = totalUnits;

if (totalUnits > nextHundred):
    totalUnits = totalUnits - nextHundred;
else:
    nextHundred = totalUnits;

if (totalUnits > 0):
    restUnits = totalUnits;

chargesOnUnits = (firstFifty * 0.5) + (nextHundred * 0.75) + (restUnits * 1.2);

billToPayAfterSurcharge = chargesOnUnits + chargesOnUnits * (0.2);

print(billToPayAfterSurcharge, "is the bill for your calculated (", originalConsumedUnits, ") units");

    
    
