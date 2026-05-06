def add(storage, barcode, number):
    pass

def new_price(storage, barcode, price):
    pass

def new_add(storage, barcode, item_name, price, number):
    pass

def delete_barcode(storage, barcode):
    pass

def delete_item_name(storage_name):
    pass

def look_barcode(storage, barcode):
    pass

def look_item_name(storage, item_name):
    pass

def add_storage(storage):
    pass

def delete_storage(storage):
    pass

def clear_storage(storage):
    pass

def look_storage(storage):
    pass

def help():
    pass

def guide():
    pass


command_list = {
    "ürün-tazele" : add,
    "fiyat-tazele" : new_price,
    "ürün-ekle" : new_add,
    "ürün-sil" : delete_barcode,
    "ürün-sil -barcode" : delete_barcode,
    "ürün-sil -isim" : delete_item_name,
    "ürün-bak" : look_barcode,
    "ürün-bak -barkod" : look_barcode,
    "ürün-bak -isim" : look_item_name,
    "yeni-depo" : add_storage,
    "depo-sil" : delete_storage,
    "depo-sıfırla" : clear_storage,
    "depo-bak" : look_storage,
    "help" : help,
    "yardım" : help,
    "guide" : guide,
    "klavuz" : guide
}