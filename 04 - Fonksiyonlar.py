# FONKSİYONLAR
"""
def toplama(sayi1,sayi2):   # toplama adında bir fonksiyon oluşturduk (def komutu fonksiyon oluşturmaya yarar)
    toplama=sayi1+sayi2     # sayi1 ve sayi2 yi topladık
    return toplama          # return değer döndür demektir

print(toplama())



def hipo(a,b,c):
    if a**2 + b**2 == c**2:
        return "Bu üçgenin bir açısı 90 derecedir."
    else:
        return "Bu üçgenin bir açısı 90 derece değildir!"
        
print(hipo(3,4,5))

"""

def sag(adet):
    for a in range(int(adet)):
        print("/",end="")       # end komutu "\n" anlamına gelir ve yeni satıra geç demektir.  

def sol(adet):
    for a in range(int(adet)):
        print("\\",end="")      # \ ifadesini  ekrana yazdırmak için 2 tane \\ kullanılır.
        
def bosluk(adet):
    for a in range(int(adet)):
        print(" ",end="") 
        
def atla(adet):
    for a in range(int(adet)):
        print() 

def ust(cap):
    baslangic=cap/2-1
    for a in range(int(cap/2)):
        bosluk(baslangic-a)
        sag(1)
        bosluk(a*2)
        sol(1)
        atla(1)
        
#ust(10)    buradaki 10  ifadesinin ÇAP değişkenine karşılık geldiğini görebilirsiniz.

def alt(cap):                        # Yukarıda yapmış olduğumuz tasarımın tersini altına yapıp ekleyeceğiz.
    baslangic=cap-2
    for a in range(int(cap/2)):
        bosluk(a)
        sol(1)
        bosluk(baslangic-a*2)
        sag(1)
        atla(1)
    
def paralel(cap):                   # Yukarısı ve aşağısı birbirinin paralelidir.
    ust(cap)                        # Bu sebeple paralel fonksiyonunda alt ve üst kısımın çap değerleri aynı olmalıdır.
    alt(cap)

boyut=int(input("Çap değerini giriniz: "))
print()
paralel(boyut)