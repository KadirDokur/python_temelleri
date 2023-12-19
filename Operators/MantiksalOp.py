#1 Girilen bir sayinin 0 ile 100 arasında olup olmadığını kontrol edin

#2 Girilen sayinin pozitif cift bir sayi olup olmadığını kontrol edin

#3 email ve parola bilgileri ile giriş kontrolü yapın

#4- Girilen 3 sayidan en büyüğünü bulun.

#5- Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayın
#Eger ortalama 50 ve üstündeyse geçti degilse kaldı yazdirin.
#a-) Ortalama 50 olsa bile final not en az 50 olmalidir.
#b-) Finalden 70 alindiginda ortalamanin önemi olmasin.

# 6- Kisinin ad, kilo ve boy bilgilerini alip kilo indekslerini hesaplayiniz.
# Formül: (Kilo / boy uzunlugunun karesi)
# Asagidaki tabloya göre kisi hangi gruba girmektedir.
# 0-18.4 =› Zayif
# 18.5-24.9 => Normal
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Sisman (Obez)



print('1. Alıştırma')
sayi = int(input('sayi:'))
print(f'Girilen sayi 0 ile 100 arasında mı:{0<sayi<100}')

#----------------------------------------------------------------------------------
print('\n2. Alıştırma')
sayi = int(input('sayi:'))
print(f'Girilen sayi pozitif bir çift sayı mı:{sayi>0 and sayi%2==0}')

#----------------------------------------------------------------------------------
print('\n3. Alıştırma')
ornekMail = 'kerem@hotmail.com'
ornekParola = '123'

mail = input('Mail adresini giriniz: ')
parola = input('Parola giriniz: ')

print(f'Giriş bilgileri doğru mu : {ornekMail==mail and {ornekParola==parola}}')

#----------------------------------------------------------------------------------
print('\n4.Alıştırma')
a = int(input('1. Sayiyi girin:'))
b = int(input('2. Sayiyi girin:'))
c = int(input('3. Sayiyi girin:'))

print(f'a en büyük sayı mıdır: {a>b and a>c}')
print(f'b en büyük sayı mıdır: {b>a and b>c}')
print(f'c en büyük sayı mıdır: {c>b and c>a}')

#----------------------------------------------------------------------------------
print('\n5.alıştırma')
vize1 = float(input('1. Vize sonucunu giriniz:'))
vize2 = float(input('2. Vize sonucunu giriniz:'))
final = float(input('Final sonucunu giriniz:'))
ort = ((vize1 + vize2)*0.6) + (final*0.4)

print(f'Ortalamanız:{ort}\nGeçme durumu:{((ort>=50 and final>=50) or final>=70)}')

#----------------------------------------------------------------------------------
print('\n6.Alıştırma')
isim = input('İsim Giriniz:')
boy = float(input('Boy giriniz(metre):'))
kilo = float(input('Kilo giriniz(kg):'))

sonuc = ((kilo / (boy**2)))
zayıf = (sonuc > 0 and sonuc <=18.4)
normal = (sonuc >= 18.5 and sonuc <=24.9)
kilolu = (sonuc >= 25 and sonuc <=29.9)
obez = (sonuc >= 30 and sonuc <=34.9)



print(f'BMI index: {sonuc}, zayıf mı:{zayıf}')
print(f'BMI index: {sonuc}, normal mi:{normal}')
print(f'BMI index: {sonuc}, kilolu mu:{kilolu}')
print(f'BMI index: {sonuc}, obez mi:{obez}')


