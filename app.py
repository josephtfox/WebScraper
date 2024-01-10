import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTabWidget, QTextEdit, QCheckBox
from PyQt6.QtCore import Qt
from qtmodern.styles import dark, light
from qtmodern.windows import ModernWindow
import requests
from bs4 import BeautifulSoup
import finnhub

class DashboardApp(QMainWindow):
    def __init__(self, app):
        # Used to call the constructor of the parent class in this case QMainWindow
        super().__init__()

        self.app = app  # Store the app instance

        self.setWindowTitle("Data Analytics Dashboard")
        self.setGeometry(100, 100, 800, 600)

        # Create widgets
        self.label_title = QLabel("Data Analytics Dashboard")
        self.label_title.setStyleSheet("font-size: 20pt; margin-bottom: 20px;")

        self.label_name = QLabel("Enter your name:")
        self.entry = QLineEdit()

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.on_button_click)

        self.label_result = QLabel()

        # Search bar
        self.search_bar = QLineEdit()
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.on_search)

        # Dark mode switch
        self.dark_mode_checkbox = QCheckBox("Dark Mode")
        self.dark_mode_checkbox.stateChanged.connect(self.toggle_dark_mode)

        # Tab Widget
        self.tabs = QTabWidget()

        # Basic Information Tab
        self.tab_basic_info = QWidget()
        self.tab_basic_info.layout = QVBoxLayout(self.tab_basic_info)
        self.tab_basic_info.layout.addWidget(QLabel("Basic Information"))
        self.tab_basic_info.layout.addWidget(QLabel("This is where basic information goes."))
        self.tabs.addTab(self.tab_basic_info, "Basic Info")

        # Analytics Tab
        self.tab_analytics = QWidget()
        self.tab_analytics.layout = QVBoxLayout(self.tab_analytics)
        self.tab_analytics.layout.addWidget(QLabel("Analytics"))
        self.text_analytics_result = QTextEdit()
        self.tab_analytics.layout.addWidget(self.text_analytics_result)
        self.tabs.addTab(self.tab_analytics, "Analytics")

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.label_name)
        layout.addWidget(self.entry)
        layout.addWidget(self.button_submit)
        layout.addWidget(self.label_result)
        layout.addWidget(self.search_bar)
        layout.addWidget(self.search_button)
        layout.addWidget(self.dark_mode_checkbox)
        layout.addWidget(self.tabs)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_button_click(self):
        entry_text = self.entry.text()
        self.label_result.setText(f"Hello, {entry_text}!")

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernWindow(DashboardApp(app))
    window.app = app  # Pass the app instance to the window
    window.show()
    sys.exit(app.exec())
