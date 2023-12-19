CelilHesap = {
    'İsim':'Celil Hancı',
    'HesapNo': '123456789',
    'Bakiye':3000
}


def goster(hesap):
    print(f"Hesap Sahibi:{hesap['İsim']}")
    print(f"Hesap Numarası:{hesap['HesapNo']}")
    print(f"Mevcut Bakiye:{hesap['Bakiye']}")

def yatir(hesap,miktar):
    hesap['Bakiye'] += miktar
    print(f"Yeni Bakiye:{hesap['Bakiye']}")

def cek(hesap,miktar):
    hesap['Bakiye'] -= miktar
    print(f"Yeni Bakiye:{hesap['Bakiye']}")
    
while True:
    print("****************************************************************************")
    print("*                                                                          *")
    print("*                         Atm Uygulamasına Hoşgeldiniz                     *")
    print("*                                                                          *")
    print("****************************************************************************")
    print("1 -> Hesabı Görüntüle\n2 -> Para Yatır\n3 -> Para Çek\n4 -> Çıkış yap")
    secim = int(input('Seçiminiz:'))
    if secim == 1:
        goster(CelilHesap)
    elif secim == 2:
        miktar = int(input("Yatirmak istediğiniz miktari girin:"))
        yatir(CelilHesap, miktar)
    elif secim == 3:
        miktar = int(input("Çekmek istediğiniz miktari girin:"))
        cek(CelilHesap,miktar)
    elif secim == 4:
        print("ÇIKIŞ YAPILDI!!!")
        break
    else:
        print("GEÇERSİZ SEÇİM YAPTINIZ!!!")


