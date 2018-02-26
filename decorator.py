def log(func):
	def wrapper(*args, **kw):
		print('call %s()' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('now!')

now()

def log2(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log2('2222')
def now2():
	print('now2!!!')

now2()
print(now2.__name__) # it's wrapper

# some code depends on function's name, so to decorate a function right
import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s()' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('now!!!')

now()
print(now.__name__) # it's 'now'

import time

def profiler(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		start = time.time()
		result = func(*args, **kw)
		print('function costs %f seconds' % (time.time() -start))
		return result
	return wrapper



# 测试
@profiler
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@profiler
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

def log(func):
	if callable(func):
		def wrapper(*args, **kw):
			print('call %s()' % func.__name__)
			return func(*args, **kw)
		return wrapper
	else:
		def decorator(func2):
			def wrapper(*args, **kw):
				print('%s %s():' % (func, func2.__name__))
				return func2(*args, **kw)
			return wrapper
		return decorator
		

@log('ff')
def now():
	print('now!!!')

now()	