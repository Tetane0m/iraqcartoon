import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

TOKEN = "7540969814:AAGSNZ900wJW-LZEns7yPDDz8X0db7GN12w"


# دالة البدء
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("عن بيت الكاريكاتير", callback_data='about')],
        [InlineKeyboardButton("الفعاليات", callback_data='events')],
        [InlineKeyboardButton("المسابقات القادمة", callback_data='competitions')],
        [InlineKeyboardButton("الإنجازات", callback_data='achievements')],
        [InlineKeyboardButton("التواصل", callback_data='contact')],
        [InlineKeyboardButton("وسائل التواصل الاجتماعي", callback_data='social_media')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎨 **مرحبًا بك في بيت الكاريكاتير العراقي!**\nاختر أحد الأزرار أدناه لمعرفة المزيد:", reply_markup=reply_markup)


# بيانات الفعاليات والمسابقات والإنجازات
EVENTS = [
    "📅 ندوة فن الكاريكاتير الرقمي - 15 أكتوبر",
    "🎨 معرض 'ضحكة وطن' - 20-25 نوفمبر",
    "🖌 دورة رسم كاريكاتير - ديسمبر 2024",
    "🗣 لقاء الفنانين الشباب - يناير 2025"
]

COMPETITIONS = [
    "🏆 مسابقة 'كاريكاتير البيئة' - آخر موعد 30 نوفمبر",
    "🎖 الجائزة الذهبية للفكاهة الاجتماعية - يناير 2024",
    "🖼 تحدي الرسم الساخر - مارس 2025"
]

ACHIEVEMENTS = [
    "🥇 تنظيم 50+ معرض دولي",
    "🏅 الفوز بـ 3 جوائز 'أفضل مؤسسة فنية' في الشرق الأوسط",
    "🖌 دعم أكثر من 200 فنان ناشئ",
    "📢 تنظيم أكبر حملة توعوية بالفن الساخر"
]

SOCIAL_MEDIA = {
    "Facebook": "https://facebook.com/example",
    "Instagram": "https://instagram.com/example",
    "Twitter": "https://twitter.com/example",
    "YouTube": "https://youtube.com/example"
}

CONTACT_BUTTONS = [
    [InlineKeyboardButton("📞 الهاتف", callback_data='contact_phone')],
    [InlineKeyboardButton("📧 البريد الإلكتروني", callback_data='contact_email')],
    [InlineKeyboardButton("📍 العنوان", callback_data='contact_address')],
    [InlineKeyboardButton("💬 واتساب", callback_data='contact_whatsapp')],
    [InlineKeyboardButton("📲 تيليجرام", callback_data='contact_telegram')],
    [InlineKeyboardButton("🌐 الموقع الإلكتروني", callback_data='contact_website')]
]


# التعامل مع الضغط على الأزرار
async def button_click(update: Update, context):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "about":
        await query.message.reply_text(
            "🏛 **عن بيت الكاريكاتير العراقي**\nنؤمن بقوة الفن الساخر في صناعة التغيير منذ عام 2005. ندعم المواهب وننظم الندوات العالمية!")
    elif data == "events":
        await query.message.reply_text("🗓 **الفعاليات القادمة:**\n" + "\n".join(EVENTS))
    elif data == "competitions":
        await query.message.reply_text("🏆 **المسابقات القادمة:**\n" + "\n".join(COMPETITIONS))
    elif data == "achievements":
        await query.message.reply_text("🌟 **إنجازاتنا:**\n" + "\n".join(ACHIEVEMENTS))
    elif data == "social_media":
        text = "🌍 **وسائل التواصل الاجتماعي:**\n"
        for platform, url in SOCIAL_MEDIA.items():
            text += f"[{platform}]({url})\n"
        await query.message.reply_text(text, parse_mode="Markdown")
    elif data == "contact":
        reply_markup = InlineKeyboardMarkup(CONTACT_BUTTONS)
        await query.message.reply_text("📞 **وسائل التواصل**\nاختر طريقة التواصل المناسبة لك:",
                                       reply_markup=reply_markup)
    elif data == "contact_phone":
        await query.message.reply_text("📱 هاتف: +964 770 123 4567")
    elif data == "contact_email":
        await query.message.reply_text("✉️ البريد: info@example.com")
    elif data == "contact_address":
        await query.message.reply_text("📍 العنوان: بغداد، شارع الفن، بناية 12")
    elif data == "contact_whatsapp":
        await query.message.reply_text("💬 واتساب: https://wa.me/9647701234567")
    elif data == "contact_telegram":
        await query.message.reply_text("📲 تيليجرام: https://t.me/example")
    elif data == "contact_website":
        await query.message.reply_text("🌐 الموقع الإلكتروني: https://example.com")


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.run_polling()


if __name__ == "__main__":
    main()
