from kutuphane import *

print("""
Kütüphane Programına Hoş Geldiniz.
İşlemler:
1- Kitapları Göster
2- Kitap Sorgula
3- Kitap Ekle
4- Kitap Sil
5- Baskı Yükselt

Çıkmak için 'q' ya basın.

""")

kutuphane = Kutuphane()

while True:
    islem = input("İşlem Seçiniz: ")
    if islem == "q":
        print("Program Sonlandırılıyor.")
        print("Yine Bekleriz")
        break
    elif islem == "1":
        kutuphane.kitaplari_goster()
    elif islem == "2":
        isim = input("Hangi Kitabı İstiyorsunuz ?: ")
        print("Kitap Sorgulanıyor.")
        time.sleep(2)
        kutuphane.kitap_sorgula(isim)
    elif islem == "3":
        isim = input("Kitabın Adı: ")
        yazar = input("Yazarın Adı: ")
        yayinevi = input("Yayınevi: ")
        tur = input("Tür: ")
        baski = int(input("Baskı: "))
        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap Ekleniyor.")
        time.sleep(2)
        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi.")
    elif islem == "4":
        isim = input("Hangi Kitabı Silmek İstiyorsunuz?: ")
        cevap = input("Emin Misiniz ? (E/H): ")
        if(cevap == "E"):
            print("Kitap Siliniyor")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap Silindi.")
    elif islem == "5":
        isim = input("Hangi Kitabın Baskısını Yükseltmek İstiyorsunuz?: ")
        print("Baskı Yükseltiliyor")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Baskı Yükseltildi.")
    else:
        print("İşlem Geçersiz.")

 