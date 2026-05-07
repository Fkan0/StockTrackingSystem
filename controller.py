#Hata kontrolcü fonksiyonu
def error_controller(main, storage=None, barcode=None, item_name=None, price=None, number=None):
    #Depo kontrolcüsü
    if storage is not None:
        if storage not in main:
            print("system: depo bulunamadı")
            return False

    #Barkod kontrolcusü
    if barcode is not None:
        #Barkod sadece sayılardanmı oluşuyor
        if not barcode.isdecimal():
            print("system: barkod sadece sayılardanoluşmalı")
            return False
        
        #Barkod 13 hanelimi
        if len(barcode) != 13:
            print("system: barkod 13 haneli olmalı")
            return False

    #Ürün ismi kontrolcüsü
    if item_name is not None:
        #Çok kısa isim ise
        if len(item_name) < 2:
            print("system: ürün ismi en az 2 karakter olmalı")
            return False
        
        #Çok uzun isim is
        if len(item_name) > 50:
            print("system: ürün ismi çok uzun (maks 50 karakter)")
            return False

    #Ürün fiyatı kontrolcüsü
    if price is not None:
        clean_price = price.replace(",", ".")

        try:
            val = float(clean_price)
            if val <= 0:
                print("system: fiyat 0'dan büyük olmalı")
                return False
            
        except ValueError:
            print("system: geçersiz fiyat formatı")
            return False
        
    #ürün adedini kontrol eder
    if number is not None:
        if not number.isdecimal():
            print("system: ürün adedi tam sayı olmalı")
            return False
        
    return True



#Stok yenileme fonksiyonu
def add(main, storage, barcode, number):

    #Hata kontrol bloğu
    if not error_controller(main=main, storage=storage, barcode=barcode, number=number):
        return



#Fiyat yenileme foksiyonu
def new_price(main, storage, barcode, price):

    #Hata kontrol bloğu
    if not error_controller(main=main, storage=storage, barcode=barcode, price=price):
        return



#Yeni ürün ekleme fonksiyonu
def new_add(main, storage, barcode, item_name, price, number):

    #Hata kontrol bloğu
    if not error_controller(main=main, storage=storage, item_name=item_name, price=price, number=number):
        return



#Ürün silme fonksiyonu
def delete(main, storage, barcode):

    #Hata kontrol bloğu
    if not error_controller(main=main, storage=storage, barcode=barcode):
        return



#Ürün özelliklerine bakma fonksiyonu
def look(main, storage, barcode):

    #Hata kontrol bloğu
    if not error_controller(main=main, storage=storage, barcode=barcode):
        return



#Yeni depo ekleme fonksiyonu
def add_storage(main, storage):

    #Hata kontrol bloğu
    if not error_controller(main=main):
        return



#Depo silme fonksiyonu
def delete_storage(main, storage):

    #Hata kontrol bloğu
    if not error_controller(main=main, storage=storage):
        return



#Depo sıfırlama fonksiyonu
def clear_storage(main, storage):

    #Hata kontrol bloğu
    if not error_controller(main=main, storage=storage):
        return



#Depo bakma fonksiyonu
def look_storage(main, storage):

    #Hata kontrol bloğu
    if not error_controller(main=main, storage=storage):
        return



#Mecvüt depoları listeler
def storages(main):
    print(f"mevcut depolarınız: {main}")



#Bulunulan sayfa konumunu gösterir
def locate(locate):
    print(f"system locate: {locate}")



#Yardım fonksiyonu
def help():
    pass



#Klavuz fonksiyonu
def guide():
    pass



#Komut yürütücü fonksiyon
def command_player(command, list):
    if not command:
        print("system: eksik komut girildi")
        return
    
    if isinstance(command, str):
        command_parts = command.split()

    else:
        command_parts = command

    command_key = command_parts[0]
    command_parameter = command_parts[1:]
    

    if command_key in list:
        code = list[command_key]

        if isinstance(code, dict):
            command_player(command_parameter, code)
        
        elif callable(code):
            try:
                code(*command_parameter)
            except TypeError as e:
                print(f"system: pametre hatası: {e}")
    else:
        print(f"system: '{command_key}' geçerli bir komut değil")



#Komut listesi
command_list = {
    "ürün" : {
        "ekle" : new_add,
        "sil" : delete,
        "bak" : look,
        "tazele" : {
            "stok" : add,
            "fiyat" : new_price,
        }
    },
    "depo" : {
        "ekle" : add_storage,
        "sıfırla" : clear_storage,
        "depo bak" : look_storage,
        "depo sil" : delete_storage
    },
    "yardım" : help,
    "klavuz" : guide,
    "depolar" : storages,
    "konum" : locate
}   