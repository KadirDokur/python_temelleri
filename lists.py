# 1-"Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
# 2- Liste Kaç elemanlıdır ?
# 3 Listenin ilk ve son elemanı nedir?
# 4-Mazda değerini Toyota ile değiştirin.
# 5-Mercedes listenin bir elemanı mıdır
# 6- Listenin -2 indeksindeki değer nedir ?
# 7- listenin ilk 3 elemanını alın
# 8- Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
# 10- Listenin son elemanını silin.
# 11- Liste elemanlarını tersten yazdırınız.

# 12- Aşağıdaki verileri bir liste içinde saklayınız.
    # studentA: Yiğit Bilgi 2010, (70,60,70) 
    # studentB: Sena Turan 1999, (80,80,70) 
    # studentC: Ahmet Turan 1998, (80,70,90)


# 1-"Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ['BMW', 'Mercedes', 'Opel', 'Mazda']

# 2- Liste Kaç elemanlıdır ?
result = len(arabalar)
print(result)

# 3 Listenin ilk ve son elemanı nedir?
print(arabalar[0])
print(arabalar[3])
print(arabalar[-1])

# 4-Mazda değerini Toyota ile değiştirin.
arabalar[-1] = 'Toyota'
print(arabalar)

# 5-Mercedes listenin bir elemanı mıdır
print('Mercedes' in arabalar)

# 6- Listenin -2 indeksindeki değer nedir ?
print(arabalar[-2])

# 7- listenin ilk 3 elemanını alın
print(arabalar[0:3])
print(arabalar[:3])
print(arabalar[-2:])

# 8- Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = ['Toyota','Renault']
print(arabalar)

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
arabalar = arabalar + ['Audi', 'Nissan']
print(arabalar)

# 10- Listenin son elemanını silin
del arabalar[-1]
print(arabalar)

# 11- Liste elemanlarını tersten yazdırınız.
print(arabalar[::-1])

#  12- Aşağıdaki verileri bir liste içinde saklayınız.
#     studentA: Yiğit Bilgi 2010, (70,60,70) 
#     studentB: Sena Turan 1999, (80,80,70) 
#     studentC: Ahmet Turan 1998, (80,70,90)

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet', 'Turan',1998,[80,70,90]]

#13 liste elemanlarını ekrana yazdırın
print(studentA[0])
print(studentB[1])
print(studentC[3][1])

print(f'{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}')