print(sorted([5,3,6,1,9]))
L = [-1,4,-6,3,-2]
print(sorted(L))
print(sorted(L, key = abs))
L = ['Credit', 'Zoo', 'about', 'bob']
print(sorted(L))
print(sorted(L, key = str.lower))
print(sorted(L, reverse = True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def compareScore(s1):
	return s1[1]
print(sorted(L, key = compareScore))