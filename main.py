import os
import asyncio
from telethon import TelegramClient

# Railway'e tanımladığın API bilgileri
API_ID = 33874556
API_HASH = '94e5e87725311749941fdbe7650cfc0e'

# Mesaj gönderilecek hedef gruplar
GROUPS = [
    "@aslantcrt11",
    "@iptvkartal",
    "@illegalforshell"
]

# Senin hazırladığın özel tanıtım mesajı
MESSAGE = """⚡ 𝕩  GÜVENLİ İŞLEM MERKEZİ  𝕩 ⚡

💎 PREMİUM TİCARET VE ÖDEME KANALI 💎

📥 𝕩 @dolarseviyorum  (İLETİŞİM) 𝕩 📥
💳 BANKA HESAPLARINIZ DEĞERİNDE ANINDA ALINIR 💳

🏛️ UZAKTAN ÖDEME VE TÜM SİSTEMLERE UYGUNDUR 🏛️

• Günlük / Haftalık Ödemeler Anında ve Nakit Yapılır
• İşlemler Sorunsuz ve Güvenli Şekilde Gerçekleştirilir
• Ciddi ve Sürekli Çalışmak İsteyen Sağlam Arkadaşlar Ulaşabilir

🔥 𝕩 TİCARETİN DOĞRU ADRESİ - İŞİNİ BİLENLER YAZSIN 𝕩 🔥"""

# Oturum dosyasını oluşturuyoruz
client = TelegramClient('userbot_session', API_ID, API_HASH)

async def main():
    print("Userbot başarıyla aktif edildi, mesaj döngüsü başlatılıyor...")
    
    while True:
        for group in GROUPS:
            try:
                await client.send_message(group, MESSAGE)
                print(f"Mesaj başarıyla gönderildi: {group}")
            except Exception as e:
                print(f"Hata ({group}): {e}")
            
            # Gruplar arası spam'e düşmemek için 60 saniye bekletme
            await asyncio.sleep(60)
            
        # Tüm gruplar bittikten sonra 10 dakika bekle
        await asyncio.sleep(600)

with client:
    # client.start() komutu ilk çalıştırmada telefon numarası ve kod isteyecektir
    client.start()
    client.loop.run_until_complete(main())
