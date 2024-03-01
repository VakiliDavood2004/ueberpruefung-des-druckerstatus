import csv
import os
def analyze_printers(csv_path, language="فارسی"):
    translations = {
                "فارسی": {
            "healthy_title": "✅ پرینترهای سالم:",
            "faulty_title": "❌ پرینترهای دارای ایراد:",
            "paper": "کاغذ",
            "ink": "جوهر",
            "toner": "تونر",
            "board": "برد",
            "none": "هیچ‌کدام",
            "error": "خطا در خواندن فایل CSV:"
        },
        "English": {
            "healthy_title": "✅ Healthy Printers:",
            "faulty_title": "❌ Faulty Printers:",
            "paper": "Paper",
            "ink": "Ink",
            "toner": "Toner",
            "board": "Board",
            "none": "None",
            "error": "Error reading CSV file:"
        },
        "Deutsch": {
            "healthy_title": "✅ Funktionierende Drucker:",
            "faulty_title": "❌ Drucker mit Fehlern:",
            "paper": "Papier",
            "ink": "Tinte",
            "toner": "Toner",
            "board": "Platine",
            "none": "Keine",
            "error": "Fehler beim Lesen der CSV-Datei:"

    }

    lang = translations.get(language, translations["فارسی"])

    if not os.path.exists(csv_path):
        return lang["error"] + "\n" + csv_path
