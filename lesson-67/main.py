# PyQt5 Labels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 QLabel Example")
        self.setGeometry(100, 100, 600, 400)

        # Create a QLabel widget
        label = QLabel("Hello!", self)
        label.setFont(QFont("Arial", 20))  # Set the font and size
        label.setGeometry(0, 0, 600, 100)  # Position the label in the window
        label.setStyleSheet("color: blue;"
                            "background-color: lightgray;"
                            "font-weight: bold;"
                            "font-style: italic;")
        label.setAlignment(Qt.AlignCenter)  # Center the text within the label

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
