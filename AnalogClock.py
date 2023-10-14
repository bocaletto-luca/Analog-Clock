# Author: Bocaletto Luca
# Web Site: https://www.elektronoide.it
# Software Name: Analog Clock
import sys
from PySide6.QtCore import QPoint, QTimer, Qt, QTime
from PySide6.QtGui import QColor, QFont, QGradient, QGuiApplication, QPainter, QPolygon, QRasterWindow
from PySide6.QtWidgets import QApplication
from datetime import datetime

# Definizione delle costanti
HOUR_HAND_POLYGON = QPolygon([QPoint(5, 5), QPoint(-5, 5), QPoint(0, -50)])  # Lancetta delle ore
MINUTE_HAND_POLYGON = QPolygon([QPoint(3, 3), QPoint(-3, 3), QPoint(0, -70)])  # Lancetta dei minuti
HOUR_COLOR = QColor(43, 240, 251)  # Colore per la lancetta delle ore
MINUTE_COLOR = QColor(242, 227, 7)  # Colore per la lancetta dei minuti
BACKGROUND_COLOR = QGradient.PlumBath

class AnalogClockWindow(QRasterWindow):

    def __init__(self):
        super().__init__()
        self.setTitle("Analog Clock")
        self.resize(300, 300)  # Dimensioni maggiori

        self._timer = QTimer(self)
        self._timer.timeout.connect(self.update)
        self._timer.start(1000)

    def paintEvent(self, e):
        with QPainter(self) as p:
            self.render(p)

    def render(self, p):
        width = self.width()
        height = self.height()

        p.fillRect(0, 0, width, height, BACKGROUND_COLOR)

        p.setRenderHint(QPainter.Antialiasing)
        p.translate(width / 2, height / 2)

        side = min(width, height)
        p.scale(side / 200.0, side / 200.0)

        current_time = self.getCurrentTime()

        # Disegna le tacche delle decine dei minuti sull'orologio
        p.setPen(MINUTE_COLOR)
        for i in range(0, 60):
            p.save()
            p.rotate(6.0 * i)
            if i % 5 == 0:
                p.drawLine(0, -70, 0, -80)  # Tacche delle decine dei minuti
            else:
                p.drawLine(0, -75, 0, -80)  # Tacche dei minuti
            p.restore()

        # Disegna i numeri delle ore sull'orologio
        p.setPen(HOUR_COLOR)
        font = QFont("Arial", 14)  # Testo più grande
        p.setFont(font)
        for i in range(1, 13):
            p.save()
            p.rotate(30.0 * i)
            p.translate(0, -90)  # Posiziona i numeri all'esterno dell'orologio con spaziatura
            p.drawText(-10, 8, str(i))
            p.restore()

        # Disegna la lancetta delle ore
        p.save()
        p.rotate(30.0 * (current_time.hour() + current_time.minute() / 60.0))
        p.setBrush(HOUR_COLOR)
        p.drawConvexPolygon(HOUR_HAND_POLYGON)
        p.restore()

        # Disegna la lancetta dei minuti
        p.save()
        p.rotate(6.0 * (current_time.minute() + current_time.second() / 60.0))
        p.setBrush(MINUTE_COLOR)
        p.drawConvexPolygon(MINUTE_HAND_POLYGON)
        p.restore()

    def getCurrentTime(self):
        return QTime.currentTime()

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    clock = AnalogClockWindow()
    clock.show()
    sys.exit(app.exec())
