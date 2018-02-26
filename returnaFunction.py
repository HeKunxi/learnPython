def lazy_sum(*args):
	def sum():
		n = 0
		for x in args:
			n += x
		return n
	return sum

sum = lazy_sum(1,3,5)
print('sum',sum())

# closure
def count():
	fs = []
	for i in range(4):
		def f():
			return i * i
		fs.append(f)
	return fs
f0, f1, f2, f3 = count()
print(f0())
print(f1())
print(f2())
print(f3())
# they are same

def count2():
	fs = []
	for i in range(4):
		def d(x):
			def g():
				return x * x
			return g
		fs.append(d(i))
	return fs
f0, f1, f2, f3 = count2()
print(f0())
print(f1())
print(f2())
print(f3())

def createCounter():
	n = 0
	def counter():
		nonlocal n
		n = n + 1
		return n
	return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')