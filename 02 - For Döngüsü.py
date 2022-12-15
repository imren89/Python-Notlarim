# FOR DÖNGÜSÜ

sayilar="123456789"

for sayi in sayilar: # Sayıların içerisindeki ilk haneyi al yani "1"i. "sayi" değişkenine ata ve bu işlemi tekrar et
    print(sayi)
""" 
        Bu şekilde ekran çıktısı alırsak, 1'den 9'a kadar olan sayılar alt alta sıralanacaktır.
        1
        2
        3
        4
        5
        6
        7
        8
        9

  # RANGE Fonksiyonu #
    
    Bu fonksiyonun aslında yukarıdaki işlemi sağlar. Herhangi bir atama yapmaya gerek kalmadan
        (sayilar="123456789" gibi) otomatik olarak 0'dan ilgili değere kadar sayar.
    GENEL YAZILIŞI
    
    for a in range(100)     Burada 0'dan 100'e kadar olan sayilar sırasıyla "a" değişkenine atanır.
    Eğer sayma işleminin 0'dan değilde mesela 10'dan başlamasını istiyorsak, kodumuzu aşağıdaki gibi yazmalıyız.
    
    for a in range(10,100)  dikkat edin 10,100 yazdık.(10'dan 100'e kadar demek için)
        10
        11
        12
        13
        ...
        99
        
    Eğer aradaki artışın 5'er 5'er olmasını istiyorsak kod parçamız aşağıdaki gibi olur.
    for a in range(10,100,5)    son ksıma eklenen ",5" ifadesine dikkat ediniz.
        10
        15
        20
        25
        ...
        95
    
    NOT: Burada ki "a" değikeni geçici bir değikendir. Sadece for döngüsü içerisinde kullanılabilir.
    ÖNEMLİ NOT: range fonksiyonu dikkat ettiyseniz 100 ifadesini bastırmıyor.
                Çünkü bilgisayarlar sayamaya 0'dan başlarlar ve 100 ifadesi saymaya dahil DEĞİLDİR.
    
"""

