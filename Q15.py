# Para miktarı, faiz oranı, yıl başlangıç ve yıl sonu alan ve faiz miktarını hesaplayan program

def faiz(para,faizorani,yil_baslangic,yil_son):
    yil_fark = yil_son - yil_baslangic
    faiz = para * (faizorani / 100) * yil_fark
    return faiz

para = int(input("Para miktarini giriniz: "))
faizorani = int(input("Faiz oranini giriniz: "))
yil_baslangic = int(input("Yil baslangicini giriniz: "))
yil_son = int(input("Yil sonunu giriniz: "))
print(faiz(para,faizorani,yil_baslangic,yil_son))
