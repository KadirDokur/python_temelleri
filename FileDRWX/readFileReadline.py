file = open("newfile.txt","r",encoding='utf-8')

print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")

liste = file.readlines()
print(liste)

file.close()