import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, QTextEdit, QCheckBox
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

        self.plot_button = QPushButton("Plot Data", self)
        self.plot_button.clicked.connect(self.plot_data)

        self.search_bar = QLineEdit()
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.on_search)

        self.dark_mode_checkbox = QCheckBox("Dark Mode")
        self.dark_mode_checkbox.stateChanged.connect(self.toggle_dark_mode)

        self.tabs = QTabWidget()

        self.tab_basic_info = QWidget()
        self.tab_basic_info.layout = QVBoxLayout(self.tab_basic_info)
        self.tab_basic_info.layout.addWidget(QLabel("Basic Information"))
        self.tab_basic_info.layout.addWidget(QLabel("This is where basic information goes."))
        self.tabs.addTab(self.tab_basic_info, "Basic Info")

        self.tab_analytics = QWidget()
        self.tab_analytics.layout = QVBoxLayout(self.tab_analytics)
        self.matplotlib_canvas = MatplotlibCanvas(self.tab_analytics, width=5, height=4, dpi=100)
        self.tab_analytics.layout.addWidget(self.matplotlib_canvas)
        self.tabs.addTab(self.tab_analytics, "Analytics")

        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.search_bar)
        layout.addWidget(self.search_button)
        layout.addWidget(self.dark_mode_checkbox)
        layout.addWidget(self.tabs)
        layout.addWidget(self.label_title)
        layout.addWidget(self.plot_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def plot_data(self):
        dummy_data = self.data_processor.generate_dummy_data()
        processed_data = self.data_processor.perform_calculation(dummy_data)
        self.matplotlib_canvas.plot_data(processed_data)

    def on_search(self):
        search_text = self.search_bar.text()
        analytics_result = f"Analytics result for '{search_text}':\nSome meaningful data here."
        self.text_analytics_result.setPlainText(analytics_result)

    def toggle_dark_mode(self, state):
        if state == 2:
            dark(self.app)
            plt.style.use('dark_background')
        else:
            light(self.app)
            plt.style.use('default')

    def on_search(self):
        search_text = self.search_bar.text()
        # Simulate data analytics result
        analytics_result = f"Analytics result for '{search_text}':\nSome meaningful data here."
        self.text_analytics_result.setPlainText(analytics_result)

    def toggle_dark_mode(self, state):
        if state == 2:  # 2 corresponds to checked
            dark(self.app)
        else:
            light(self.app)

    def get_stock_prices(self):
        # Placeholder function to simulate fetching stock prices
        # Replace this with your actual web scraping logic
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        url = 'https://finance.yahoo.com/quote/NXT'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        price = soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
        change = soup.find('fin-streamer', {'class':'Fw(500) Pstart(8px) Fz(24px)'}).text

        return {
            "AAPL": 150.25,
            "GOOGL": 2700.50,
            "MSFT": 300.75,
            # Add more stock symbols and prices as needed
        }

    def update_price_display(self, stock_prices):
        # Clear the text widget
        # self.price_display.delete(1.0, tk.END)

        # Update the text widget with the stock prices
        for symbol, price in stock_prices.items():
            pass
            # self.price_display.insert(tk.END, f"{symbol}: ${price:.2f}\n")


class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor='black')
        self.axes = fig.add_subplot(111)

        # Set the face color of the subplot to black
        self.axes.set_facecolor('black')

        super().__init__(fig)
        self.setParent(parent)


    def plot_data(self, data):
        self.axes.clear()
        self.axes.plot(data, 'r-')
        # self.axes.
        self.axes.set_title('Processed Data')
        self.axes.set_xlabel('X-Axis Label')
        self.axes.set_ylabel('Y-Axis Label')
        # Set the color of grid, ticks, and labels to white
        self.axes.grid(True, color='white', linestyle='--', linewidth=0.5)
        self.axes.tick_params(axis='both', colors='white')
        self.axes.xaxis.label.set_color('white')
        self.axes.yaxis.label.set_color('white')
        self.figure.tight_layout()
        self.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernWindow(DashboardApp(app))
    window.app = app
    window.show()
    sys.exit(app.exec())
