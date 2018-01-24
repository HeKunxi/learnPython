d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key, ':', d[key])
for value in d.values():
	print(value)

for ch in 'abc':
	print(ch)

for i, ch in enumerate('abc'):
	print(i, ':', ch)

for m, n in [[1,3], ['a', 4.5], [d, 'b']]:
	print(m, '\\', n)