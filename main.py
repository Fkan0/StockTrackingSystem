import controller
import json
import os

def veriyi_hazirla():
    if not os.path.exists("database.json"):
        # Eğer stock.py'den kurtulmak istersen buraya boş bir sözlük 
        # veya varsayılan bir depo yapısı yazabilirsin:
        # varsayilan = {"ana_depo": {}}
        import stock # Sadece burada, dosya yoksa geçici olarak çağır
        with open("database.json", "w", encoding="utf-8") as f:
            json.dump(stock.storage, f, indent=4, ensure_ascii=False)
    
    with open("database.json", "r", encoding="utf-8") as f:
        return json.load(f)

main_data = veriyi_hazirla()


#Uygulama başlatılıyor
#ansayfa döngüsü
while True:
    
   #Anasayfa bilgileri
    print("---  ANASAYFA ---\n")

    locate = "anasayfa"
    command = input(">>> ")
    print("") #Space oluşturma satırı

    controller.command_player(command, controller.command_list, main_data)

    # Her işlemden sonra veriyi otomatik kaydet
    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(main_data, f, indent=4, ensure_ascii=False)