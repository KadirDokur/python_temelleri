file = open("newfile.txt","r",encoding='utf-8')

for i in file:
    print(i,end="")

file.close()