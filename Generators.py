#example no.1:
def simpleGeneratorFun1():
    yield 1            
    yield 2            
    yield 3            
 
for value in simpleGeneratorFun1(): 
    print(value)

#example no.2:
def simpleGeneratorFun2():
    yield 1
    yield 2
    yield 3
 

x = simpleGeneratorFun2()

print(next(x))
print(next(x))
print(next(x))

#example no.3:

def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


x = fib(5)

print(next(x)) 
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print("\nUsing for in loop")
for i in fib(5): 
    print(i)
