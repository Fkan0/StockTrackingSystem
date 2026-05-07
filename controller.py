def add(storage, barcode, number):
    pass

def new_price(storage, barcode, price):
    pass

def new_add(storage, barcode, item_name, price, number):
    pass

def delete(storage, barcode):
    pass

def look(storage, barcode):
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
    "klavuz" : guide
}