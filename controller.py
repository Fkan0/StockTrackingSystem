#SAYFA FONKSİYONLARI

#Sayfanın başlığını yazdırır ve alt sayfa veya komutları listeler.
def title_page(locate, name_list):


    #Sayfa başlığını yazdırır
    name = name_list.get(locate)
    title = f"  {name.upper()}  "
    print(title.center(50, "-"), end="\n\n")
    y = 1
    

    #Komut sayfasını açar
    if len(locate) == 3:
        print(f"--------  0 - Geri Dön  ")  
        print()    


    #Alt sayfaları listeler
    elif len(locate) == 2:
        for x in name_list:
            if len(x) == 3 and x[0] == locate[0] and x[1] == locate[1]:
                print(f"--------  {y} - {name_list.get(x)}  ")
                y += 1
                
        print(f"--------  0 - Geri Dön  ")
        print()      
        y = 1


    #Alt sayfaları listeler
    elif len(locate) == 1:
        print(">>> system: sayfa seçiniz.", end="\n\n")
        for x in name_list:
            if x[0] == locate[0] and len(x) == 2:
                print(f"--------  {y} - {name_list.get(x)}  ")
                y += 1
        
        print(f"--------  0 - Çıkış Yap  ")
        print() 
        y = 1



#SİSTEM FONKSİYONLARI
#komutları listeler
def help():
    pass

#komutların nasıl çalıştığını anlatır
def about():
    pass

#foksiyonları önceden kontrol eder
def error():
    pass



#KOMUT FONKSİYONLARI

#yeni ürün ekler
def new_item():
    pass
#ürün siler
def del_item():
    pass
#ürün günceller
def update_item():
    pass
#ürünü gösterir
def look_item():
    pass
#tüm ürünleri listeler
def item_list():
    pass
#stoğa ürün girişi yapar
def add_stock_item():
    pass
#stoktan ürün çıkışı yapar
def del_stock_item():
    pass
#kritik stokları gösterir
def danger_stock():
    pass
#stok hareket geçmişini gösterir
def transaction_history():
    pass
#satış yapar
def sales():
    pass
#satış geçmişini gösterir
def sales_history():
    pass
#iade işlemi yapar
def return_history():
    pass
#en çok satan ürünleri gösterir
def most_sales_item():
    pass
#en az satan ürünleri gösterir
def least_sales_item():
    pass
#günlük satış raporu gösterir
def daily_sales_report():
    pass
#kar zarar hesabı yapar
def profit_loss():
    pass        
#toplam stok değerini gösterir
def total_worth_stok():
    pass
#giriş yapar
def login():
    pass
#çıkış yapar
def logout():
    pass 
#yeni kullanıcı ekler
def new_user():
    pass
#kullanıcı yetkilerini gösterir
def user_role():
    pass
#veritabanı yedeği alır
def backup():
    pass
#tema değiştirir
def theme():
    pass
#tarih / saat ayarları yapar
def date_setting():
    pass
#logları temizler
def clear_log():
    pass
