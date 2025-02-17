#4 tane bardağım var hepsini tanımla 
#liste oluştur
# #elimde ve her birinin içine rastgele bir biçimde şeker dolduruyorum 
# bardaklar max100 gr alıyor ve 
# daha sonra kullanıcıdan kaç gr şeker hesaplamak istediğini alıyorum 
#her döngüyü yazdır ve benim istediğim sayıya ne kadar eksik ne kaddar fazla göster
# ve bardakların içinde şekerlerin kullanıcının girdiği sayıya en yakın bardakların toplamını ekrana yazdırıyorum
import random

bardak1 = random.randint(0, 100)
bardak2 = random.randint(0, 100)
bardak3 = random.randint(0, 100)
bardak4 = random.randint(0, 100)

bardaklar = [bardak1, bardak2, bardak3, bardak4]

hedef = int(input("Kaç gram şeker hesaplayalım? "))

toplam = 0
en_yakin_bardaklar = []
en_yakin_fark = float('inf')

for i in range(1, 2**len(bardaklar)):
    kombinasyon = []
    toplam = 0
    for j in range(len(bardaklar)):
        if (i >> j) & 1:
            toplam += bardaklar[j]
            kombinasyon.append(f"Bardak {j+1} ({bardaklar[j]} gr)")
    
    fark = toplam - hedef
    if fark == 0:
        en_yakin_bardaklar = kombinasyon
        print(f"Döngü {i}: Hedefe tam uyuyor {', '.join(kombinasyon)} ve toplam şeker: {toplam} gr")
        break  
    else:
        durum = "fazla" if fark > 0 else "eksik"
        print(f"Döngü {i}: {', '.join(kombinasyon)} ve toplam şeker: {toplam} gr, {abs(fark)} gr {durum}")
        
        if abs(fark) < en_yakin_fark:
            en_yakin_fark = abs(fark)
            en_yakin_bardaklar = kombinasyon
            en_yakin_toplam = toplam


print(f"\nBardakların içindeki miktarlar: {bardaklar}")
if en_yakin_bardaklar:
    print(f"Hedefe en yakın bardaklar: {', '.join(en_yakin_bardaklar)} ve toplam şeker: {en_yakin_toplam} gr, fark: {en_yakin_fark} gr")
else:
    print("Hiçbir kombinasyon seçilmedi.")