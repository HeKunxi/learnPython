# 默认参数
def pow(x, n = 2):
	s = 1;
	while n > 0:
		s *= x
		n -= 1
	return s

print(pow(2))
print(pow(4, 4))

# 