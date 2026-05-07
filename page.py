page_list = {
    "1 - Ürün İşlemleri" : {
        "1 - Ürün Ekle" : {},
        "2 - Ürün Sil" : {},
        "3 - Ürün Güncelle" :{},
        "4 - Ürün Ara" :{},
        "5 - Tüm Ürünleri Listele" : {},
        "0 - Geri" : {}
    },
    "2 - Stok İşlemleri" : {
        "1 - Stoğa Ürün Girişi" : {},
        "2 - Stoktan Ürün Çıkışı" : {},
        "3 - Kritik Stokları Göster" : {},
        "4 - Stok Harekek Geçmişi" : {},
        "0 - Geri" : {}
    },
    "3 - Satış İşlemleri" : {
        "1 - Sayış Yap" : {},
        "2 - Sayış Geçmişi" : {},
        "3 - İade İşlemi" : {},
        "0 - Geri" : {}
    },
    "4 - Raporlar" : {
        "1 - En Çok Satan Ürüner" : {},
        "2 - En Az Satan Ürünler" : {},
        "3 - Günlük Satış Raporu" : {},
        "4 - Kar Zarar Hesabı" : {},
        "5 - Toplam Stok Değeri" : {},
        "0 - Geri" : {}
    },
    "5 - Kullanıcı İşlemleri" : {
        "1 - Giriş Yap" : {},
        "2 - Çıkış Yap" : {},
        "3 - Kullanıcı Ekle" : {},
        "4 - Yetkileri Görüntüle" : {},
        "0 - Geri" : {}
    },
    "6 - Ayarlar" : {
        "1 - Veritabanı Yedeği" : {},
        "2 - Tema Değiştir" : {},
        "3 - Tarih / Saat Ayarları" : {},
        "4 - Logları Temizle" : {},
        "0 - Geri" : {}
    },
    "0 - Çıkış" : {}
}

#HATA AYIKLAMA KOMUTLARI



#ÜRÜN İŞLEMLERİ FONKSİYONLARI
def new_item(barcode, price, *, stock=0 ,item_name=None, add_price=None, category=None, supplier=None):
    pass

def del_item(barcode):
    pass

def update_item(barcode, *, price=None, item_name=None, add_price=None, category=None, supplier=None ):
    pass

def look_item(barcode):
    pass

def item_list():
    pass



#STOK İŞLEMLERİ FONKSİYONLARI
def add_stock_item(barcode, stock=1, *, price=None):
    pass

def del_stock_item(barcode, stock=1):
    pass

def danger_stock():
    pass

def transaction_history():
    pass



#SATIŞ İŞLEMLERİ FONKSİYONLARI
def sales(barcode):
    pass

def sales_history():
    pass

def return_history():
    pass


#RAPOR FONKSİYONLARI
def most_sales_item():
    pass

def least_sales_item():
    pass

def daily_sales_report():
    pass

def profit_loss():
    pass

def total_worth_stok():
    pass



#AYAR FONKSİYONLARI
def backup():
    pass

def theme():
    pass

def date_setting():
    pass

def clear_log():
    pass



#TEMEL KOMUT FONKSİYONLARI
def help():
    pass

def quide():
    pass

def local():
    pass


#İŞLETİM KOMUTLARI



#SAYFA KOMUTLARI LİSTESI
page_command = {
    "1" : {
        "1" : {},
        "2" : {},
        "3" : {},
        "4" : {},
        "5" : {},
        "0" : {}
    },
    "2" : {
        "1" : {},
        "2" : {},
        "3" : {},
        "4" : {},
        "0" : {}        
    },
    "3" : {
        "1" : {},
        "2" : {},
        "3" : {},
        "0" : {}
    },
    "4" : {
        "1" : {},
        "2" : {},
        "3" : {},
        "4" : {},
        "5" : {},
        "0" : {}
    },
    "5" : {
        "1" : {},
        "2" : {},
        "3" : {},
        "4" : {},
        "0" : {}
    },
    "6" : {
        "1" : {},
        "2" : {},
        "3" : {},
        "4" : {},
        "0" : {}
    },
    "0" : {}
}