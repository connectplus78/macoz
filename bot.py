import requests
from bs4 import BeautifulSoup
import datetime
import re

# Tarihi anlık al
zaman = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
url = "https://m.sporx.com/tvdebugun/"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    # ... (Buraya daha önceki maç çekme döngünüzü ekleyin) ...
    
    # HTML'i oluştururken 'zaman' değişkenini kullanıyoruz
    tam_html = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Connect Plus - Günün Maçları</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
            body {{ font-family: 'Poppins', sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }}
            .kutu {{ background: #1e293b; padding: 15px; margin-bottom: 10px; border-radius: 12px; border-left: 5px solid #0ea5e9; }}
            .alt-bilgi {{ text-align: center; color: #64748b; margin-top: 20px; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div id="mac-listesi">
            <!-- Maçlar buraya gelecek -->
        </div>
        <div class="alt-bilgi">
            © 2026 Connect Plus | Son Güncelleme: {zaman}
        </div>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(tam_html)
    print(f"Başarılı! Güncelleme saati: {zaman}")
