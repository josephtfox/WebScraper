import sys
# import PyQt6 
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QLineEdit, QTabWidget, QTextEdit, QCheckBox
from PyQt6.QtCore import Qt
from qtmodern.styles import dark, light
from qtmodern.windows import ModernWindow

import requests
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

import finnhub


class DataProcessor:
    @staticmethod
    def generate_dummy_data():
        return np.random.rand(10)

    @staticmethod
    def perform_calculation(data):
        return data * 2


class DashboardApp(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.setWindowTitle("Data Analytics Dashboard")
        self.setGeometry(100, 100, 800, 600)

        self.label_title = QLabel("Data Analytics Dashboard")
        self.label_title.setStyleSheet("font-size: 20pt; margin-bottom: 20px;")

        self.data_processor = DataProcessor()

        # Navigation Bar
        self.dashboard_btn = QPushButton("Dashboard", self)
        self.dashboard_btn.clicked.connect(self.dashboard_btn_clicked)

        self.clusters_btn = QPushButton("Clusters", self)
        self.clusters_btn.clicked.connect(self.clusters_btn_clicked)

        self.activity_btn = QPushButton("Activity", self)
        self.activity_btn.clicked.connect(self.activity_btn_clicked)

        self.discovery_btn = QPushButton("Discovery", self)
        self.discovery_btn.clicked.connect(self.discovery_btn_clicked)

        self.statistics_btn = QPushButton("Statistics", self)
        self.statistics_btn.clicked.connect(self.statistics_btn_clicked)


        layout = QGridLayout()
        layout.addWidget(self.dashboard_btn, 1,0)
        layout.addWidget(self.clusters_btn, 1,0)
        layout.addWidget(self.activity_btn, 1,0)
        layout.addWidget(self.discovery_btn, 1,0)
        layout.addWidget(self.statistics_btn, 1,0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def dashboard_btn_clicked():
        pass

    def clusters_btn_clicked():
        pass

    def activity_btn_clicked():
        pass

    def discovery_btn_clicked():
        pass

    def statistics_btn_clicked():
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernWindow(DashboardApp(app))
    window.app = app
    window.show()
    sys.exit(app.exec())