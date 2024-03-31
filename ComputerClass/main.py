import time

class Computer():
    def __init__(self,bilgisayar_durumu = "Kapalı",uygulama_listesi = ["Opera"],ses = 0):
        self.bilgisayar_durumu = bilgisayar_durumu
        self.uygulama_listesi = uygulama_listesi
        self.ses = ses


    def bilgisayari_ac(self):

        if(self.bilgisayar_durumu == "Açık"):
            print("Bilgisayar Zaten Açık.")
        else:
            print("Bilgisayar Açılıyor...")
            time.sleep(1)
            self.bilgisayar_durumu = "Açık"
            print("Hoşgeldiniz...")
    def bilgisayari_kapat(self):
        if(self.bilgisayar_durumu == "Kapalı"):
            print("Bilgisayar Zaten Kapalı.")
        else:
            print("Bilgisayar Kapanıyor...")
            time.sleep(1)
            print("Hoşçakalın...")
            self.bilgisayar_durumu = "Kapalı"

    def uygulama_indir(self,uygulama):
        print("Uygulama İndiriliyor...")
        time.sleep(1)

        self.uygulama_listesi.append(uygulama)
        print("Uygulama İndirildi:", uygulama)
    def ses_ayarlari(self):
       while True:
           cevap = input("\nSES ARTTIR:'>'\nSES AZALT:'<'\nÇIKIŞ:'exit'\n:")
           if (cevap == ">"):
               if (self.ses != 100):
                   self.ses += 1
                   print("\nSES:", self.ses)
           elif (cevap == "<"):
               if (self.ses != 0):
                   self.ses -= 1
                   print("SES:", self.ses)
           elif (cevap == "exit"):
               break
           else:
               print("Hatalı Giriş Yaptınız. Tekrar Deneyin.")

    def __len__(self):
        print(self.uygulama_listesi)
        return len(self.uygulama_listesi)
    def __str__(self):
        print("Bilgisayar Durumu:{}\nBilgisayar Sesi:{}\nBilgisayardaki Uygulamalar:{}".format(self.bilgisayar_durumu,self.ses,self.uygulama_listesi))

    def uygulama_sil(self,uygulama):
        for i in self.uygulama_listesi:
            if(uygulama == i):
                self.uygulama_listesi.remove(i)
                print("Uygulama Silindi:",i)
                break
computer = Computer()
print("""
Bilgisayarına Hoşgeldin!
1.Bilgisayarı Aç
2.Bilgisayarı Kapat
3.Uygulama İndir
4.Ses Ayarları
5.Bilgisayardaki Uygulamalar
6.Uygulama Sil
7.Çıkış

""")

while True:
    işlem = int(input("\nİşleminizi Seçin:"))
    if(işlem == 1):
        computer.bilgisayari_ac()
    elif(işlem==2):
        computer.bilgisayari_kapat()
    elif(işlem == 3):
        uygulamalar = input("İndirmek istediğiniz uygulamaları ',' ile ayırarak yazınız:")
        girilen_uygulamalar = uygulamalar.split(",")
        for i in girilen_uygulamalar:
            computer.uygulama_indir(i)
    elif(işlem == 4):
        computer.ses_ayarlari()
    elif(işlem == 5):
        print(computer.uygulama_listesi)
    elif(işlem == 6):
        print(computer.uygulama_listesi)
        sil = input("Silmek istediğiniz uygulamayı yazın(Büyük/Küçük harflere dikkat edin):")
        computer.uygulama_sil(sil)
    elif(işlem == 7):
        print("İşlemler sonlandırılıyor...")
        time.sleep(1)
        break
    else:
        print("Hatalı Giriş.")




