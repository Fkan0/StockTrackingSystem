def add(storage, barcode, number):
    print("başarılı")

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
    "klavuz" : guide
}