import sys, time
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QApplication, QLineEdit, QLabel
from PyQt5.QtCore import QSize, Qt, QLine, QPoint, QRect, pyqtSlot
from PyQt5.QtGui import QPainter, QPen, QBrush, QPixmap, QFont, QColor, QIcon
from PyQt5.QtCore import QThread, pyqtSignal

class Bod: #vytvoreni tridy pro bod
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Kolecko(): #trida s nazvem Kolecko
    stred = Bod(0,0)
    polomer = 0
    def __init__(self, stred, polomer):
        self.stred = stred
        self.polomer = polomer

class MainWindow(QMainWindow): #QMainWindow je objekt z Qt - je to rodic odvozovane tridy MainWindow

    def __init__(self):
        super().__init__()
        self.title = 'rut0018 - projekt'
        self.setMinimumSize(QSize(800, 600)) #nastaveni velikosti formulare
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        #vytvoreni a nastaveni jednotlivých tlacitek na formulari
        bod_X = QLabel('X-ova souřadnice:', self)
        bod_X.move(10, 10)
        self.H_bod_X = QLineEdit('400', self)
        self.H_bod_X.move(130, 10)

        bod_Y = QLabel('Y-ova souřadnice:', self)
        bod_Y.move(10, 50)
        self.H_bod_Y = QLineEdit('200', self)
        self.H_bod_Y.move(130, 50)

        polomer = QLabel('Poloměr:', self)
        polomer.move(10, 90)
        self.H_polomer = QLineEdit('200', self)
        self.H_polomer.move(130, 90)

        self.circle = None
        self.point_circle = None
        self.point_stred = None

        buttonCircle = QPushButton('Vykreslit', self)
        buttonCircle.clicked.connect(self.draw_circle)
        buttonCircle.resize(100, 20)
        buttonCircle.move(60, 130)

        ZM_polomer = QLabel('Násobek poloměru:', self)
        ZM_polomer.move(10, 170)
        self.H_ZM_polomer = QLineEdit('1', self)
        self.H_ZM_polomer.move(130, 170)

        buttonCircle = QPushButton('Změnit poloměr', self)
        buttonCircle.clicked.connect(self.change_polomer)
        buttonCircle.resize(100, 20)
        buttonCircle.move(60, 210)

        self.show()

    def draw_circle(self): #metoda pro vykresleni kolecka
        polomer = int(self.H_polomer.text())
        sur_X_bod = int(self.H_bod_X.text())
        sur_Y_bod = int(self.H_bod_Y.text())
        sur_X = int(self.H_bod_X.text()) - polomer/2
        sur_Y = int(self.H_bod_Y.text()) - polomer/2

        self.point_stred = Bod(sur_X_bod, sur_Y_bod)
        self.point_circle = Bod(sur_X, sur_Y)
        self.circle = Kolecko(self.point_circle, polomer)
        self.update()

    def change_polomer(self): #metoda pro zmenu polomeru
        polomer = int(self.H_polomer.text())
        nasobek = self.H_ZM_polomer.text()

        if ',' in nasobek:
            nasobek = nasobek.replace(",", ".")
        else:
            nasobek = nasobek

        new_polomer = polomer * float(nasobek)
        sur_X = int(self.H_bod_X.text()) - new_polomer / 2
        sur_Y = int(self.H_bod_Y.text()) - new_polomer / 2
        self.point_circle = Bod(sur_X, sur_Y)
        self.circle = Kolecko(self.point_circle, new_polomer)
        self.update()


    def paintEvent(self, e): #metoda, ktera se spusti pri prekresleni formulare
        qp = QPainter() #vytvoreni instance objektu QPainter
        qp.begin(self)
        if not self.circle is None:
            pen = QPen(Qt.blue, 5) #vytvoreni instance objektu QPen - nastavenin barvy a tloustky pera pro kolecko
            qp.setPen(pen) #prirazeni pera Painteru
            qp.drawEllipse(self.circle.stred.x, self.circle.stred.y, self.circle.polomer, self.circle.polomer)
        if not self.point_stred is None:
            pen = QPen(Qt.red, 5) #vytvoreni instance objektu QPen - nastavenin barvy a tloustky pera pro stred
            qp.setPen(pen) #prirazeni pera Painteru
            qp.drawPoint(self.point_stred.x, self.point_stred.y)
        qp.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)  #vytvoreni (systemove) aplikace
    ex = MainWindow() #zobrazeni formulare
    sys.exit(app.exec_())  #ukonceni aplikace s formularem - uzavreni formulare