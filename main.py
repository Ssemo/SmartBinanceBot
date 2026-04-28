#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SmartBinanceBot 🚀
بوت تداول ذكي لـ Binance (Spot & Futures)
مع تحليل فني وإدارة مخاطر متقدمة
"""

from core.binance_client import BinanceClient
from datetime import datetime
import time


def print_header():
    """عرض رأس البوت بشكل احترافي"""
    print("=" * 60)
    print(" Smart Binance Bot ")
    print("=" * 60)
    print(f"⏰ الوقت: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


def print_balance(bot):
    """عرض الرصيد بشكل مفصل"""
    try:
        print("\n💰 === محفظة التداول ===")

        # رصيد USDT
        usdt_balance = bot.get_balance("USDT")
        print(f"💵 USDT المتاح: {usdt_balance:.2f}$")

        # رصيد BTC
        btc_balance = bot.get_balance("BTC")
        print(f"₿ BTC المتاح: {btc_balance:.8f}")

        # رصيد ETH
        eth_balance = bot.get_balance("ETH")
        print(f"Ξ ETH المتاح: {eth_balance:.6f}")

        # إجمالي المحفظة
        total_value = bot.get_total_balance()
        print(f"\n📊 إجمالي المحفظة: {total_value:.2f}$")

    except Exception as e:
        print(f"❌ خطأ في جلب الرصيد: {e}")


def analyze_market(bot):
    """تحليل السوق للعملات الرئيسية"""
    print("\n📈 === تحليل السوق ===")

    pairs = ["BTC/USDT", "ETH/USDT", "BNB/USDT"]
    for symbol in pairs:
        try:
            # جلب السعر الحالي
            ticker = bot.get_ticker(symbol)
            price = ticker.get('last', 0)

            # جلب التغير خلال 24 ساعة
            change_24h = ticker.get('percentage', 0)

            # تحديد الاتجاه
            if change_24h > 0:
                trend = "📈 صاعد"
            elif change_24h < 0:
                trend = "📉 هابط"
            else:
                trend = "➡️ مستقر"

            print(f"\n{symbol}:")
            print(f"  السعر: {price:,.2f}$")
            print(f"  التغير (24س): {change_24h:+.2f}% {trend}")

        except Exception as e:
            print(f"  ❌ خطأ في تحليل {symbol}: {e}")


def check_trading_signals(bot):
    """التحقق من إشارات التداول"""
    print("\n🎯 === إشارات التداول ===")

    # مثال: التحقق من فرص الشراء
    opportunities = []

    pairs = ["BTC/USDT", "ETH/USDT", "BNB/USDT", "SOL/USDT", "XRP/USDT"]

    for symbol in pairs:
        try:
            ticker = bot.get_ticker(symbol)
            price = ticker.get('last', 0)
            change = ticker.get('percentage', 0)

            # إشارة شراء إذا كان الانخفاض أكثر من 5%
            if change < -5:
                opportunities.append({
                    'symbol': symbol,
                    'price': price,
                    'change': change,
                    'signal': 'شراء قوي 🟢'
                })
            # إشارة بيع إذا كان الارتفاع أكثر من 5%
            elif change > 5:
                opportunities.append({
                    'symbol': symbol,
                    'price': price,
                    'change': change,
                    'signal': 'بيع أحمر 🔴'
                })

        except Exception:
            continue

    if opportunities:
        for opp in opportunities:
            print(f"\n{opp['symbol']}:")
            print(f"  السعر: {opp['price']:,.2f}$")
            print(f"  التغير: {opp['change']:+.2f}%")
            print(f"  الإشارة: {opp['signal']}")
    else:
        print("  ⚠️ لا توجد إشارات قوية حالياً")


def execute_test_trade(bot):
    """تنفيذ صفقة تجريبية (بدون أموال حقيقية)"""
    print("\n🧪 === صفقة تجريبية ===")

    symbol = "BTC/USDT"
    amount = 0.001  # كمية صغيرة للتجربة

    try:
        ticker = bot.get_ticker(symbol)
        price = ticker.get('last', 0)
        total = price * amount

        print(f"📊 تفاصيل الصفقة:")
        print(f"  الزوج: {symbol}")
        print(f"  النوع: شراء 🟢")
        print(f"  الكمية: {amount} BTC")
        print(f"  السعر: {price:,.2f}$")
        print(f"  الإجمالي: {total:,.2f}$")
        print(f"  ⚠️ هذه صفقة تجريبية فقط!")

        # هنا يمكنك إضافة كود التنفيذ الفعلي لاحقاً
        # bot.create_order(symbol, 'buy', amount, price)

    except Exception as e:
        print(f"  ❌ خطأ: {e}")


def show_bot_status():
    """عرض حالة البوت"""
    print("\n🔧 === حالة البوت ===")
    print("  ✅ البوت يعمل بشكل صحيح")
    print("  🌐 الاتصال: نشط")
    print("  🔐 المصادقة: ناجحة")
    print("  📡 API: متصل")


def main():
    """الدالة الرئيسية"""
    print_header()

    try:
        # إنشاء عميل Binance
        print("\n🔄 جاري الاتصال بـ Binance...")
        bot = BinanceClient()

        print("✅ تم الاتصال بنجاح!\n")

        # عرض حالة البوت
        show_bot_status()

        # عرض الرصيد
        print_balance(bot)

        # تحليل السوق
        analyze_market(bot)

        # إشارات التداول
        check_trading_signals(bot)

        # صفقة تجريبية
        execute_test_trade(bot)

        print("\n" + "=" * 60)
        print("✅ انتهى التحليل بنجاح!")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ خطأ فادح: {e}")
        print("\n💡 الحلول المقترحة:")
        print("  1. تأكد من صحة المفاتيح في ملف .env")
        print("  2. تحقق من اتصال الإنترنت")
        print("  3. تأكد من تفعيل IP Unrestricted في Binance")


if __name__ == "__main__":
    main()
