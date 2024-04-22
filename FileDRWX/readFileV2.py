file = open("newfile.txt","r",encoding='utf-8')

content1 = file.read()

print("içerik1")
print(content1)

content2 = file.read()

print("içerik2")
# file = open("newfile.txt","r",encoding='utf-8')
# **** 11. satırda yeni bir okuma işlemi yapılmalıdır ki content1 yazdırıldıktan sonra content2 yazdırılabilsin
print(content2)
file.close()