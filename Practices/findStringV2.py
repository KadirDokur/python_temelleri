# Bu program bir dizi içerisindeki istenilen kelimeyi bulur ve indexiyle beraber ekrana yazdırır.


def find(array,word):
    store = []
    for index,item in enumerate(array):
        if (item==word):
            store.append(index+1)

    if len(store) == 0:
        print('Aranılan kelime dizde yok!')  
    else:      
        print(f'{word} is present at indexes {store}')
            
        

words = ['Merhaba','benim','adım','piotr','knopp',
         'Merhaba','benim','adım','piotr','knopp',
         'Merhaba','benim','adım','piotr','knopp',
         'Merhaba','benim','adım','piotr','knopp',
         'Merhaba','benim','adım','piotr','knopp',
         'Merhaba','benim','adım','piotr','knopp']


find(words,"piotr")

