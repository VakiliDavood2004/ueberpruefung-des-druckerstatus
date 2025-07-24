# **🇩🇪 Erklärung in deutscher Sprache**

# 🖨️ Überprüfung des Druckerstatus

Ein grafisches Tool entwickelt mit **Python + PyQt5** zur Überwachung des Zustands mehrerer Drucker basierend auf einer CSV-Datei.  
Die Anwendung bietet eine einfache, ansprechende und mehrsprachige Benutzeroberfläche mit Unterstützung für **Deutsch, Englisch und Persisch**.

## 📌 Funktionen
- Manuelle und automatische Statusüberprüfung des ausgewählten Druckers (alle 2 Sekunden)
- Akustischer Alarm bei Statusänderung von „OK“ zu „Fehlerhaft“
- Vollständige Sprachunterstützung: Deutsch / English / فارسی
- Bericht über funktionierende und fehlerhafte Drucker in der gewählten Sprache
- Benutzeroberfläche im eigenen CSS-Stil (Qt StyleSheet)
- Einlesen der Druckerdaten aus einer standardisierten CSV-Datei

## 📁 Projektstruktur
├── main.py  
├── style.css  
├── assets/  
│   └── icon.png      # Programmsymbol  
│   └── alert.wav     # Alarmton-Datei  
├── data/  
│   └── sample.csv    # Beispieldatei zur Überprüfung  
├── printer_report.py  
└── README.md  

## 📄 Struktur der CSV-Datei
Die Datei muss folgende Spalten enthalten:

```csv
PrinterName,Paper,Ink,Toner,Board  
HP LaserJet 1020,True,True,False,True  
Canon Pixma G3000,True,False,True,True  
Epson L3150,False,True,True,True  
Brother HL-L2350,True,True,True,True  
```

Jede Spalte gibt den Status eines bestimmten Druckerkomponentenfeldes an (`True` für funktionsfähig, `False` für fehlerhaft).

## 🚀 Ausführung
1. Installation der Abhängigkeiten:
```
pip install PyQt5
```

2. Start der Anwendung:
```
python main.py
```

3. Bedienungsschritte:
- Sprache auswählen (Deutsch, Englisch, Persisch)  
- CSV-Datei laden  
- Status des ausgewählten Druckers anzeigen  
- Automatische Statusprüfung alle 2 Sekunden  
- Bericht über alle funktionierenden und fehlerhaften Drucker generieren

## 🌐 Unterstützte Sprachen
🇩🇪 Deutsch  🇬🇧 English  🇮🇷 فارسی  
Alle Texte, Schaltflächen und Berichtsformate passen sich der gewählten Sprache an.

## 📊 Beispielausgabe (Deutsch)

✅ **Funktionsfähige Drucker**  
- Brother HL-L2350  

❌ **Fehlerhafte Drucker**  
- Canon Pixma G3000 → Fehler in der Tintenpatrone  
- HP LaserJet 1020 → Fehler im Toner  
- Epson L3150 → Papierfehler  

## 🔔 Hinweise
- Die Datei `alert.wav` muss sich im Ordner `assets/` oder im selben Verzeichnis wie `main.py` befinden.  
- CSV-Dateien sollten mit **UTF-8 ohne BOM** kodiert sein.  
- Bei Fehlern wie „codec“ oder „charmap“ sollte die Codierung überprüft werden.  
- Für schnelle Tests kann die Datei `sample.csv` im Ordner `data/` verwendet werden.

## 👨‍💻 Entwickler
Dieses Projekt wurde von **Davood Vakili** konzipiert und umgesetzt – mit Fokus auf praktische PyQt5-Anwendung, modernes UI-Design und die Entwicklung eines mehrsprachigen Monitoring-Systems. Alle Schritte wurden sorgfältig und strukturiert ausgeführt, um ein professionelles und benutzerfreundliches Ergebnis zu gewährleisten.


---


# **🇬🇧 Explanation in the English language**

# 🖨️ Überprüfung des Druckerstatus

A graphical application built with **Python + PyQt5** for checking and monitoring the status of multiple printers via a CSV file.  
This tool features a clean, modern, multilingual interface supporting **English, German, and Persian**.

## 📌 Features
- Manual and automatic status checks for selected printers (every 2 seconds)
- Audible alerts when status changes from “Healthy” to “Faulty”
- Full language support: English / Deutsch / فارسی
- Detailed reports listing both working and faulty printers in the selected language
- Custom CSS-based UI styling using Qt StyleSheet
- Loads printer status data from a standard CSV file

## 📁 Project Structure
├── main.py  
├── style.css  
├── assets/  
│   └── icon.png      # Application icon  
│   └── alert.wav     # Alert sound  
├── data/  
│   └── sample.csv    # Sample CSV file for testing  
├── printer_report.py  
└── README.md  

## 📄 Input CSV File Structure
The file must contain the following columns:

```csv
PrinterName,Paper,Ink,Toner,Board  
HP LaserJet 1020,True,True,False,True  
Canon Pixma G3000,True,False,True,True  
Epson L3150,False,True,True,True  
Brother HL-L2350,True,True,True,True  
```

Each field represents the status of a printer component (`True` for working, `False` for faulty).

## 🚀 How to Run
1. Install dependencies:
```
pip install PyQt5
```

2. Start the application:
```
python main.py
```

3. Usage steps:
- Select your preferred language (English, German, Persian)  
- Load your CSV file  
- View live status of selected printers  
- Automatic checking every 2 seconds  
- Use the “Report” button to generate a list of working and faulty printers  

## 🌐 Supported Languages
🇬🇧 English  🇩🇪 Deutsch  🇮🇷 فارسی  
All interface elements, buttons, and report outputs appear in the selected language.

## 📊 Sample Report Output (English)

✅ **Healthy Printers**  
- Brother HL-L2350  

❌ **Faulty Printers**  
- Canon Pixma G3000 → Ink issue  
- HP LaserJet 1020 → Toner issue  
- Epson L3150 → Paper issue  

## 🔔 Important Notes
- The `alert.wav` file must be placed inside the `assets/` folder or next to `main.py`.  
- CSV files should be encoded in **UTF-8 without BOM**.  
- If you encounter “codec” or “charmap” errors, check the file’s encoding settings.  
- For quick testing, use the `sample.csv` file located in the `data/` folder.

## 👨‍💻 Developer
This project was designed and implemented by **Davood Vakili**, with a focus on hands-on PyQt5 development, modern GUI design, and building a multilingual monitoring system. Every component has been carefully structured and crafted to deliver a professional and user-friendly experience.


---


# **✔️ توضیحات به زبان فارسی**

# 🖨️ Überprüfung des Druckerstatus

یک برنامه گرافیکی نوشته‌شده با **Python + PyQt5** برای بررسی و مانیتور کردن وضعیت پرینترها از طریق فایل CSV.  
این ابزار دارای رابط کاربری ساده، زیبا و چندزبانه است که از **فارسی، آلمانی و انگلیسی** پشتیبانی می‌کند.

## 📌 قابلیت‌ها
- بررسی دستی و خودکار وضعیت پرینتر انتخاب‌شده (هر ۲ ثانیه)
- آلارم صوتی هنگام تغییر وضعیت از «سالم» به «خراب»
- پشتیبانی کامل از سه زبان: فارسی / Deutsch / English
- نمایش گزارش کامل از پرینترهای سالم و معیوب
- طراحی رابط گرافیکی با CSS سفارشی (Qt StyleSheet)
- بارگذاری اطلاعات از فایل CSV استاندارد

## 📁 ساختار پروژه
├── main.py  
├── style.css  
├── assets/  
│   └── icon.png      # آیکن برنامه  
│   └── alert.wav     # فایل آلارم صوتی  
├── data/  
│   └── sample.csv    # فایل نمونه برای تست  
├── printer_report.py  
└── README.md  

## 📄 ساختار فایل CSV ورودی
فایل باید شامل ستون‌های زیر باشد:

```csv
PrinterName,Paper,Ink,Toner,Board  
HP LaserJet 1020,True,True,False,True  
Canon Pixma G3000,True,False,True,True  
Epson L3150,False,True,True,True  
Brother HL-L2350,True,True,True,True  
```

هر ستون وضعیت یک بخش از پرینتر را با مقادیر `True` یا `False` نشان می‌دهد.

## 🚀 نحوه‌ی اجرا
۱. نصب پیش‌نیازها:
```
pip install PyQt5
```

۲. اجرای برنامه:
```
python main.py
```

۳. مراحل استفاده:
- انتخاب زبان (فارسی، آلمانی، انگلیسی)  
- بارگذاری فایل CSV  
- مشاهده وضعیت پرینترها  
- بررسی خودکار هر ۲ ثانیه  
- دریافت گزارش کامل از پرینترهای سالم و معیوب  

## 🌐 زبان‌های پشتیبانی‌شده
🇮🇷 فارسی  🇩🇪 Deutsch  🇬🇧 English  
تمام متن‌ها، دکمه‌ها و خروجی گزارش متناسب با زبان انتخاب‌شده نمایش داده می‌شوند.

## 📊 مثال خروجی گزارش (فارسی)
✅ **پرینترهای سالم**  
- Brother HL-L2350  

❌ **پرینترهای دارای ایراد**  
- Canon Pixma G3000 → ایراد در جوهر  
- HP LaserJet 1020 → ایراد در تونر  
- Epson L3150 → ایراد در کاغذ  

## 🔔 نکات مهم
- فایل `alert.wav` باید داخل پوشه `assets/` یا کنار `main.py` قرار گیرد.  
- فایل‌های CSV باید با کدگذاری **UTF-8 بدون BOM** ذخیره شوند.  
- در صورت بروز خطاهای مربوط به "codec" یا "charmap"، تنظیمات encoding فایل بررسی شود.  
- برای تست سریع، از `sample.csv` موجود در پوشه `data/` استفاده کنید.  

## 👨‍💻 توسعه‌دهنده
این پروژه توسط **داوود وکیلی** طراحی و پیاده‌سازی شده؛ با تمرکز بر آموزش عملی PyQt5، طراحی رابط‌های گرافیکی مدرن، و ساخت سیستم‌های مانیتورینگ چندزبانه. تمام مراحل با دقت، ساختارمند و با سلیقه اجرا شده تا تجربه‌ای حرفه‌ای و کاربردی فراهم شود.
