#example no.1 :
#****************************************
def count(start=0, step=1):
    n = start
    while n<100:
        yield n
        n += step
print(list(count(1,23)))

#****************************************
#example no.2 :
#****************************************
from itertools import count

for number in count(start=1, step=2):
	if number > 10:
		break
	print(number)

#****************************************
#example no.3 :
#****************************************

import itertools

print("Printing the numbers repeatedly : ")
print(list(itertools.repeat(25, 4)))

#****************************************
#example no.4 :
#****************************************

# import the product function from itertools module
from itertools import product

print("The cartesian product using repeat:")
print(list(product([1, 2], repeat=2)))
print()

print("The cartesian product of the containers:")
print(list(product(['hello', 'hamza'], '3')))
print()

print("The cartesian product of the containers:")
print(list(product('AB', [3, 4])))
