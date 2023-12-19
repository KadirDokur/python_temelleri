# 1-"Cenk" ismini listenin sonuna ekleyiniz.
# 2-"Sena" değerini listenin başına ekleyiniz.
# 3-"Deniz" ismini listeden siliniz.
# 4-"Hakan" isminin indeksi nedir ?
# 5-"Ali" listenin bir elemanı mıdır ?
# 6- Liste elemanlarını ters çevirin.
# 7- Liste elemanlarını alfabetik olarak sıralayınız.
# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
# 9- str ="Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
# 11- years dizisinde kaç tane 1998 değeri vardır ?
# 12- years dizisinin tüm elemanlarını siliniz.
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1-"Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)

# 2-"Sena" değerini listenin başına ekleyiniz
names.insert(0,'Sena')
print(names)
names.insert(len(names),'Mehmet') # sona eklemek için alternatif yöntem
print(names)

# 3-"Deniz" ismini listeden siliniz.
names.remove('Deniz')
print(names)

# 4-"Hakan" isminin indeksi nedir ?
index = names.index('Hakan')
print(index)

# 5-"Ali" listenin bir elemanı mıdır ?
print('Ali' in names)
print(names.index('Ali')) # -1 den farklı bir değer geliyorsa vardır gelmiyorsa yoktur

# 6- Liste elemanlarını ters çevirin.
names.reverse()
print(names)

# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names) #sort() value return etmez bu yüzden print dışında yapılır
print(sorted(names)) # print içerisinde kullanmak için alternatif

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years) #sort() value return etmez bu yüzden print dışında yapılır
print(sorted(years)) # print içerisinde kullanmak için alternatif

# 9- str ="Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
str = 'Chevrolet, Dacia'
result = str.split(',')
print(result)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
print(min(years))
print(max(years))

# 11- years dizisinde kaç tane 1998 değeri vardır ?
print(years.count(1998))

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []

marka = input('marka : ')
markalar.append(marka)

marka = input('marka : ')
markalar.append(marka)

marka = input('marka : ')
markalar.append(marka)
print(markalar)