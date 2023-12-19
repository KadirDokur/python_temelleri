numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a','g', 's', 'b', 'y', 'a', 's']

print(min(numbers))
print(max(numbers))
print(max(letters))
print(min(letters))

print (numbers[3:6]) # 3. indexten 6. indexe kadarkileri göster
print(numbers[:3]) # 3. indexe kadar göster
print(numbers[4:]) # 4. indexten itibaren göster

numbers [4] = 40 # 4. indexi 40 yap
print(numbers)

numbers.append(49) # listeye ekler
numbers.append(59)
numbers.insert(3,78) # istenilen indexten itibaren ekler
numbers.insert(-1,52) # en sonki indexin önüne ekler

print(numbers)

numbers.pop() # en sondaki değeri siler
print(numbers) 
numbers.pop(0) # ilk indexi siler
numbers.pop(-1) # son indexi siler
numbers.remove(49) # silmek istenen eleman silinir
print(numbers)

numbers.sort() # sıralama yapar
print(numbers)
letters.sort()
print(letters)
numbers.reverse() # tersine çevirir
print(numbers)
letters.reverse()
print(letters)

print(numbers.count(10))
print(letters.count('a'))

numbers.clear() # listeyi boşaltır
print(numbers)
