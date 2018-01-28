L = [x * x for x in range(10)]
print(L)

L = [x * x for x in range(1, 10) if x % 2 == 0]
print(L)

print([m + n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')])
print(m + n for m in 'ABC' for n in 'XYZ') # in fact it's a generator
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print(d.items())
print([k + '=' + v for k, v in d.items() ])

L = ['Hello', 'World', 'IBM', 'Apple', 18]
print([s.lower() for s in L if isinstance(s, str)])