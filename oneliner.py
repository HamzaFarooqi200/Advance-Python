#Example no.1
# *********************************************
number = 4
result = "Even" if number % 2 == 0 else "Odd"
print(result) 

#Example no.2
# *********************************************
number=[1,2,3,4,5]
nums=  [num if num%2==0 else -1 for num in number]
print(nums)

#Example no.3
# *********************************************
numbers = [1, 2, 3, 4, 5, 6]
squares_of_evens = [x**2 for x in numbers if x % 2 == 0]
print(squares_of_evens)

#example no.4
# *********************************************
words = ['cat', 'dog', 'elephant', 'fox']
filtered_uppercase = [word.upper() for word in words if len(word) >= 4]
print(filtered_uppercase)
