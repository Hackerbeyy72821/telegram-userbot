import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
import os

API_ID = 33874556
API_HASH = '94e5e87725311749941fdbe7650cfc0e'

# Render'a eklediğimiz gizli oturum anahtarını alıyoruz
SESSION_STRING = os.environ.get('SESSION_STRING', '')

GRUPLAR = [
    'https://t.me/aslantcrt11',
    'https://t.me/iptvkartal',
    '@illegalforshell'
]

MESAJ = """⚡ 𝕩 GÜVENLİ İŞLEM MERKEZİ  𝕩 ⚡

💎 PREMİUM TİCARET VE ÖDEME KANALI 💎

📥 𝕩 @dolarseviyorum  (İLETİŞİM) 𝕩 📥
💳 BANKA HESAPLARINIZ DEĞERİNDE ANINDA ALINIR 💳

🏛️ UZAKTAN ÖDEME VE TÜM SİSTEMLERE UYGUNDUR 🏛️

• Günlük / Haftalık Ödemeler Anında ve Nakit Yapılır
• İşlemler Sorunsuz ve Güvenli Şekilde Gerçekleştirilir
• Ciddi ve Sürekli Çalışmak İsteyen Sağlam Arkadaşlar Ulaşabilir

🔥 𝕩 TİCARETİN DOĞRU ADRESİ - İŞİNİ BİLENLER YAZSIN 𝕩 🔥"""

DAKIKA_ARALIGI = 2

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def mesaj_dongusu():
    await client.start()
    print("Userbot başarıyla başlatıldı ve çalışıyor!")
    
    while True:
        try:
            for hedef in GRUPLAR:
                await client.send_message(hedef, MESAJ)
                print(f"Mesaj gönderildi: {hedef}")
                await asyncio.sleep(3)
        except Exception as e:
            print(f"Hata oluştu: {e}")
        
        await asyncio.sleep(DAKIKA_ARALIGI * 60)

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(mesaj_dongusu())
