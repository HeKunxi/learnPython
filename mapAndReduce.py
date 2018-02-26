def f(x):
	return x * x
r = map(f, range(10))
print(list(r))

def r(x, y):
	return x + y
import functools
print(functools.reduce(r, range(10)))

def str2int(s):
	return functools.reduce(lambda x, y : x * 10 + y, map(int, s))
print(str2int('321'))