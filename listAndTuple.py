classmates = ['bob', 'alice', 'Jack']
print(classmates)
print(len(classmates))
for n in [0,1,2]:
	print(classmates[n])

# use nagetive index to access the item from the opposite direction
def reversePrint(list, len):
	print('## reversePrint ##')
	for n in range(-1, -1 - len, -1):
		print(list[n]) 
reversePrint(classmates, len(classmates))
#append
classmates.append('Peter')
reversePrint(classmates, len(classmates))