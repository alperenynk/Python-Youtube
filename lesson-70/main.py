# PyQt5 Buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Button Example")
        self.button = QPushButton("Click Me", self)
        self.label = QLabel("Hello!", self)
        self.setGeometry(100, 100, 300, 200)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(100, 80, 100, 30)
        self.button.setStyleSheet("font-size: 16px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(100, 50, 200, 30)
        self.label.setStyleSheet("font-size: 25px; color: blue;")

    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        self.label.setText("Goodbye")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
