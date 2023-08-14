^#map & filter & reduce 


^#map : Bir listenin içinde fonksiyon çalıştırmamıza yarar 
liste = [1,2,3,4,5]

for i in liste: 
    print(i+10)
    
    
list(map(lampda x: x*10, liste))


#filter: şartın sağlandığı elemanlara etki gösterir filtreler
liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x%2 == 0, liste))

#reduce 

from functools import reduce

liste = [1,2,3,4,5]
reduce(lambda a,b: a + b , liste)

^# Fonksiyonel programlama işlerimizi daha kolay hale getirir daha az yan etkisi vardır 
# =============================================================================
# biraz daha matematiksel alana geçtiğimizde fonksiyonel programlaama daha çok işimize yarayacak
# =============================================================================
