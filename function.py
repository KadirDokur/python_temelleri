#1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazin.
#2- Kendine gönderilen sinirsiz sayidaki parametreyi bir listeye çeviren fonksiyon yazın
#3- Gönderilen 2 say1 arasindaki tüm asal sayilar1 bulun.
#4- Kendisine gönderilen bir sayinin tam bölenlerini bir liste seklinde döndür

print('--------------1------------------')
def goster(kelime, adet):
    print(kelime * adet)

goster('merhaba\n',10)

print('--------------2------------------')
def cevir(*args):
    liste = []

    for param in args:
        liste.append(param)

    return liste

result = cevir(10,20,30,'Merhaba')
print(result)

print('--------------3------------------')


def asalBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1): #sayi 2 yi de dahil etmek için +1 denildi
        if sayi > 1:
            for i in range(2,sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)

sayi1 = int(input('sayı 1:'))
sayi2 = int(input('sayı 2:'))

asalBul(sayi1, sayi2)

print('--------------4------------------')
def bolenBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if sayi % i == 0:
            tamBolenler.append(i)

    return tamBolenler

print(bolenBul(20))