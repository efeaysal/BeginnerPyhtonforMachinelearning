# Modüller : Kütüphane ve pakette denir fonksiyonlar grubudur

#''''HESAPLAMA MODULU ORNEK ''''''

def yeni_maas(x):
    print(x*20/100 + x)
    

import HesapModulu

HesapModulu.yeni_maas(1000)


import HesapModulu as hm
hm.yeni_maas(100)

from HesapModulu import yeni_maas
yeni_maas(2000)

