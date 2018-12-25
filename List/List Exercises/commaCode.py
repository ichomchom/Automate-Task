spam = ['apples', 'bananas', 'tofu', 'cats']
aye = [' 1','2','3','4','5','56','6','7','8']

def comma(list):
	for i in range(len(list) - 1):
		print(list[i], end =', ') 
		if len(list) - 2 == i:
			print('and '+ list[i + 1])
comma(spam)
comma(aye)
