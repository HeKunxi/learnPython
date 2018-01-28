g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n += 1
	return 'doneaaaa'
print(next(fib(3)))
print(next(fib(3)))
print(next(fib(3)))
print(next(fib(3))) # every time fib(3) is a new generator

f = fib(3)

print(next(f))
print(next(f))
print(next(f))
# print(next(f)) # throw a StopIteration Error with value 'doneaaaa'

for x in fib(6):
	print(x)

# yanghui triangle
print('=============')
def triangles():
	l, l2 = [1], []
	while True:
		yield l
		for i, v in enumerate(l):
			l2.append(l[i] if i == 0 else (l[i] + l[i - 1]))
		l2.append(1)
		l, l2 = l2, []

yanghuit = triangles()

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
