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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrinterStatusApp()
    sys.exit(app.exec_())
