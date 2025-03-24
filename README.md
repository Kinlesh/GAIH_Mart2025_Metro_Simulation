# GAIH_Mart2025_Metro_Simulation
Python ile metro ağı rota optimizasyonu simülasyonu.


# 🚇 Sürücüsüz Metro Simülasyonu – Rota Optimizasyonu

Bu proje, Global AI Hub & Akbank “Python ile Yapay Zekaya Giriş” Bootcamp'i kapsamında gerçekleştirilmiştir. Amaç, bir metro ağı üzerinde iki istasyon arasındaki:
- **En az aktarmalı rotayı** (BFS algoritması ile)
- **En hızlı rotayı** (A* algoritması ile)

bulabilen bir simülasyon geliştirmektir.

---

## 📌 Proje Özeti

- Metro ağı, bir **graf veri yapısı** olarak modellenmiştir.
- **BFS (Breadth-First Search)** algoritması ile istasyonlar arası en az aktarmalı rota bulunur.
- **A\*** algoritması ile toplam süre baz alınarak en hızlı rota hesaplanır.
- Gerçek hayattaki rota bulma problemlerine benzer bir yaklaşım sunar.

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

- **Python 3**
- `collections.deque`: BFS algoritması için kuyruk yapısı
- `heapq`: A* algoritması için öncelik kuyruğu

---

## 🔍 Algoritmaların Çalışma Mantığı

### ✅ BFS – En Az Aktarmalı Rota

- Her istasyon bir düğüm olarak modellenmiştir.
- `deque` yapısı ile genişlik öncelikli arama yapılır.
- Hedef istasyona en kısa yoldan (minimum düğüm sayısı) ulaşan rota döndürülür.
- Aktarma sayısını minimize eder.

### ✅ A* – En Hızlı Rota

- A* algoritmasında `f(n) = g(n) + h(n)` formülü uygulanır.
- Bu projede `h(n) = 0` olarak alındığı için algoritma **Dijkstra algoritması gibi** çalışır.
- Amaç: iki istasyon arasındaki **toplam yol süresini** en aza indirmektir.

---

## 🚀 Örnek Kullanım

Aşağıda örnek bir test senaryosu gösterilmektedir:

```python
# AŞTİ'den OSB'ye rota hesaplama
aktarmasiz = metro.en_az_aktarma_bul("M1", "K4")
print("En az aktarmalı rota:", " -> ".join(metro.istasyonlar[i].ad for i in aktarmasiz))

hizli = metro.en_hizli_rota_bul("M1", "K4")
yol, sure = hizli
print(f"En hızlı rota ({sure} dk):", " -> ".join(metro.istasyonlar[i].ad for i in yol))

Örnek Çıktı
En az aktarmalı rota: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
En hızlı rota (21 dk): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
