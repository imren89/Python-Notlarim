# Python notları

# Dört işlem yapan bir program ile açıklayalım

sayi1 = float(input("Birinci sayiyi giriniz : "))
"""
Burada input ile kullanıcıdan sayı istedik, ancak girilen ifadenin string bir değer olmadığını
anlatabilmek için "float" olarak belirttik ve kullanıcıdan alınan sayiyi "sayi" değişkenine tanımladık.
"""
sayi2 = float(input("ikinci sayiyi giriniz : "))
islem = input("islem tipini giriniz : ") 

"""
    Operatörleri hatırlayalım

    +   Toplama Operatörü
    -   Çıkarma Operatörü
    /   Bölme Operatörü
    *   Çarpma Operatörü
    %   Mod alma Operatörü (Kalan bulma)
    **  Üst alma (Kuvvet) Operatörü 2**3 2'nin 3'üncü kuvveti demektir.
    //  Tam Bölüm Operatörü (Kalansız Bölme)
"""
if islem=="+":
    print("Toplam = ",sayi1+sayi2)
elif islem=="-":
    print("Fark = ",sayi1-sayi2)
elif islem=="*":
    print("Carpim = ",sayi1*sayi2)
elif islem=="/":
    print("Bolum = ",sayi1/sayi2)
elif islem=="%":
    print("Bolumden Kalan = ",sayi1%sayi2)
else:
    print("Hatali islem sectiniz.")
    
"""
    if'den sonra parantez açılmadan koşul yazılır ve kod parçasının tamamlandığı ":" ile söylenir
    alt satıra inerek ekrana socunu çıktı olarak vermek istediğimiz için "print" ifadesi kullanılır.
        NOT: Python programlama dili yorum dilidir. Bu sebeple süslü parantez gibi blok belirten ifadeler
        kullanılmaz. Onun yerine içeri doğru yazılır (Bir TAB boşluk kullanılır.)
"""