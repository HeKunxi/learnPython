def move(n, a, b, c):
	if n == 2:
		print(a, '-->', b)
		print(a, '-->', c)
		print(b, '-->', c)
		return
	move(n - 1, a, c, b)
	print(a, '-->', c)
	move(n - 1, b, a, c)
	
move(3, 'a', 'b', 'c')