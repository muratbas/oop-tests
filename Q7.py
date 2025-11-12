

def buyukmu(a,b,c):
    buyuk = a
    
    if b > buyuk:
        buyuk = b
    if c > buyuk:
        buyuk = c
    return buyuk

a = int(input("a'yi giriniz: "))
b = int(input("b'yi giriniz: "))
c = int(input("c'yi giriniz: "))

print(buyukmu(a,b,c))