from getpass import getpass
#1 - Girilen 2 sayıdan hangisi büyüktür

#2 - kullanıcıdan vize (%60) ve final (%40) notu alıp ortalama hesaplayınız
#Eğer ortalama 50 ve üstüyse geçti yazdırın

#3 - Girilen bir sayının tek mi çift mi olduğunu yazdırın

#4 - Girilen bir sayının pozitif mi negatif mi olduğunu yazdırın

#5 - Parola ve email bilgisi isteyip doğruluğunu kontrol edin

#------------------------------------------------------- 1
print('Büyük-Küçük')
a = int(input('a: '))
b = int(input('b: '))

result = (a>b)

print(f'a:{a} b:{b} den büyük müdür : {result}')


#-------------------------------------------------------- 2
print('Geçti-Kaldı')
vize = float(input('vize: '))
final = float(input('final: '))

ort = (vize*0.6 + final*0.4)
sonuc = (ort >= 50 and final >= 50)

print(f'Ortalamanız:{ort}, Geçtiniz:{sonuc}')

#----------------------------------------------------------3
print('Tek mi çift mi')
sayi = int(input('sayi: '))
print(sayi % 2 == 0)

#-----------------------------------------------------------4
print('Pozitif-Negatif')
sayi = int(input('sayı:'))
print(f'Girilen sayinin pozitif olma durumu:{sayi>=0}')

#----------------------------------------------------------5
print('Email Doğrulama\n')
email = 'celilhanci@hotmail.com'
password = 'celilhanci123'

girilenMail = input('email: ')
girilenPass = getpass('parola: ')

print(f'Email doğru girildi mi: {email==girilenMail.strip()}\nParola doğru girildi mi: {password==girilenPass}')