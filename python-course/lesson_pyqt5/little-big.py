import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class LittleBig(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.__increment = True

        self.initUi()
        self.initSignals()

    def initUi(self):
        self.resize(400, 400)

        self.setMinimumSize(300, 300)
        self.setMaximumSize(600, 600)

        self.btn = QPushButton('We wil push the button', self)

        self.setCentralWidget(self.btn)

    def initSignals(self):
        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        """Обработчик сигнала - в Qt называется слот."""
        if self.__increment:
            self.resize(self.width() + 10, self.height() + 10)
        else:
            self.resize(self.width() - 10, self.height() - 10)

        if self.width() <= self.minimumWidth():
            self.__increment = True

        if self.width() >= self.maximumWidth():
            self.__increment = False


if __name__ == '__main__':
    app = QApplication(sys.argv)  
    q = LittleBig()
    q.show()
    sys.exit(app.exec_())
