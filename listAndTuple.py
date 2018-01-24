classmates = ['bob', 'alice', 'Jack']
print(classmates)
print(len(classmates))
def normalPrint(list):
	print('## normalPrint ##')
	for n in range(0, len(list)):
		print(list[n]) 
normalPrint(classmates)
# use nagetive index to access the item from the opposite direction
def reversePrint(list):
	print('## reversePrint ##')
	for n in range(-1, -1 - len(list), -1):
		print(list[n]) 
reversePrint(classmates)
#append
classmates.append('Peter')
reversePrint(classmates)

#insert
classmates.insert(1, 'Mike')
normalPrint(classmates)

#pop,like a stack
classmates.pop()
normalPrint(classmates)

classmates.pop(1)
normalPrint(classmates)

# empty tuple
t = ()
# tuple with only one item
t = (1,)
print(t)
t = (1,3,5,6,7)
print(t)
for x in t:
	print(x)