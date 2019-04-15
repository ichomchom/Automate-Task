spam = {'color' : 'red', 'age': 42}
print('print value: ')
for v in spam.values():
	print(v)
print('print key: ')
for k in spam.keys():
	print(k)
print('print items: ')
for i in spam.items():
	print(i)


print('return list: ' )
print(list(spam.keys()))
