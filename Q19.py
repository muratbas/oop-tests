# Yarıçapı verilen bir dairenin alanını hesaplayan program

def dairealan(r):
    pi = 3.14
    alan = pi * (r**2)
    return alan

r = int(input("Yarıçapı giriniz: "))
print(dairealan(r))