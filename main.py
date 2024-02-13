import sys
import csv
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox,
    QGridLayout, QWidget, QGroupBox, QFileDialog, QDialog, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtMultimedia import QSound
from Druckerbericht import analyze_printers

class LanguageSelector(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprache wählen / Select Language / انتخاب زبان")
        self.setFixedSize(300, 150)
        layout = QVBoxLayout()
        label = QLabel("Bitte wählen Sie eine Sprache:\nPlease select a language:\nلطفاً یک زبان انتخاب کنید:")
        label.setObjectName("languageLabel")
        layout.addWidget(label)
        self.language_combobox = QComboBox()
        self.language_combobox.addItems(["Deutsch", "English", " فارسی"])
        self.language_combobox.setObjectName("languageCombo")
        layout.addWidget(self.language_combobox)
        self.ok_button = QPushButton("OK")
        self.ok_button.setObjectName("languageButton")
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)
        self.load_stylesheet()

    def load_stylesheet(self):
        css_path = os.path.join(os.path.dirname(__file__), "style.css")
        try:
            with open(css_path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim Laden style.css:\n{str(e)}")
            sys.exit(1)

    def get_selected_language(self):
        return self.language_combobox.currentText()

class ClickableLineEdit(QLineEdit):
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        file_path, _ = QFileDialog.getOpenFileName(self, "CSV-Datei auswählen", "", "CSV Datei (*.csv);;All Files (*)")
        if file_path:
            self.setText(file_path)

class PrinterStatusApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Überprüfung des Druckerstatus")
        self.setMinimumWidth(450)
        self.last_status_ok = True
        language_dialog = LanguageSelector()
        if language_dialog.exec_() == QDialog.Accepted:
            self.selected_language = language_dialog.get_selected_language()
        else:
            sys.exit()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QGridLayout()

        # Dateieinstellungen
        file_group = QGroupBox()
        file_layout = QGridLayout()
        self.file_label = QLabel()
        self.file_entry = ClickableLineEdit()
        self.load_button = QPushButton()
        self.load_button.clicked.connect(self.load_printers)
        file_layout.addWidget(self.file_label, 0, 0)
        file_layout.addWidget(self.file_entry, 0, 1)
        file_layout.addWidget(self.load_button, 0, 2)
        file_group.setLayout(file_layout)
        self.main_layout.addWidget(file_group, 0, 0, 1, 2)

        # Druckerauswahl
        printer_group = QGroupBox()
        printer_layout = QGridLayout()
        self.printer_label = QLabel()
        self.printer_combobox = QComboBox()
        self.status_label = QLabel("Overall Status: Unknown")
        self.status_label.setAlignment(Qt.AlignCenter)
        printer_layout.addWidget(self.printer_label, 0, 0)
        printer_layout.addWidget(self.printer_combobox, 0, 1)
        printer_layout.addWidget(self.status_label, 1, 0, 1, 2)
        printer_group.setLayout(printer_layout)
        self.main_layout.addWidget(printer_group, 1, 0, 1, 2)

        # Detaillierter Status
        details_group = QGroupBox()
        details_layout = QGridLayout()
        self.paper_label = QLabel()
        self.ink_label = QLabel()
        self.toner_label = QLabel()
        self.board_label = QLabel()
        self.paper_status_label = QLabel("")
        self.ink_status_label = QLabel("")
        self.toner_status_label = QLabel("")
        self.board_status_label = QLabel("")
        details_layout.addWidget(self.paper_label, 0, 0)
        details_layout.addWidget(self.paper_status_label, 0, 1)
        details_layout.addWidget(self.ink_label, 0, 2)
        details_layout.addWidget(self.ink_status_label, 0, 3)
        details_layout.addWidget(self.toner_label, 1, 0)
        details_layout.addWidget(self.toner_status_label, 1, 1)
        details_layout.addWidget(self.board_label, 1, 2)
        details_layout.addWidget(self.board_status_label, 1, 3)
        details_group.setLayout(details_layout)
        self.main_layout.addWidget(details_group, 2, 0, 1, 2)

        # Steuerungsschaltflächen
        self.check_button = QPushButton()
        self.check_button.clicked.connect(self.check_printer_status)
        self.main_layout.addWidget(self.check_button, 3, 0, 1, 2)

        self.report_button = QPushButton()
        self.report_button.clicked.connect(self.show_report)
        self.main_layout.addWidget(self.report_button, 4, 0, 1, 2)

        self.central_widget.setLayout(self.main_layout)
        self.load_stylesheet()
        self.apply_translations(file_group, printer_group, details_group)

        self.printer_list = []
        self.is_running = True
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_status_periodically)
        self.timer.start(2000)
        self.app = QApplication.instance()
        self.app.aboutToQuit.connect(self.on_closing)
        self.show()
    def load_stylesheet(self):
        css_path = os.path.join(os.path.dirname(__file__), "style.css")
        try:
            with open(css_path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim Laden  style.css:\n{str(e)}")
            sys.exit(1)
    def apply_translations(self, file_group, printer_group, details_group):
        lang = self.selected_language
        if lang == "Deutsch":
            file_group.setTitle("Dateieinstellungen")
            self.file_label.setText("CSV-Dateipfad:")
            self.load_button.setText("Drucker laden")
            printer_group.setTitle("Druckerstatus")
            self.printer_label.setText("Drucker auswählen:")
            self.check_button.setText("Status prüfen")
            self.report_button.setText("Statusbericht anzeigen")
            details_group.setTitle("Detailstatus")
            self.paper_label.setText("Papier:")
            self.ink_label.setText("Tinte:")
            self.toner_label.setText("Toner:")
            self.board_label.setText("Platine:")
        elif lang == "فارسی":
            file_group.setTitle("تنظیمات فایل")
            self.file_label.setText("مسیر فایل CSV:")
            self.load_button.setText("بارگذاری پرینترها")
            printer_group.setTitle("وضعیت پرینتر")
            self.printer_label.setText("انتخاب پرینتر:")
            self.check_button.setText("بررسی وضعیت")
            self.report_button.setText("نمایش گزارش")
            details_group.setTitle("وضعیت جزئیات")
            self.paper_label.setText("کاغذ:")
            self.ink_label.setText("جوهر:")
            self.toner_label.setText("تونر:")
            self.board_label.setText("برد:")
        else:
            file_group.setTitle("File Settings")
            self.file_label.setText("CSV File Path:")
            self.load_button.setText("Load Printers")
            printer_group.setTitle("Printer Status")
            self.printer_label.setText("Select Printer:")
            self.check_button.setText("Check Status")
            self.report_button.setText("Show Report")
            details_group.setTitle("Detailed Status")
            self.paper_label.setText("Paper:")
            self.ink_label.setText("Ink:")
            self.toner_label.setText("Toner:")
            self.board_label.setText("Board:")
    def load_printers(self):
        path = self.file_entry.text()
        try:
            with open(path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.printer_list = list(reader)
                self.printer_combobox.clear()
                self.clear_detailed_status()
                names = [printer['PrinterName'] for printer in self.printer_list]
                self.printer_combobox.addItems(names)
        except Exception as e:
            self.update_status_label("Overall Status", f"CSV Error: {str(e)}")

    def get_printer_status(self, info):
        try:
            paper = info.get('Paper', 'False').lower() == 'true'
            ink = info.get('Ink', 'False').lower() == 'true'
            toner = info.get('Toner', 'False').lower() == 'true'
            board = info.get('Board', 'False').lower() == 'true'
            return paper, ink, toner, board
        except Exception:
            return None, None, None, None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrinterStatusApp()
    sys.exit(app.exec_())
