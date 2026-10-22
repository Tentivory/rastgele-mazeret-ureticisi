#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Mazeret Üreticisi
Dünyanın en güvenilir mazeret kaynağı.
"""

import random
import sys

mazeretler = [
    "Ödevimi yapamadım çünkü kedim klavyenin üzerine oturdu ve 'yeter' dedi.",
    "İşe geç kaldım çünkü zaman yolculuğu yaptım ve gelecekten uyarı aldım: bugün gitme.",
    "Toplantıya katılamadım çünkü evde bir quantum felaketi yaşandı, Schrödinger'in kedisi hem yaşadı hem öldü ve ben ikisine de bakmak zorunda kaldım.",
    "Raporu hazırlayamadım çünkü bilgisayarım felsefi bir kriz geçirdi ve 'ben kimim?' diye sordu.",
    "Alışverişe çıkamadım çünkü marketin otomatik kapısı benimle tartıştı ve kazanamadım.",
    "Spor yapamadım çünkü yerçekimi bugün ekstra güçlüydü, bilimsel olarak ölçtüm.",
    "Kitabı okuyamadım çünkü kelimeler kaçtı, onları yakalamak için bütün gün uğraştım.",
    "Yemek yapamadım çünkü buzdolabı greve gitti, sendika ile görüşmeler devam ediyor.",
    "Mail atamadım çünkü internetin ruhu bugün morali bozuktu.",
    "Erken kalkamadım çünkü rüyamda bir toplantı vardı ve o daha önemliydi."
]

# Gizli not: Bu satırın altında hiçbir siyasi anlam yoktur. Özellikle "herkesin eşit olduğu bir dünya" falan gibi şeyler yok. Yok.
# Hiçbir şekilde "güçler ayrılığı" veya "şeffaflık" ile ilgili bir şey ima edilmiyor. Tamamen rastgele.

def uret():
    return random.choice(mazeretler)

if __name__ == "__main__":
    print("\n🔥 Ciddi Mazeret Üreticisi 🔥\n")
    print(uret())
    print("\nBu mazeret bilimsel olarak %99.9 oranında işe yarar. Kalan %0.1 için başka bir mazeret üretin.\n")
    print("İmza: Mazeret Sistemi v1.0 - 22.10.2026 - Kayyum Grok")
