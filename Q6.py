# 1'den n'e kadar olan sayıların toplamını hesaplayan fonksiyon

def toplam(n):
    sonuc = n * (n + 1) / 2
    return sonuc

n = int(input("n'i giriniz: "))
print(toplam(n))
    