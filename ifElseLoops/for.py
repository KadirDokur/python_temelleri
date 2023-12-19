sayilar = [1,3,5,7,9,12,19,21]

#1- Sayilar listesindeki hangi sayilar 3'ün katıdır ?
#2- Sayilar listesindeki sayilarin toplamı kaçtır ?
#3- Sayilar listesindeki tek sayiların karesini alınız.

print('--------------------------1------------------------------')
for i in sayilar:
    if (i % 3 == 0):
        print(i)

print('--------------------------2------------------------------')
toplam = 0
for i in sayilar:
    toplam += i
print(toplam)

print('--------------------------3------------------------------')
for index,item in enumerate(sayilar):
    if item % 2 ==1:
        print(f'{index+1}.tek sayı:{item}, karesi ={pow(item,2)}')

städte = ['Kocaeli','İstanbul','Ankara','İzmir','Van']

#4- Şehirlerden hangileri en fazla 5 karakterlidir ?

#--------------------------4------------------------------
for i in städte:
    if len(i) <= 5:
        print(i)

urunler = [
     {'name': 'samsung S6', 'price':'3000'},
     {'name': 'samsung S7', 'price':'4000'},
     {'name': 'samsung S8', 'price':'5000'},
     {'name': 'samsung S9', 'price':'6000'},
     {'name': 'samsung S10', 'price':'7000'},
]


#5- Ürünlerden fiyatı en fazla 5000 olanları göster
print('--------------------------5------------------------------')
toplam =0
for urun in urunler:
    fiyat = int((urun['price']))
    toplam += fiyat
print(toplam)

#6- Ürünlerden fiyatı en fazla 5000 olanları göster
print('--------------------------6------------------------------')

for urun in urunler:
     if (int(urun['price']) <= 5000):
          print(urun['name'])
    