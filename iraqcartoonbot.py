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
        # روابط وسائل التواصل الاجتماعي
        facebook_link = "https://www.facebook.com/iraqcartoon"
        twitter_link = "https://twitter.com/iraqcartoon"
        instagram_link = "https://www.instagram.com/iraqcartoon"
        # youtube_link = "https://www.youtube.com/@iraqcartoon"
        # linkedin_link = "https://www.linkedin.com/company/iraqcartoon"
        photo_url = "photos/site.jpg"  # استبدل برابط الصورة المناسبة
        # النص المدمج مع الروابط
        caption = (
            "🌍 **تابعنا على وسائل التواصل الاجتماعي!**\n"
            "📲 كن جزءًا من عائلتنا الرقمية وابقَ على اطلاع دائم بأحدث الأخبار، الفعاليات، والعروض الحصرية! 🚀✨\n\n\n"

            "📘 **فيسبوك - عالمنا بين يديك!**\n"
            "🎭 تابع آخر التحديثات والفعاليات مباشرة على صفحتنا.\n"
            f"🔗 **انضم إلينا الآن:** [اضغط هنا]({facebook_link})\n\n\n"

            "🐦 **تويتر (إكس) - كن في قلب الحدث!**\n"
            "📰 تابعنا لتكون أول من يعرف عن أحدث الأخبار والتحديثات الفورية.\n"
            f"🔗 **تابعنا على تويتر:** [اضغط هنا]({twitter_link})\n\n\n"

            "📸 **إنستجرام - لحظات ملهمة، صور مذهلة!**\n"
            "📷 استمتع بأجمل اللقطات وتفاعل مع محتوى حصري يوميًا.\n"
            f"🔗 **اكتشف عالمنا البصري:** [اضغط هنا]({instagram_link})\n\n\n")
            # "▶️ **يوتيوب:**\n"
            # f"🔗 اشترك في قناتنا على يوتيوب: [اضغط هنا]({youtube_link})\n\n\n"
            # "💼 **لينكدإن:**\n"
            # f"🔗 تابعنا على لينكدإن: [اضغط هنا]({linkedin_link})\n\n\n")

        # إرسال الرسالة مع الصورة
        await query.message.reply_photo(photo=photo_url, caption=caption, parse_mode="Markdown")

    #     contact
    elif data == "contact":
        # البيانات الخاصة بكل قسم
        phone_number = "+9647701409810"
        whatsapp_link = f"https://wa.me/9647701409810"
        telegram_link = "https://t.me/iraqcartoon"
        website_link = "https://iraqevents.site"
        location_link = "https://maps.app.goo.gl/xwUb2YuVBQ3H6LcZA"
        email = "info@iraqcartoon.iq"

        photo_url = "photos/whatsapp.jpg"  # استبدل برابط الصورة المناسبة

        # النص المدمج مع الروابط
        caption = (
            "📱 **هاتفنا:**\n"
            f"يمكنك الاتصال بنا مباشرة على الرقم التالي:\n اضغط للاتصال{phone_number}\n\n\n"

            "✉️ **البريد الإلكتروني:**\n"
            f"يمكنك مراسلتنا عبر البريد الإلكتروني: {email}\n\n\n"

            "📍 **العنوان:**\n"
            "بغداد، زيونة، شارع الربيعي,مجاور جامع القزاز\n"
            f"📌 **موقعنا على الخريطة:** {location_link}\n\n\n"

            "💬 **تواصل معنا على واتساب!**\n"
            f"📱 هل لديك استفسار؟ نحن هنا لمساعدتك! يمكنك مراسلتنا مباشرة عبر واتساب.\n"
            f"🔗 **رابط واتساب:** [اضغط هنا]({whatsapp_link})\n\n\n"

            "📢 **انضم إلينا على تيليجرام!**\n"
            "📲 كن على اطلاع دائم بأحدث الفعاليات والأخبار.\n"
            "تابع قناتنا الرسمية وكن جزءًا من مجتمعنا. 🚀\n"
            f"🔗 **رابط القناة:** [اضغط هنا]({telegram_link})\n\n\n"

            "🔗 **مرحبًا بك في منصتنا!**\n"
            "🌐 اكتشف جميع الفعاليات والأنشطة المميزة في العراق عبر موقعنا الإلكتروني.\n"
            "لا تفوّت أي حدث مهم!\n"
            f"📲 قم بزيارتنا الآن: [اضغط هنا]({website_link})\n\n\n"
        )

        # إرسال الرسالة مع الصورة
        await query.message.reply_photo(photo=photo_url, caption=caption, parse_mode="Markdown")

    # elif data == "contact_phone":
    #     phone_number = "+9647701234567"
    #     photo_url = "photos/phone.jpg"  # استبدل برابط صورة مناسبة
    #     caption = (
    #         "📱 **هاتفنا:**\n"
    #         "يمكنك الاتصال بنا مباشرة على الرقم التالي:\n"
    #         "[اضغط للاتصال]\n\n"
    #         f"[{phone_number}]\n\n"
    #         "لا تتردد في الاتصال بنا إذا كان لديك أي استفسار."
    #     )
    #     await query.message.reply_photo(photo=photo_url, caption=caption, parse_mode="Markdown")
    #
    # elif data == "contact_email":
    #     email = "info@iraqcartoon.iq"
    #     photo_url = "photos/email.jpg"  # استبدل برابط صورة مناسبة
    #     caption = (
    #         "✉️ **البريد الإلكتروني:**\n"
    #         f"يمكنك مراسلتنا عبر البريد الإلكتروني: {email}\n\n"
    #         "نحن هنا للإجابة على استفساراتك ومساعدتك في أي وقت."
    #     )
    #     await query.message.reply_photo(photo=photo_url, caption=caption, parse_mode="Markdown")
    #
    # elif data == "contact_address":
    #     location_link = "https://maps.app.goo.gl/xwUb2YuVBQ3H6LcZA"
    #     photo_url = "photos/maps.jpg"  # استبدل برابط صورة الموقع أو شعار مؤسستك
    #     caption = (
    #     "📍 **العنوان:**\n"
    #     "بغداد، زيونة، شارع الربيعي\n"
    #     "مجاور جامع القزاز\n\n"
    #     "📌 **موقعنا على الخريطة:**\n" + location_link
    #     )
    #     await query.message.reply_photo(photo=photo_url, caption=caption, parse_mode="Markdown")
    #
    # elif data == "contact_whatsapp":
    #     whatsapp_link = f"https://wa.me/9647701409810?"
    #     photo_url = "photos/whatsapp.jpg"  # استبدل برابط الصورة الفعلي
    #     caption = (
    #             "💬 **تواصل معنا على واتساب!**\n\n"
    #             "📱 هل لديك استفسار؟ نحن هنا لمساعدتك! يمكنك مراسلتنا مباشرة عبر واتساب.\n\n"
    #             "🔗 **رابط واتساب:** [اضغط هنا](%s)" % whatsapp_link
    #     )
    #     await query.message.reply_photo(photo=photo_url, caption=caption, parse_mode="Markdown")
    #
    # elif data == "contact_telegram":
    #     telegram_link = "https://t.me/iraqcartoon"
    #     photo_url = "photos/tg_ch.jpg"  # استبدل برابط الصورة الفعلي
    #     caption = (
    #             "📢 **انضم إلينا على تيليجرام!**\n\n"
    #             "📲 كن على اطلاع دائم بأحدث الفعاليات والأخبار.\n"
    #             "تابع قناتنا الرسمية وكن جزءًا من مجتمعنا. 🚀\n\n"
    #             "🔗 **رابط القناة:** [اضغط هنا](%s)" % telegram_link
    #     )
    #     await query.message.reply_photo(photo=photo_url, caption=caption, parse_mode="Markdown")
    #
    #
    # elif data == "contact_website":
    #     website_link = "https://iraqevents.site"
    #     photo_url = "photos/site.jpg"  # استبدل برابط الصورة الفعلي
    #     caption = (
    #             "🔗 **مرحبًا بك في منصتنا!**\n\n"
    #             "🌐 اكتشف جميع الفعاليات والأنشطة المميزة في العراق عبر موقعنا الإلكتروني.\n"
    #             "لا تفوّت أي حدث مهم!\n\n"
    #             "📲 قم بزيارتنا الآن: [اضغط هنا](%s)" % website_link
    #     )
    #     await query.message.reply_photo(photo=photo_url, caption=caption, parse_mode="Markdown")


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.run_polling()


if __name__ == "__main__":
    main()
