# printer_report.py

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
    }

    lang = translations.get(language, translations["فارسی"])

    if not os.path.exists(csv_path):
        return lang["error"] + "\n" + csv_path

    try:
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            healthy = []
            faulty = []

            for row in reader:
                name = row.get("PrinterName", "Unbekannt")
                faults = []
                if row.get("Paper", "False").lower() != "true":
                    faults.append(lang["paper"])
                if row.get("Ink", "False").lower() != "true":
                    faults.append(lang["ink"])
                if row.get("Toner", "False").lower() != "true":
                    faults.append(lang["toner"])
                if row.get("Board", "False").lower() != "true":
                    faults.append(lang["board"])

                if faults:
                    faulty.append(f"{name}: {', '.join(faults)}")
                else:
                    healthy.append(name)

            report = lang["healthy_title"] + "\n" + ("\n".join(healthy) if healthy else lang["none"]) + "\n\n"
            report += lang["faulty_title"] + "\n" + ("\n".join(faulty) if faulty else lang["none"])
            return report

    except Exception as e:
        return f"{lang['error']}\n{str(e)}"
