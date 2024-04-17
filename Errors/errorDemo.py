liste = ["1","2","5a","10b","abc","10","50"]

# 1:Liste elemanları içerisindeki sayıları bulun
for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

# 2:Kullanıcı "q" harfini girmediği sürece her input sayı değeri olsun aksi halde hata yazdırsın
while True:
    sayi = input('sayı:')
    if sayi=='q':
        break

    try:
        result = float(sayi)
        print("Girdiğiniz sayı :", result)
        break
    except ValueError:
        print("Geçersiz sayı!")
        continue


# 3:Girilen parola içerisinde türkçe karakter hatası versin
def checkPass(parola):
    turkce_karakterler ='şçğüöıİ'

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola turkce karakter iceremez!")
        else:
            pass
        
    print("Gecerli parola!")

parola = input('parola:')

try:
    checkPass(parola)
except TypeError as err:
    print(err)

    
# 4:Faktöriyel fonksyionu oluşturup fonksiyona gelen değerler için hata üretin

def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif değer!')
    
    result = 1

    for i in range(1, x+1):
        result *= i

    return result

for x in [5,10,20,-3,'10a']:
    try:
        y =faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)