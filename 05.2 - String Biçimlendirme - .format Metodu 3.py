a="Yazılım"
b="Programlama"

t=" {} {} ".format(a,b)

print(t)

"""
    EKRAN ÇIKTISI
    
    Yazılım Programlama
    
"""

"""
                FARKLI KULLANIM - 1
                
    Eğer t=" {1} {0} ".format(a,b)
    
    Şeklinde bir tanımlama yaparsam, bilgisayar 0'dan sayamaya bağladığı için ve b'nin argümanına 0 dediğimiz için
    
    EKRAN ÇIKTISI
    
    Programlama Yazılım
    
                    şeklinde olacaktır.
            
"""


"""
                FARKLI KULLANIM - 2

    Eğer t=" {0} {0} ".format(a,b)
        
    EKRAN ÇIKTISI
    
    Yazılım Yazılım
    
                    şeklinde olacaktır.
            
"""

"""


t=" {ilk} {son} ".format(ilk=a,son=b)     # anlık olarak ilk ve son değişkenlerini oluşturdum
                                          # bu değişkenleri argüman olarak kullandım.
    
    EKRAN ÇIKTISI
    
    Yazılım Programlama
    
"""