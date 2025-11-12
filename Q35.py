# Vize ve final notlarını alan ve ortalamayı hesaplayan program

def ort(vize,final):
    vize = vize * 0.4
    final = final * 0.6
    ortalama = (vize + final) / 2
    if ortalama >= 60:
        return "Geçti", ortalama
    else:
        return "Kaldı", ortalama

vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
print(ort(vize,final))