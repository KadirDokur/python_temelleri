#1 ' Hello World ' karakter dizisinin başındaki ve sonundaki boşluk karakterlerini sil
#2 'www.kadirdokur.com' icindeki kadirdokur bilgisi hariç her şeyi sil
#3 'course' dizisinin tüm karakterlerini küçük yap
#4 'website' içinde kaç tane k karakteri var ?
#5 'website' www ile başlayıp bitiyor mu ?
#6 'website' içinde .com var mı ?
#7  'course' içindeki karakterlerin hepsi alfabetik mi ?
#8 'contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekle
#9 'course' dizisinin tüm boşlukarını '-' yap
#10 'Hello World' dizisinin 'World' ifadesini 'There' olarak değiştir
#11 'course' karakter dizisini boşluk karakterlerinden ayır

website = 'http://www.kadirdokur.com'
course = 'Introduction to Python Programming'


#1 ' Hello World ' karakter dizisinin başındaki ve sonundaki boşluk karakterlerini sil
result = ' Hello World '
print(result.strip())       # iki taraftan siler     
print(result.lstrip())      # soldan siler
print(result.rstrip(),'\n') # sağdan siler


#2 'www.kadirdokur.com' icindeki kadirdokur bilgisi hariç her şeyi sil
print(website.strip('/:htp.wcom')) # belirtilen karakterleri sil

#3 'course' dizisinin tüm karakterlerini küçük yap
print(course.lower())
print(course.upper())
print(course.title(),'\n')

#4 'website' içinde kaç tane k karakteri var ?
print(website.count('k'))
print(website.count('www'))
print(website.count('www',0,10),'\n') #0 ile 10. index arasına bakar

#5 'website' www ile başlayıp bitiyor mu ?
print(website.startswith('www'))
print(website.startswith('http'))
print(website.startswith('com') , '\n')

#6 'website' içinde .com var mı ?
print(website.find('com'))          # 22 yazdıracaktır çünkü 'c' nin indexi 22
print(website.find('com',0,10))     # 0 ile 10. karakter arasında arar ve bulamazsa -1 yazdırır
print(course.find('Python'), '\n')  # eğer bulursa ait olduğu index sayısını yazar

#7  'course' içindeki karakterlerin hepsi alfabetik mi ?
print(course.isalpha())
print('Hello'.isalpha())
print(course.isdigit())
print('123'.isdigit(), '\n')

#8 'contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekle
print('Contents'.center(50, '*'))
print('Contents'.ljust(50, '*'))
print('Contents'.rjust(50, '*'), '\n')

#9 'course' dizisinin tüm boşlukarını '-' yap
print(course.replace(' ','-'))
print(course.replace(' ','-',2)) # indexi 0'dan başlayarak 2. indexe kadar olan boşlukları - yap
print(course.replace(' ',''), '\n') # boşlukları sil

#10 'Hello World' dizisinin 'World' ifadesini 'There' olarak değiştir
print(result.replace('World','There'), '\n')

#11 'course' karakter dizisini boşluk karakterlerinden ayır
print(course.split(' '))
