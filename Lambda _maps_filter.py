#example no.1
add_ten = lambda x: x + 10
print(add_ten(5))

#**************************************************
#example no.2

pairs = [(3, 'three'),(1, 'one'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

#**************************************************
#example no.3

words = ['hello', 'Hamza']
upper_words = map(lambda s: s.upper(), words)
print(list(upper_words))

#**************************************************
#example no.4

list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_lists = map(lambda x, y: x + y, list1, list2)
print(list(sum_lists)) 

#**************************************************
#example no.5

words = ['cat', 'elephant', 'dog', 'giraffe']
long_words = filter(lambda s: len(s) > 3, words)
print(list(long_words))

