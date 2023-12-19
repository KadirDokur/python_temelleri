
print("Fizz Buzz using while loop")

i = 1
while (i<100):
    if (i % 3 == 0 and i % 5 == 0):
        print("fizzbuzz")
    elif (i % 3 == 0):
        print("fizz")
    elif (i % 5 == 0):
        print("buzz")
    else:
        print(i)
    i += 1

print("Fizz Buzz using for loop")
for i in range(1,100):
    if (i % 3 == 0 and i % 5 == 0):
        print("fizzbuzz")
    elif (i % 3 == 0):
        print("fizz")
    elif (i % 5 == 0):
        print("buzz")
    else:
        print(i)