# n tane sayının toplamını hesaplayan

def keretoplam(n):
    toplam = 0
    for i in range(n):
        sayi = int(input("Sayı giriniz: "))
        toplam += sayi
    return toplam

n=int(input("Kaç sayi girmek istiyorsunuz: "))
print(keretoplam(n))