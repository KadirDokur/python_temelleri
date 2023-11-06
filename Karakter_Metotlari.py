#1 course dizisinde kaç karakter var
#2 'website' içinden www karakterlerini al
#3 'website' içinden com karakterlerini al
#4 'course' dizisinden ilk ve son 15 karakteri al
#5 'course' dizisinin karakterlerini tersten yaz
#6 Verilen değişkenler ile ekrana aşağıdaki ifadeyi yaz
# 'Benim adım Piotr Knop, yaşım 32 ve mesleğim mühendis'

#7 abc ifadesiin yanyana 3 kere yazdırın


website = 'http://www.kadirdokur.com'
course = 'Introduction to Python Programming'

#1 course dizisinde kaç karakter var
print(len(course))

#2 'website' içinden www karakterlerini al
print(website[7:10],'\n')

#3 'website' içinden com karakterlerini al
print(website[22:25])
print(website[len(website)-3:len(website)],'\n')

#4 'course' dizisinden ilk ve son 15 karakteri al
print(course[0:15])
print(course[:15])
print(course[-15:-1],'\n')

#5 'course' dizisinin karakterlerini tersten yaz
print(course[::-1],'\n')

#6 Verilen değişkenler ile ekrana aşağıdaki ifadeyi yaz
# 'Benim adım Piotr Knop, yaşım 32 ve mesleğim mühendis'

name, surname, age, job = 'Piotr', 'Knop', '32', 'mühendis'

print("Benim adım " + name+ " " + surname+ ", yaşım "+ str(age + " ve mesleğim " + job))
print("Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.".format(name,surname,age,job))
print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.",'\n')

#7 abc ifadesiin yanyana 3 kere yazdırın
print("abc "*3)