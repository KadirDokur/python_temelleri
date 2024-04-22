# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# kullanımı : open(dosya_adı,dosya_erişim_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

#"w" (Write) yazma modu. Dosyayı konumda oluşturur.
#   ** Dosya içeriğini her defasında üstüne yazar

# file = open("newfile.txt","w")
# file = open("C:/users/Nith/desktop/newfile.txt","w")
# file.close()

#file = open(newfile.txt,"w",encoding='utf-8')
#file.write("Piotr Knop")
#file.close()

#"a" (Append) ekleme. Dosya konumda yoksa oluşturur
# file = open("newfile.txt","a",encoding='utf-8')
# file.write("\nPiotr Knop")
# file.write("Piotr Knop\n")
# file.write("Celil Hancı\n")
# file.write("Tobias Reaper\n")
# file.close()

#"x" (Create) oluşturma. Dosya zaten varsa hata verir
# file = open("newfile.txt","a",encoding='utf-8')

#"r" (Read) okuma. Dosya yoksa hata verir