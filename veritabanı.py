import sqlite3
con = sqlite3.connect("Kutuphane.db") #connection açar. db yoksa da oluşturur.

cursor = con.cursor() #imleç oluşturuyor

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit() # sorgunun veri tabanı üzerinde geçerli olması için commit işlemi gerekli.

def veri_Ekle():
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi,sayfa_Sayisi):
    cursor.execute("Insert Into kitaplık VALUES(?,?,?,?)",(isim,yazar,yayinevi,sayfa_Sayisi))
    con.commit()
def Butun_Verileri_Getir():
    cursor.execute("SELECT * FROM kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Bilgileri Yükleniyor.")
    for i in data:
        print(i)
def Bazi_Verileri_Getir():
    cursor.execute("SELECT Isim,Yazar FROM kitaplık")
    data = cursor.fetchall()
    for i in data:
        print(i)
def Secilen_Verileir_Getir(YAYINEVI):
    cursor.execute("Select * From kitaplık where Yayinevi =?",(YAYINEVI,))
    data = cursor.fetchall()
    for i in data:
        print(i)
def Veri_Guncelle(EskiYayinevi,YeniYayinevi):
    cursor.execute("UPDATE kitaplık set Yayinevi = ? where Yayinevi = ?",(YeniYayinevi,EskiYayinevi,))
    con.commit()
def Veri_Sil(yazar):
    cursor.execute("Delete From kitaplık where yazar = ?",(yazar,))
    con.commit()

# isim = input("Kitap İsmi: ")
# yazar = input("Yazar: ")
# yayinevi = input("Yayınevi: ")
# sayfa_Sayisi = int(input("Sayfa Sayısı: "))
# tablo_olustur()
# veri_Ekle()
# veri_ekle2(isim,yazar,yayinevi,sayfa_Sayisi)
# Butun_Verileri_Getir()
# Bazi_Verileri_Getir()
# Secilen_Verileir_Getir("Everest")
# Veri_Guncelle("Doğan Kitap","Everest")
# Veri_Sil("Tess Gerritsen")
con.close() #connection kapatır.


