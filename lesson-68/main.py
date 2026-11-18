# PyQt5 Images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 QLabel Example")
        self.setGeometry(100, 100, 600, 400)

        # Create a QLabel widget
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)  # Position the label in the window

        pixmap = QPixmap("lesson-68/picture.jpg")  # Load the image
        label.setPixmap(pixmap)  # Set the pixmap to the label
        label.setScaledContents(True)  # Scale the image to fit the label size

        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2, 
                          label.width(), 
                          label.height())

def main():
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
