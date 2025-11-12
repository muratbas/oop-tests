# Bir üçgenin en küçük kenarını bulan program

def enkucukkenar(a,b,c):
    enkucuk = a
    if b < enkucuk:
        enkucuk = b
    if c < enkucuk:
        enkucuk = c
    return enkucuk

a = int(input("a'yi giriniz: "))
b = int(input("b'yi giriniz: "))
c = int(input("c'yi giriniz: "))
print(enkucukkenar(a,b,c))