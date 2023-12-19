sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdirin.
# 2: Baslangiç ve bitis degerlerini kullanicidan alip aradaki sayilari yazdirin.
# 3: 1-100 arasindaki sayiları azalan sekilde yazdirin.
# 4: Kullanicidan alacaginiz 5 sayıyı ekranda sirali bir sekilde yazdirin.
# 5: Kullanicidan alacaginiz sinirs1z ürün bilgisini urunler listesi içinde yazdirin
#    **ürün sayisini kullaniclya sorun.
#    ** dictionary listesi yapis1 (name, price) seklinde olsun.
#    ** ürün ekleme islemi bittiginde ürünleri ekranda while ile listeleyin.

print('------------------------1---------------------')

i = 0

while i < len(sayilar):
     print(sayilar[i])
     i += 1

print('------------------------2---------------------')
bas = int(input('Gebe die erste Zahl ein:'))
son = int(input('Gebe die letzte Zahl ein:'))

i = bas
while i <= son:
    print(i)
    i+=1

print('------------------------3---------------------')
i = 100
while i >= 1:
    print(i)
    i-=1

print('------------------------4---------------------')
i = 1
list = []
while i <= 5:
    list.append(int(input(f'{i}.sayiyi giriniz ')))
    i += 1

list.sort()
print(list)

print('------------------------5---------------------')
urunler = []
adet = int(input('kaç ürün eklemek istiyorsunuz:'))
i = 0
while (i<adet):
    name = input('ürün ismi:')
    price = input('ürün fiyatı:')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1
for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')
