a="Yazılım"
b="Programlama"

t="| {:>20} |".format(a)     # | Pipe işaretini koyma nedenimiz olan biteni görmektir.
                             # Bir kod parçası amaçlı yazmadık yani | işaretini.

print(t)

""" Yazı Solda

    t="| {:>20} |".format(a)
    
        EKRAN ÇIKTISI
        
        |               Yazılım |
    
    
"""

""" Yazı Sağda

    t="| {:<20} |".format(a)        # yön değiştirdiğimizde ise durum tam tersi olacaktır.
    
    
        EKRAN ÇIKTISI
        
        | Yazılım                |
    
"""

""" Yazı Ortada

      t="| {:^20} |".format(a)        # ^ işareti ile tam ortasına yazıdırabiliriz.
    
    
        EKRAN ÇIKTISI
        
        |       Yazılım      |
        
"""

""" Sadece String/integer İfadeler Görünsün
  
      t="| {:s} |".format(123)      # "s" ile sadece string ifadeler yazıdırabiliriz.
                                    # "d" ile sadece integer ifadeleri yazdırabiliriz.
                                    # "b" ile Binary sayı sistemi (2'lik taban)'da görüntüleme yapar ve değerlerinde yine
                                      2'lik sayı sistemine göre yazılmış olması gerekmektedir.
                                      
                                    # bu durumda içerğinde string ifade olmadığından hata verecektir.
"""

