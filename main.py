import asyncio
from telethon import TelegramClient

API_ID = 33874556
API_HASH = '94e5e87725311749941fdbe7650cfc0e'

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

client = TelegramClient('userbot_session', API_ID, API_HASH)

async def mesaj_gonderici():
    while True:
        try:
            for hedef in GRUPLAR:
                await client.send_message(hedef, MESAJ)
                print(f"Mesaj gönderildi: {hedef}")
                await asyncio.sleep(3)
        except Exception as e:
            print(f"Hata: {e}")
        
        await asyncio.sleep(DAKIKA_ARALIGI * 60)

async def main():
    print("Userbot başlatılıyor...")
    await client.start()
    print("Userbot başarıyla bağlandı ve çalışıyor!")
    
    # Arka plan döngüsünü başlat
    client.loop.create_task(mesaj_gonderici())
    
    # Botun 7/24 düşmeden çalışmasını sağla
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
