import controller
import stock


#Uygulama hazırlanıyor
storage_list = list(stock.storage.keys())


#Uygulama başlatılıyor
#ansayfa döngüsü
while True:
    
   #Anasayfa bilgileri
    print("---  ANASAYFA ---\n")

    locate = "anasayfa"
    command = input(": ")
    main = "stock"
    
    controller.command_player(command, controller.command_list)