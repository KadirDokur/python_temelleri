# error handling

try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except (ZeroDivisionError,ValueError) as e:
    print('yanlış bilgi girdiniz!')
    print(e)



try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except:
    print('yanlış bilgi girdiniz!')



while True:
    try:
        x = int (input('x: '))
        y = int (input('y: '))
        print(x/y)
    except (ZeroDivisionError,ValueError) as e:
        print('Yanlış bilgi girdiniz!')
        print(e)
    else:
        print('alles gut')
        break
    finally:
        print('try exception sonlandı')