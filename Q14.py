# Günlük ücret ve çalışılan gün sayısını alan ve maaşı hesaplayan program

def iscimaas(g_ucret,g_sayi):
    sigorta = 4/100
    pul = 5/100
    maas = g_ucret * g_sayi
    maas = maas - (maas * sigorta) - (maas * pul)
    maas = maas - (maas / 4)
    return maas

g_ucret = int(input("Günlük Ücreti Giriniz: "))
g_sayi = int(input("Kac gun calisti: " ))
print(iscimaas(g_ucret,g_sayi))
    
    