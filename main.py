import json
import pages
import controller 

#Uygulama başlatılıyor
def veriyi_hazirla():
    with open("database.json", "r", encoding="utf-8") as f:
        return json.load(f)

main_data = veriyi_hazirla()

print("system: uygulama başlatıldı")
locate = ()

#PROGRAM İSKELETİ
def main(locate, code_list):
    


    #ANASAYFA (PAGE 1)
    while True:
        locate = ("1",)
        controller.title_page(locate, pages.page_keys)
        command = input(">>> ")

        if command == "0":
            locate = ()
            break
        
        elif command in code_list:
            locate =  ("1", command)

            #YAN SAYFA (PAGE 2)
            while True:
                controller.title_page(locate, pages.page_keys)
                command = input(">>> ")

                if command == "0":
                    locate = ("1",)
                    break

                elif command in code_list:
                    locate = ("1", locate[1], command)

                    #KOMUT SAYFASI (PAGE 3)
                    while True:
                        controller.title_page(locate, pages.page_keys)
                        command = input(">>> ")

                        if command == "0":
                            locate = ("1", locate[1])
                            break
        
                        else: 
                            try:
                                print(locate)
                                controller.command_list[locate]()
                            except Exception as e:
                                print(f"system: komut çalıştırılırken hata oluştu: {e}")

                            with open("database.json", "w", encoding="utf-8") as f:
                                json.dump(main_data, f, indent=4, ensure_ascii=False)

                else:
                    print("system: geçersiz komut a.")

        else:
            print("system: geçersiz komut b.")    

#main(locate, pages.page_keys)

print(main_data)