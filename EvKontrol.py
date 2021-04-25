import time


class ev_kontrol():
    def __init__(self, ışık_durumu="kapalı", internet_durumu="kapalı", doğalgaz_durumu="kapalı", sıcaklık=24,
                 kapıların_durumu="kapalı"):
        self.ışık_durumu = ışık_durumu
        self.internet_durumu = internet_durumu
        self.doğalgaz_durumu = doğalgaz_durumu
        self.sıcaklık = sıcaklık
        self.kapıların_durumu = kapıların_durumu

    def ışık_aç(self):
        if (self.ışık_durumu == "açık"):
            print("Işıklar zaten açık")
        else:
            print("ışıklar açılıyor")
            self.ışık_durumu = "açık"

    def ışık_kapat(self):
        if (self.ışık_durumu == "kapalı"):
            print("ışıklar zaten kapalı")
        else:
            print("ışıklar kapanıyor")
            self.ışık_durumu = "kapalı"

    def internet(self):
        print("Şuanda bağlı cihaz sayısı 12'dir. ")

    def doğalgaz_aç(self):
        if (self.doğalgaz_durumu == "açık"):
            print("doğalgaz açık")
        else:
            print("doğalgaz açılıyor..")
            self.doğalgaz_durumu = "açık"

    def doğalgaz_kapat(self):
        if (self.doğalgaz_durumu == "kapalı"):
            print("doğalgaz kapalı")
        else:
            print("doğalgaz kapatılıyor")
            self.doğalgaz_durumu = "kapalı"

    def sıcaklık_söstergesi(self):
        print(self.sıcaklık)

    def sıcaklık_Değiştir(self):
        soru = input("arttırmak mı azaltmak mı istiyorsunuz: ")
        if (soru == "art"):
            sıcaklıklar = int(input("Arttırmak istediğiniz değeri giriniz: "))
            self.sıcaklık += sıcaklıklar
        elif (soru == "azalt"):
            sıcaklıklar2 = int(input("Azaltmak istediğiniz değeri giriniz: "))
            self.sıcaklık -= sıcaklıklar2

    def kapı_aç(self):
        if (self.kapıların_durumu == "açık"):
            print("kapılar zaten açık")
        else:
            print("kapılar açılıyor")
            self.kapıların_durumu = "açık"

    def kapı_kapat(self):
        if (self.kapıların_durumu == "kapalı"):
            print("kapılar zaten açık")
        else:
            print("kapılar kapatılıyor")
            self.kapıların_durumu = "kapalı"

    def __str__(self):
        return "Işıklar{}\nİnternet{}\nDoğalgaz{}\Sıcaklık{}\Kapılar{}".format(self.ışık_durumu, self.internet_durumu,
                                                                               self.doğalgaz_durumu, self.sıcaklık,
                                                                               self.kapıların_durumu)


kontrol = ev_kontrol()

print("""
EV KONTROL UYGULAMAMIZA HOŞGELDİNİZ EVİNİZİN ÖZELLİKLEİNİ KULLANMAYA BAŞLAYABİLİRSİNİZ
1-IŞIKLARI AÇ
2-IŞIKLARI KAPAT
3-DOĞALGAZI AÇ
4-DOĞALGAZI KAPAT
5-SICAKLIK GÖSTER
6-SICAKLIK DEĞİŞTİR
7-KAPILARI AÇ
8-KAPILARI KAPAT
9-EVİN DURUMUNU GÖSTER
""")

while True:
    işlem = input("Yapmak istediğiniz işlemi seçiniz: ")
    if (işlem == "1"):
        kontrol.ışık_aç()

    elif (işlem == "2"):
        kontrol.ışık_kapat()

    elif (işlem == "3"):
        kontrol.doğalgaz_aç()

    elif (işlem == "4"):
        kontrol.doğalgaz_kapat()

    elif (işlem == "5"):
        kontrol.sıcaklık_söstergesi()

    elif (işlem == "6"):
        kontrol.sıcaklık_Değiştir()
    elif (işlem == "7"):
        kontrol.kapı_aç()
    elif (işlem == "8"):
        kontrol.kapı_kapat()
    elif (işlem == "9"):
        kontrol.__str__()
        