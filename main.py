import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# Senin API bilgilerim
API_ID = 33874556
API_HASH = '94e5e87725311749941fdbe7650cfc0e'

# Pydroid'den aldığın String Session kodun
SESSION_STRING = "1BJWap1wBu73yAU0WrzfEUYp3Eu-kccLd4854Ox26ZtKW0PmR3OBeHyVlGLaV7SxxuLqRjSAGdN-uFZKHOxFgzO02OH5uC-a40N49A4sEtGw5dx0UYNTg9SAtTXkysoVoR2KqOmXI6UDfbXPYgARZFv7-aFQExr0L-1tgC3b9jVw-ySmeIMop8fsv93orBIgQ_ToVbGODvuUYe44lB0GNREfVJKQ_QXud-0-X78LPArev7Qi5KDFGjJjp3MlEztiWUpp0VvUBnGkQbI8HwtfaVgYn6pBMc8y-iYmVhhj7c6fFftcpWm4Rh6kmnYpju2fBOlYu-qS8fPOKLJ51vBgt27eKEYXw_pM="

# Mesaj gönderilecek hedef gruplar
GROUPS = [
    "@aslantcrt11",
    "@iptvkartal",
    "@illegalforshell"
]

# Gönderilecek tanıtım mesajı
MESSAGE = """⚡ 𝕩  GÜVENLİ İŞLEM MERKEZİ  𝕩 ⚡

💎 PREMİUM TİCARET VE ÖDEME KANALI 💎

📥 𝕩 @dolarseviyorum  (İLETİŞİM) 𝕩 📥
💳 BANKA HESAPLARINIZ DEĞERİNDE ANINDA ALINIR 💳

🏛️ UZAKTAN ÖDEME VE TÜM SİSTEMLERE UYGUNDUR 🏛️

• Günlük / Haftalık Ödemeler Anında ve Nakit Yapılır
• İşlemler Sorunsuz ve Güvenli Şekilde Gerçekleştirilir
• Ciddi ve Sürekli Çalışmak İsteyen Sağlam Arkadaşlar Ulaşabilir

🔥 𝕩 TİCARETİN DOĞRU ADRESİ - İŞİNİ BİLENLER YAZSIN 𝕩 🔥"""

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    print("Userbot başarıyla aktif edildi, 1 dakikalık aralarla döngü başlatılıyor...")
    
    while True:
        for group in GROUPS:
            try:
                await client.send_message(group, MESSAGE)
                print(f"Mesaj başarıyla gönderildi: {group}")
            except Exception as e:
                print(f"Hata ({group}): {e}")
            
            # Her grup mesajından sonra tam 60 saniye (1 dakika) bekler
            await asyncio.sleep(60)
            
        # Tüm gruplara mesaj gittikten sonra döngü başa sarana kadar 1 dakika daha bekler
        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(main())
