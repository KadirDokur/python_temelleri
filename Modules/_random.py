import random

rand = random.random() #0.0- 1.0
rand = random.random() *100
rand = int(random.uniform(10,100)) #type conversion
rand = random.randint(1,100) #without conversion

print(rand)

greetings = 'hello there'
names = ['Tobias','Reaper','Celil','Hanci']


result = random.choice(names) #yields random member
# result = names[random.randint(0,len(names)-1)] // another but longer
print(result)

result = random.choice(greetings)
# yields random letter from the string
print(result)

liste = list(range(10))
random.shuffle(liste)
# This method changes the original list, it does not return a new list.
print(liste)

list2 = range(100)
result = random.sample(list2,3)
# returns 3 different samples from the given list
print(result)
print("-------------")

result = random.sample(greetings,5)
print("Sample from the string =\"Hello World\"")
print(result)
print("-------------")
print("Sample from the \"names\"=[Tobias,Reaper,Celil,Hanci]")
result = random.sample(names,3)
print(result)