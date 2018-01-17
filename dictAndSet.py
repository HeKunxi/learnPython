d = {'Micheal': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Bob'])
d['Tracy'] = 70
print(d['Tracy'])
d['Fuck'] = 'Foo'
print(d['Fuck'])

print('Hi' in d)
print('Fuck' in d)

# the get Method
print(d.get('Fuck'))
print('')
print(d.get('Hi'))
print(d.get('Hi', d))
d.pop('Fuck')
print(d.get('Fuck'))
# tuple can be the key
d[(1,2)]=2
# list cannot
# d[[1,2]]=2

'''
Set
'''
# var = set(list)
s = set([1,2,3])
print(s)
s = set([1,2,3,3,5])
print(s)
s.add(4)
print(s)
s.add(5)
print(s)
s.remove(5)
print(s)
# intersection
s2 = set([1,3,5,7,9])
print(s & s2)
# union
print(s | s2)
print(True & False)
