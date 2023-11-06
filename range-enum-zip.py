#--------------range-----------------
for item in range(50,100,20):
    print(item)

print(list(range(5,100,20)))

#--------------Enumerate------------
greetings = 'Hello'


for index,item in enumerate(greetings):
    print(f'index: {index+1} letter: {item}')
    
#--------------zip-------------------
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1, list2, list3)))