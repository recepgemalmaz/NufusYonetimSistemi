import json


class FileManager:
    __instance__ = None

    def __init__(self):
        if FileManager.__instance__ is None:
            FileManager.__instance__ = self
            self.vatandaslar = Vatandaslar()
            self.vatandaslar = self.kayitlariGetir()
            print(f"Veritabaninda suanda {len(self.vatandaslar.vatandaslar)} kisi var")
        else:
            raise Exception("Bu siniftan sadece bir tane uretebilirsin")

    @staticmethod
    def getInstance():
        if not FileManager.__instance__:
            FileManager()
        return FileManager.__instance__

    def kayitlariGetir(self):
        file1 = open("kisiler.db", "r+")
        fileStr = str(file1.read())
        file1.close()
        if not fileStr:
            self.__jsonHazirla()
        vatandaslar = Vatandaslar(fileStr)
        return vatandaslar

    def kayitMevcutMu(self, kimlikNo):
        kayitlar = self.kayitlariGetir()
        for kayit in kayitlar.vatandaslar:
            if kayit.kimlikNo == kimlikNo:
                return True
        return False

    def kayitGir(self):
        vatandas = Vatandas(None)
        while (True):
            kimlikNo = input("Kimlik No:")
            if len(kimlikNo) < 11 or len(kimlikNo) > 11:
                print("Lütfen geçerli bir kimlik numarası giriniz!!!!!")
                continue
            if self.kayitMevcutMu(kimlikNo):
                print("Bu kimlik numaralı kişi kayıtlarda mevcuttur")
                continue
            vatandas.kimlikNo = kimlikNo
            break
        while (True):
            adi = input("isim giriniz:")
            if len(adi) == 0:
                print("Lütfen geçerli bir isim giriniz!!!!!")
                continue
            vatandas.adi = adi
            break

        while (True):
            soyadi = input("Soyisim giriniz:")
            if len(soyadi) == 0:
                print("Lütfen geçerli bir soyisim giriniz!!!!!")
                continue
            vatandas.soyadi = soyadi
            break

        while (True):
            babaAdi = input("Baba adı giriniz:")
            if len(babaAdi) == 0:
                print("Lütfen geçerli bir baba adı giriniz!!!!!")
                continue
            vatandas.babaAdi = babaAdi
            break
        while (True):
            anneAdi = input("Anne adı giriniz:")
            if len(anneAdi) == 0:
                print("Lütfen geçerli bir anne adı giriniz!!!!!")
                continue
            vatandas.anneAdi = anneAdi
            break
        while (True):
            dogumYeri = input("Doğum yeri giriniz:")
            if len(dogumYeri) == 0:
                print("Lütfen geçerli bir doğum yeri giriniz!!!!!")
                continue
            vatandas.dogumYeri = dogumYeri
            break
        while (True):
            medeniDurumu = input("Medeni durumu giriniz:")
            if len(medeniDurumu) == 0:
                print("Lütfen geçerli bir medeni durumu giriniz!!!!!")
                continue
            vatandas.medeniDurumu = medeniDurumu
            break
        while (True):
            kanGrubu = input("Kan grubu giriniz:")
            if len(kanGrubu) == 0:
                print("Lütfen geçerli bir kan grubu giriniz!!!!!")
                continue
            vatandas.kanGrubu = kanGrubu
            break
        while (True):
            kutukSehir = input("Kütük şehrini giriniz:")
            if len(kutukSehir) == 0:
                print("Lütfen geçerli bir kütük şehri giriniz!!!!!")
                continue
            vatandas.kutukSehir = kutukSehir
            break
        while (True):
            kutukIlce = input("Kütük ilçe giriniz:")
            if len(kutukIlce) == 0:
                print("Lütfen geçerli bir kütük ilçe giriniz!!!!!")
                continue
            vatandas.kutukIlce = kutukIlce
            break
        while (True):
            ikametgahSehir = input("ikametgah şehri giriniz:")
            if len(ikametgahSehir) == 0:
                print("Lütfen geçerli bir ikametgah şehri giriniz!!!!!")
                continue
            vatandas.ikametgahSehri = ikametgahSehir
            break
        while (True):
            ikametgahIlce = input("ikametgah ilçe giriniz:")
            if len(ikametgahIlce) == 0:
                print("Lütfen geçerli bir ikametgah ilçe giriniz!!!!!")
                continue
            vatandas.ikametgahIlce = ikametgahIlce
            break
        kayitlar = self.vatandaslar.vatandaslar
        kayitlar.append(vatandas)
        self.__kaydet()
        print("Kayit başarıyla gerçekleştirildi.")

    def kayitAra(self, kimlikNo):
        kayitlar = self.vatandaslar.vatandaslar
        for kayit in kayitlar:
            if kimlikNo == kayit.kimlikNo:
                print(kayit.__dict__)
                return
        print("Kayit bulunamadı")

    def kayitSil(self, kimlikNo):
        kayitlar = self.vatandaslar.vatandaslar
        for i in range(0, len(kayitlar)):
            kayit = kayitlar[i]
            if kimlikNo == kayit.kimlikNo:
                kayitlar.pop(i)
                self.__kaydet()
                print("kayıt basari ile silindi")
                return
        print("Kayıt bulunamadı")

    def kayitGuncelle(self):
        while (True):
            kimlikNo = input("Güncellemek istediğiniz kişinin kimlik No:")
            if len(kimlikNo) < 11 or len(kimlikNo) > 11:
                print("Lütfen geçerli bir kimlik numarası giriniz!!!!!")
                continue
            if not self.kayitMevcutMu(kimlikNo):
                print("Bu kimlik numaralı kişi kayıtlarda mevcuttur değildir")
                continue
            break
        kayitlar = self.vatandaslar.vatandaslar
        for i in range(0, len(kayitlar)):
            kayit = kayitlar[i]
            if kimlikNo == kayit.kimlikNo:
                action = input(
                    "1-Ad 2-Soyad 3-Baba Adi 4-Anne Adi 5-Dogum Yeri 6-Medeni Durum 7-KanGrubu 8-Kutuk Sehir 9-Kutuk ilce 10-Ikamethah Sehir 11-Ikametgah Ilce\nLutfen bir secenek seciniz-->")
                while (True):
                    if not action.isdigit():
                        print("Lutfen gecerli bir deger giriniz")
                        continue
                    if int(action) < 1 or int(action) > 11:
                        print("Lutfen gecerli bir deger giriniz")
                        continue
                    actionInt = int(action)
                    if actionInt == 1:
                        while (True):
                            adi = input("isim giriniz:")
                            if len(adi) == 0:
                                print("Lütfen geçerli bir isim giriniz!!!!!")
                                continue
                            kayit.adi = adi
                            break

                    elif actionInt == 2:
                        while (True):
                            soyisim = input("soyisim giriniz:")
                            if len(soyisim) == 0:
                                print("Lütfen geçerli bir soyisim giriniz!!!!!")
                                continue
                            kayit.soyadi = soyisim
                            break
                    elif actionInt == 3:
                        while (True):
                            babaAdi = input("baba adı giriniz giriniz:")
                            if len(babaAdi) == 0:
                                print("Lütfen geçerli bir baba adı giriniz!!!!!")
                                continue
                            kayit.babaAdi = babaAdi
                            break
                    elif actionInt == 4:
                        while (True):
                            anneAdi = input("anne adı giriniz giriniz:")
                            if len(anneAdi) == 0:
                                print("Lütfen geçerli bir anne adı giriniz!!!!!")
                                continue
                            kayit.anneAdi = anneAdi
                            break
                    elif actionInt == 5:
                        while (True):
                            dogumYeri = input("doğum yeri giriniz:")
                            if len(dogumYeri) == 0:
                                print("Lütfen geçerli bir doğum yeri giriniz!!!!!")
                                continue
                            kayit.dogumYeri = dogumYeri
                            break
                    elif actionInt == 6:
                        while (True):
                            medeniDurumu = input("medeni durum giriniz:")
                            if len(medeniDurumu) == 0:
                                print("Lütfen geçerli bir medeni durum giriniz!!!!!")
                                continue
                            kayit.medeniDurumu = medeniDurumu
                            break
                    elif actionInt == 7:
                        while (True):
                            kanGrubu = input("kan grubu giriniz:")
                            if len(kanGrubu) == 0:
                                print("Lütfen geçerli bir kan grubu giriniz!!!!!")
                                continue
                            kayit.kanGrubu = kanGrubu
                            break
                    elif actionInt == 8:
                        while (True):
                            kutukSehir = input("kütük şehir giriniz:")
                            if len(kutukSehir) == 0:
                                print("Lütfen geçerli bir kütük şehir giriniz!!!!!")
                                continue
                            kayit.kutukSehir = kutukSehir
                            break
                    elif actionInt == 9:
                        while (True):
                            kutukIlce = input("kütük ilçe giriniz:")
                            if len(kutukIlce) == 0:
                                print("Lütfen geçerli bir kütük ilçe giriniz!!!!!")
                                continue
                            kayit.kutukIlce = kutukIlce
                            break
                    elif actionInt == 10:
                        while (True):
                            ikametgahSehri = input("ikametgah şehri giriniz:")
                            if len(ikametgahSehri) == 0:
                                print("Lütfen geçerli bir ikametgah şehri  giriniz!!!!!")
                                continue
                            kayit.ikametgahSehri = ikametgahSehri
                            break
                    elif actionInt == 11:
                        while (True):
                            ikametgahIlce = input("kütük ilçe giriniz:")
                            if len(ikametgahIlce) == 0:
                                print("Lütfen geçerli bir kütük ilçe giriniz!!!!!")
                                continue
                            kayit.ikametgahIlce = ikametgahIlce
                            break

                    break

                self.__kaydet()
                print("kayıt basari ile guncellendi")
                return

        print("Kayıt bulunamadı")

    def veritabaniniListele(self):
        for kayit in self.vatandaslar.vatandaslar:
            print(kayit.__dict__)

    def __jsonHazirla(self):
        file1 = open("kisiler.db", "a+")
        jsonStr = json.dumps(self.vatandaslar.__dict__)
        file1.write(jsonStr)
        file1.close()

    def __kaydet(self):
        file1 = open("kisiler.db", "r+")
        file1.truncate(0)
        jsonStr = json.dumps(self.vatandaslar.__dict__, default=self.__encodeVatandas)
        file1.write(jsonStr)
        file1.close()

    def __encodeVatandas(self, obj):
        if isinstance(obj, Vatandas):
            return obj.__dict__
        return obj


class Vatandaslar(object):

    def __init__(self, jsonString=None):
        self.vatandaslar = []
        if jsonString:
            vatandaslarListStr = json.loads(jsonString)
            for vatandasJsonObj in vatandaslarListStr["vatandaslar"]:
                vatandas = Vatandas(vatandasJsonObj)
                self.vatandaslar.append(vatandas)


class Vatandas(object):

    def __init__(self, jsonObj: None):
        if jsonObj:
            self.kimlikNo = jsonObj["kimlikNo"]
            self.adi = jsonObj["adi"]
            self.soyadi = jsonObj["soyadi"]
            self.babaAdi = jsonObj["babaAdi"]
            self.anneAdi = jsonObj["anneAdi"]
            self.dogumYeri = jsonObj["dogumYeri"]
            self.medeniDurumu = jsonObj["medeniDurumu"]
            self.kanGrubu = jsonObj["kanGrubu"]
            self.kutukSehir = jsonObj["kutukSehir"]
            self.kutukIlce = jsonObj["kutukIlce"]
            self.ikametgahSehri = jsonObj["ikametgahSehri"]
            self.ikametgahIlce = jsonObj["ikametgahIlce"]


fileManager = FileManager.getInstance()

while (True):
    islem = str(input(
        "Lutfen yapmak istediginiz islemi giriniz\n1-Kayit ekle\n2-Kayit Ara\n3-Kayit Guncelle\n4-Kayit Sil\n5-Kayitlari Listele\n0-Cikis\n----->"))
    if islem == "0":
        break
    elif islem == "1":
        fileManager.kayitGir()
    elif islem == "2":
        kimlikNo = str(input("Lutfen aramak istediginiz kayitin kimlik numarasini giriniz --->"))
        fileManager.kayitAra(kimlikNo)
    elif islem == "3":
        fileManager.kayitGuncelle()
    elif islem == "4":
        kimlikNo = str(input("Lutfen silmek istediginiz kayitin kimlik numarasini giriniz --->"))
        fileManager.kayitSil(kimlikNo)
    elif islem == "5":
        fileManager.veritabaniniListele()
    else:
        print("Lutfen gecerli bir deger giriniz")
