class Library:
    def __init__(self, dosya_adi):
        self.dosya = open(dosya_adi, "a+")

    def __del__(self):
        self.dosya.close()

    def listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        # i, sayfa = 0, 10
        # sayfa_indisi = "c"

        if kitaplar:
            kitap_listesi = []
            # while sayfa_indisi == "c":
            #     print(str(i) + ". sayfada bulunan " + str(sayfa) + "adet kitap:\n")

            i = 0
            for kitap in kitaplar:
                kitap_bilgi = kitap.split(',')
                kitap_listesi.append(f"Kitap Adı: {kitap_bilgi[0]} | Yazar: {kitap_bilgi[1]} | Yayın Tarihi: {kitap_bilgi[2]} | Sayfa Sayısı: {kitap_bilgi[3]}")
                print(kitap_listesi[i])
                i += 1



                # while sayfa_indisi != "c" or sayfa_indisi != "q":
                #     sayfa_indisi = input("sonraki sayfaya gecmek icin: c\n listeden cikmak icin: q\n")
                #     if sayfa_indisi == "c":
                #         sayfa = sayfa + 10
                #         continue
                #     elif sayfa_indisi == "q":
                #         break
                #     else:
                #         print("Gecersiz giris!")
        else:
            print("Kitaplıkta kitap bulunmamaktadır.\n")

        input("Devam etmek için Enter tuşuna basın...")

    def kitap_ekle(self):
        while True:
            baslik = input("Kitabın adını girin: ")
            yazar = input("Kitabin yazarını girin: ")
            yayin_tarihi = input("Kitabın yayın tarihini girin: ")
            sayfalar = input("Kitabın sayfa sayısını girin: ")
            kitap_bilgisi = f"{baslik},{yazar},{yayin_tarihi},{sayfalar}\n"
            tamamdevam = input(f"{kitap_bilgisi}girmek istediğiniz kitap bilgisi doğru ise Y girin, değilse Enter tuşuna basarak bilgileri yeniden girin: ")
            if tamamdevam.upper() == "Y":
                self.dosya.writelines(kitap_bilgisi)
                print("Kitap başarıyla eklendi.")
                input("Devam etmek için Enter tuşuna basın...")
                break
            else:
                continue

    def kitap_sil(self):
        while True:
            baslik = input("\nSilmek istediğiniz kitabın adı: ")
            tamamdevam = input(f"\n{baslik} isimli kitap kaldırılacaktır. Onaylıyor musunuz?\nSilmek için: Y\nFarklı bir kitap silmek için: R\nİşlemi iptal edip menüye dönmek için: M\n")
            if tamamdevam.upper() == "Y":
                self.dosya.seek(0)
                kitaplar = self.dosya.readlines()
                yeni_kitaplik = [kitap for kitap in kitaplar if baslik not in kitap]
                if kitaplar == yeni_kitaplik:
                    print("Bu kitap zaten yok!")
                else:
                    self.dosya.truncate(0)
                    self.dosya.writelines(yeni_kitaplik)
                    print("Kitap başarıyla silindi.")
                break
            elif tamamdevam.upper() == "R":
                continue
            elif tamamdevam.upper() == "M":
                break
            else:
                print("Geçersiz giriş")

    # def remove_book(self):
    #     title_to_remove = input("Enter the title of the book to remove: ")
    #     self.file.seek(0)
    #     books = self.file.readlines()
    #     updated_books = [book for book in books if title_to_remove not in book]
    #     self.file.truncate(0)
    #     self.file.writelines(updated_books)
    #     print(f"Book '{title_to_remove}' successfully removed.")


lib = Library("books.txt")

while True:
    print("\n#### KÜTÜPHANE YÖNETİM SİSTEMİ ####")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitaplıktan Kitap Sil")
    print("Q) Çıkış Yap")

    secim = input("İşlem seçin: ")

    if secim == "1":
        lib.listele()
    elif secim == "2":
        lib.kitap_ekle()
    elif secim == "3":
        lib.kitap_sil()
    elif secim.upper() == "Q":
        break
    else:
        print("Geçersiz giriş. Lütfen geçerli bir işlem seçin.")