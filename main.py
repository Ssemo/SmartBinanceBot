from core.binance_client import BinanceClient
def main():
    try:
        bot = BinanceClient()
        balance = bot.get_balance("USDT")
        print(f"USDT Balance: {balance:.2f}")
        # تجربة بسيطة
        print("✅ البوت يشتغل بشكل صحيح!")
    except Exception as e:
        print(f"❌ خطأ: {e}")
if __name__ == "__main__":
        main()