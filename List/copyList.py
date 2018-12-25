import copy
spam = ['A', 'B', 'C']
cheese = copy.copy(spam)
cheese[1] = 420
print(spam)
print(cheese)
