# a ve b sayılarının ortalamasını hesaplayan program

def islem(a,b):
    ort = ((a * 0.1) + (b * 0.1)) / 2
    return ort

a=int(input("a'yi giriniz: "))
b=int(input("b'yi giriniz: "))
print(islem(a,b))
     