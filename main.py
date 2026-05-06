import controller
import stock


#Uygulama hazırlanıyor
storage_list = list(stock.storage.keys())


#Uygulama başlatılıyor
#ansayfa döngüsü
while True:
    
   #Anasayfa bilgileri
    print("---  ANASAYFA ---\n")
    print("system: lütfen bir depo seçiniz")
    print(f"system: aktif depolarınız: {storage_list}")

    locate = "anasayfa"
    command = input(": ")


    if command in storage_list:

        storage = command

        #DEPO SAYFASI döngüsü
        while True:

            print(f"---  {storage.upper()}  ---")
            locate = f"anasayfa/{storage}"

            #Komut düzenleme kısmı.
            command = input(": ")
            command_parts = command.split()
            command_key = command_parts[0]
            command_parameter = command_parts[1:]
            print(command_key)
            print(command_parameter)

            #Çıkış yapmak istenirse
            if command in ["quit", "çıkış"]:
                break

            #Geçerli komut girlirse.
            elif command_key in controller.command_list:
                
                try:
                    controller.command_list[command_key](*command_parameter)

                except TypeError as e:
                    print(f"Hata: Eksik veya fazla parametre! \nDetay: {e}")

                except Exception as e:
                    print(f"Beklenmedik bir hata oluştu: {e}")
            
            #Bilinmeyen komut girilirse
            else:
                print("system: Bilinmeyen komut.")

    #Bilinmeyen komut girilirse.
    else:
        print("system: bilinmeyen komut.")
        continue