# 默认参数
def pow(x, n = 2):
	s = 1;
	while n > 0:
		s *= x
		n -= 1
	return s

print(pow(2))
print(pow(4, 4))

# default argument must be immutable
def add_end(L = []):
	L.append('End')
	return L
print(add_end())
print(add_end())

def haha(n = 2):
	n += 1
	return n
print(haha())
print(haha())

# variadic parameter
def calc(*numbers):
	# numbers is a tuple here, numbers.append(2) will throw an error
	sum = 0
	for x in numbers:
		sum += x
	return sum
print(calc(1,3,5))
def calc(a,b,*numbers):
	# numbers is a tuple here, numbers.append(2) will throw an error
	sum = a + b
	for x in numbers:
		sum += x
	return sum
t = (1,5,7)
print(calc(*t)) # use tuple's items in variadic parameter
l = [1,5,7]
print(calc(*l))

# keyword parameter
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
person('fuck', 'hi')
person('fuck', 'hi', city='Beijing')
person('fuck', 'hi', city='Beijing', gender='Male')
d = {'city':'Beijing', 'gender':'Male'}
person('hei', 'you', **d)
# kw is a copy of d, modifying kw will not change d
def person2(name, age, **kw):
	kw['city'] = 'hangzhou'
	person(name, age, **kw)
person2('hei', 'you', **d)
print(d['city'])

# Named keyword parameters
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Cleaner')

def person(name, age, *, city='beijing', job):
    print(name, age, city, job)
person('Jack', 24, job='fuck')

def person(name, age, *numbers, city, job):
    print(name, age, numbers, city, job)

person('Jack', 24, 1,2,3, city='Beijing', job='Cleaner')

def f1(a, b, c=0, *args, city, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'city =', city, 'args =', args, 'kw =', kw)

f1(1, 2, city='Beijing')
args = [1,2,3,4]
kw = {'city' : 'city', 'f1' : 'a', 'f2' : 'b'}
f1(*args, **kw)
