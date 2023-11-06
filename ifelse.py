import datetime



# 1- Kullanicidan isim, yas ve egitim bilgilerini isteyip ehliyet alabilme
# durumunu kontrol ediniz. Ehliyet alma kosulu en az 18 ve egitim durumu
# lise ya da üniversite olmalidir.

# 2- Bir ögrencinin 2 yazil1 bir sözlü notunu alip hesaplanan ortalamaya göre
# not araligina karsilk gelen not bilgisini yazdiriniz.
# 0 -24 => 0
# 25-44=> 1
# 45-54=> 2
# 55-69=> 3
# 70-84=>4
# 85-100 =≥ 5

# 3- Trafige çıkış tarihi alinan bir aracin servis zamanini asagidaki bilgilere
# göre hesaplayiniz.
# 1. Bakim => 1. yıl
# 2. Bakim => 2. yıl
# 3. Bakim => 3. yıl
# ** Süre hesabini alinan gün, ay, yil bilgisine göre gün bazli hesaplayin:
# ***datetime modülünü kullanmaniz gerekiyor.








#----------------------------------------1-------------------------------------------
# isim = input('İsim:')
# yas = int(input('Yaş:'))

# print('\nEğitim durumunua denk gelen sayiyi seçiniz\n')
# print('1 = İlkokul, 2 = Lise, 3 = Üniversite, 4 = Hiçbiri')
# egitim = int(input('Egitim durumu:'))
# if (egitim == 1):
#     egitim = 'İlkokul'
# elif egitim == 2:
#     egitim = 'Lise'
# elif egitim == 3:
#     egitim = 'Üniversite'
# else:
#     egitim = 0

# print(f'\nİsim:{isim}  Yaş:{yas}  Egitim Durumu:{egitim}')

# if (yas >= 18):
#     if (egitim == 'Lise') or (egitim == 'Üniversite'):
#         print('Ehliyet alabilmek için uygundur!')
#     elif (egitim == 'İlkokul'):
#         print('18 Yaşından büyük ancak eğitim durumu yetersiz!')
# else:
#     print('Ehliyet alabilmek için 18 yaşı doldurulmalıdır!')

#--------------------------------------2---------------------------------------------

# bir = int(input('1. yazılı notunu girin:'))
# iki = int(input('2. yazılı notunu girin:'))
# sozlu = int(input('Sözlü notunu girin:'))
# puan = ...

# ort = float((bir + iki + sozlu) / 3)

# if 0 <= ort and ort <= 24:
#     puan = 0
# elif 25 <=ort and ort<=44:
#     puan = 1
# elif 45 <=ort and ort<=54:
#     puan = 2
# elif 55 <=ort and ort<=69:
#     puan = 3
# elif 70 <=ort and ort<=84:
#     puan = 4
# else:
#     puan = 5

# print(f'Ogrencinin notu:{ort:.2f} Ogrencinin puanı:{puan}')

#--------------------------------------3---------------------------------------------

# tarih = input('Aracın trafiğe çıktığı tarih (2019/8/9): ')
# tarih = tarih.split('/')

# trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# simdi = datetime.datetime.now()
# fark = simdi - trafigeCikis
# days = fark.days

# if days<=365:
#     print('1.servis aralığı')
# elif days >365 and days <= 365*2:
#     print('2.servis aralığı')
# elif days >365*2 and days <= 365*3:
#     print('3.servis aralığı')
# elif days >365*3 and days <= 365*4:
#     print('4.servis aralığı')
# elif days >365*4 and days <= 365*5:
#     print('5.servis aralığı')
# else:
#     print('Hatalı süre')