from collections import deque, defaultdict
import heapq

# Istasyon sınıfı, her bir metro istasyonunu temsil eder
class Istasyon:
    def __init__(self, id, ad, hat):
        self.id = id                  # Istasyon ID
        self.ad = ad                  # Istasyonun adı
        self.hat = hat                # Hangi hatta bulunduğu
        self.komsular = []            # [(komsu_id, süre)]

# Metro ağı sınıfı
class MetroAgi:
    def __init__(self):
        self.istasyonlar = {}                # ID -> Istasyon
        self.graf = defaultdict(list)        # ID -> [(komsu_id, süre)]

    def istasyon_ekle(self, id, ad, hat):
        self.istasyonlar[id] = Istasyon(id, ad, hat)

    def baglanti_ekle(self, id1, id2, sure):
        self.istasyonlar[id1].komsular.append((id2, sure))
        self.istasyonlar[id2].komsular.append((id1, sure))
        self.graf[id1].append((id2, sure))
        self.graf[id2].append((id1, sure))

    # BFS algoritması: en az aktarmalı rota
    def en_az_aktarma_bul(self, baslangic, hedef):
        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edilen = set()

        while kuyruk:
            mevcut, yol = kuyruk.popleft()
            if mevcut == hedef:
                return yol
            if mevcut in ziyaret_edilen:
                continue
            ziyaret_edilen.add(mevcut)
            for komsu, _ in self.graf[mevcut]:
                if komsu not in ziyaret_edilen:
                    kuyruk.append((komsu, yol + [komsu]))
        return None

    # A* algoritması: en hızlı rota (heuristic = 0 olduğu için Dijkstra gibi çalışır)
    def en_hizli_rota_bul(self, baslangic, hedef):
        def heuristik(a, b):
            # Sabit 0 heuristik: Gerçek mesafeleri bilmediğimiz için Dijkstra gibi çalışır, .
            return 0

        pq = [(0 + heuristik(baslangic, hedef), 0, baslangic, [baslangic])]
        ziyaret_edilen = set()

        while pq:
            tahmini_toplam, g_maliyeti, mevcut, yol = heapq.heappop(pq)
            if mevcut == hedef:
                return yol, g_maliyeti
            if mevcut in ziyaret_edilen:
                continue
            ziyaret_edilen.add(mevcut)
            for komsu, s in self.graf[mevcut]:
                if komsu not in ziyaret_edilen:
                    yeni_g = g_maliyeti + s
                    f = yeni_g + heuristik(komsu, hedef)
                    heapq.heappush(pq, (f, yeni_g, komsu, yol + [komsu]))
        return None

# Örnek metro ağı tanımı
metro = MetroAgi()

# İstasyonlar
metro.istasyon_ekle("K1", "Kızılay", "Kırmızı")
metro.istasyon_ekle("K2", "Ulus", "Kırmızı")
metro.istasyon_ekle("K3", "Demetevler", "Kırmızı")
metro.istasyon_ekle("K4", "OSB", "Kırmızı")
metro.istasyon_ekle("M1", "AŞTİ", "Mavi")
metro.istasyon_ekle("M2", "Kızılay", "Mavi")
metro.istasyon_ekle("M3", "Sıhhiye", "Mavi")
metro.istasyon_ekle("T1", "Gar", "Turuncu")
metro.istasyon_ekle("T2", "Demetevler", "Turuncu")

# Bağlantılar (komşuluk ve süre)
metro.baglanti_ekle("K1", "K2", 9)
metro.baglanti_ekle("K2", "K3", 1)
metro.baglanti_ekle("K3", "K4", 8)
metro.baglanti_ekle("M1", "M2", 2)
metro.baglanti_ekle("M2", "M3", 7)
metro.baglanti_ekle("K1", "M2", 3)
metro.baglanti_ekle("M3", "T1", 6)
metro.baglanti_ekle("K3", "T2", 4)

# Test senaryosu: AŞTİ'den OSB'ye
print("\nAŞTİ'den OSB'ye")
aktarmasiz = metro.en_az_aktarma_bul("M1", "K4")
if aktarmasiz:
    print("En az aktarmalı rota:", " -> ".join(metro.istasyonlar[i].ad for i in aktarmasiz))

hizli = metro.en_hizli_rota_bul("M1", "K4")
if hizli:
    yol, sure = hizli
    print(f"En hızlı rota ({sure} dk):", " -> ".join(metro.istasyonlar[i].ad for i in yol))
