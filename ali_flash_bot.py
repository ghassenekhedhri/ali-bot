import os
import requests
import telegram

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = telegram.Bot(token=TELEGRAM_TOKEN)

def get_fake_deals():
    # هنا مكان AliExpress API الحقيقي لاحقًا
    deals = [
        "🔥 Deal 1: 90% off kitchen gadget → https://s.click.aliexpress.com/deal1",
        "🔥 Deal 2: 85% off LED light → https://s.click.aliexpress.com/deal2"
    ]
    return deals

if __name__ == "__main__":
    deals = get_fake_deals()
    for deal in deals:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=deal)
