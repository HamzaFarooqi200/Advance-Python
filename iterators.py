print("Example no.1")
print("*********************************")
mytuple = ("2", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print("*********************************")
print("Example no.2")
print("*********************************")
mystr = "Hamza Farooqi"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("*********************************")
print("Example no.3")
print("*********************************")
mytuple = ("hello", "how", "Byeeeeee!")
for x in mytuple:
  print(x) 
print("*********************************")
print("Example no.4")
print("*********************************")
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current

countdown = Countdown(5)
for number in countdown:
    print(number)
