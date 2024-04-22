try:
    file = open("newfile.txt","r")
    print(file)
except FileNotFoundError:
    print("Dosya okuma hatası")
finally:
    print("dosya kapandı.")
    file.close()