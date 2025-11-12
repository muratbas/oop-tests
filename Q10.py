# Üç sayının ortalamasını hesaplayan program

def ortalama(a,b,c):
    ort = (a + b + c) / 3
    return ort

a = int(input("a'yi giriniz: "))
b = int(input("b'yi giriniz: "))
c = int(input("c'yi giriniz: "))

print("Ortalama:", ortalama(a,b,c))