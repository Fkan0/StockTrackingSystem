import controller
import json
import page


#Uygulama başlatılıyor
def veriyi_hazirla():
    with open("database.json", "r", encoding="utf-8") as f:
        return json.load(f)

main_data = veriyi_hazirla()

print("system: uygulama başlatıldı")



#ansayfa döngüsü
while True:
    
   #Anasayfa bilgileri
    print("  ANASAYFA  ".center(50, "-"))
    print()
    for x in page.page_list:
        print("----------  " + x)
    print()
    command = input(">>> ")
    print() 

    controller.command_player(command, controller.command_list, main_data)

    # Her işlemden sonra veriyi otomatik kaydet
    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(main_data, f, indent=4, ensure_ascii=False)