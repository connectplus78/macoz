import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone
import re

# Türkiye saati için zaman dilimi ayarı
tr_tz = timezone(timedelta(hours=3))

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
}
url = "https://m.sporx.com/tvdebugun/"

print("Siteden veriler çekiliyor...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # --- HTML Tasarım Kısmı (Aynı bıraktım) ---
    html_ust = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Connect Plus - Günün Maçları</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
            * { box-sizing: border-box; }
            body { font-family: 'Poppins', sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 0; }
            .header { background: linear-gradient(135deg, #1e293b, #0f172a); padding: 20px 15px; text-align: center; border-bottom: 1px solid #334155; }
            .header-title { font-size: 24px; font-weight: 800; color: #0ea5e9; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
            .header-subtitle { font-size: 13px; color: #94a3b8; font-weight: 500; letter-spacing: 0.5px; }
            .tabs { display: flex; justify-content: center; gap: 8px; background: #0f172a; padding: 15px 10px; position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
            .tab-btn { flex: 1; max-width: 90px; background: #1e293b; border: 1px solid #334155; border-radius: 20px; font-size: 13px; color: #94a3b8; font-weight: 600; cursor: pointer; padding: 8px 5px; transition: all 0.3s ease; text-align: center; }
            .tab-btn.active { background: #0ea5e9; color: #fff; border-color: #0ea5e9; box-shadow: 0 0 12px rgba(14, 165, 233, 0.5); }
            #mac-listesi { padding: 15px; }
            .kutu { display: flex; align-items: center; background: #1e293b; margin-bottom: 12px; padding: 15px; border-radius: 16px; border-left: 5px solid #0ea5e9; box-shadow: 0 4px 6px rgba(0,0,0,0.2); }
            .saat { color: #38bdf8; font-size: 22px; font-weight: 700; min-width: 65px; border-right: 1px solid #334155; margin-right: 12px; }
            .orta { flex-grow: 1; display: flex; flex-direction: column; justify-content: center; overflow: hidden; }
            .kanal-satiri { display: flex; align-items: center; gap: 10px; margin-bottom: 5px; }
            .kanal-isim { color: #f1f5f9; font-weight: 600; font-size: 15px; }
            .kanal-logo { height: 22px; max-width: 60px; object-fit: contain; background: #fff; border-radius: 4px; padding: 2px; }
            .mac-isim { color: #94a3b8; font-size: 13px; }
            .canli { background: #ef4444; color: white; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; }
            .gizli { display: none !important; }
            .alt-bilgi { text-align: center; color: #64748b; font-size: 12px; margin: 20px 0 40px 0; }
        </style>
    </head>
    <body>
        <div class="header">
            <div class="header-title">📺 Connect Plus</div>
            <div class="header-subtitle">Günün Maç Yayınları</div>
        </div>
        <div class="tabs">
            <button class="tab-btn active" onclick="filtrele('Tumu', this)">Tümü</button>
            <button class="tab-btn" onclick="filtrele('Futbol', this)">Futbol</button>
            <button class="tab-btn" onclick="filtrele('Basketbol', this)">Basket</button>
        </div>
        <div id="mac-listesi">
    """

    # ... (Veri işleme mantığınız aynı kalıyor) ...
    # (Buradaki mac listesi oluşturma döngülerinizi olduğu gibi kullanabilirsiniz)
    
    # ZAMAN KISMI DÜZELTİLDİ:
    guncel_zaman = datetime.now(tr_tz).strftime("%d-%m-%Y %H:%M")
    
    tam_html = html_ust + "..." + f"<div class='alt-bilgi'>Son Güncelleme: {guncel_zaman}</div>" + "..." 
    
    with open("index.html", "w", encoding="utf-8") as dosya:
        dosya.write(tam_html)
        
    print(f"İşlem tamamlandı! Saat: {guncel_zaman}")

else:
    print(f"Bağlantı hatası: {response.status_code}")
