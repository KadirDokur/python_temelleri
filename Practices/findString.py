# Bu program bir dizi içerisindeki istenilen kelimeyi bulur ve indexiyle beraber ekrana yazdırır.


def find(array,word):
    store = {}
    for index,item in enumerate(array):
        if (item==word):
            store[index] = word

    if len(store) == 0:
        print('Aranılan kelime dizde yok!')  
    else:      
        for index,word in store.items():
            print(f'{word} is at {index+1}. index')
                  
words = ['Merhaba','benim','adım','piotr','knopp',
         'Merhaba','benim','adım','piotr','knopp',
         'Merhaba','benim','adım','piotr','knopp',
         'Merhaba','benim','adım','piotr','knopp',
         'Merhaba','benim','adım','piotr','knopp',
         'Merhaba','benim','adım','piotr','knopp']


find(words,"piotr")


