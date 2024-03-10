# **🇬🇧 Explanation in the English language**

## 🖨️ Überprüfung des Druckerstatus

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

| File / Folder Path       | Description |
|--------------------------|-------------|
| `main.py`                | Main file to run the application |
| `style.css`              | Custom CSS styles for the GUI |
| `assets/`                | Folder for graphic and audio resources |
| `assets/icon.png`        | Program icon |
| `assets/alert.wav`       | Audio file for alert notifications |
| `data/`                  | Data folder |
| `data/sample.csv`        | Sample file for testing |
| `printer_report.py`      | Module for printer status reporting |
| `README.md`              | Project documentation and instructions |

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

| مسیر فایل / پوشه        | توضیحات |
|-------------------------|---------|
| `main.py`               | فایل اصلی اجرای برنامه |
| `style.css`             | استایل سفارشی رابط گرافیکی |
| `assets/`               | پوشه فایل‌های گرافیکی و صوتی |
| `assets/icon.png`       | آیکن برنامه |
| `assets/alert.wav`      | فایل آلارم صوتی |
| `data/`                 | پوشه داده‌ها |
| `data/sample.csv`       | فایل نمونه برای تست |
| `printer_report.py`     | ماژول گزارش‌گیری از پرینترها |
| `README.md`             | فایل توضیحات پروژه |


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
