import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class TuxWalk(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.X11BypassWindowManagerHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(0, 850, 500, 170)
        
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 500, 170)
        self.label.setMouseTracking(True)
        self.label.mousePressEvent = self.on_mouse_press
        
        self.direction = 15
        self.i = 0
        self.walk_movie = QMovie("image/tuxwalk.gif")
        self.hey_movie = QMovie("image/tux02.gif")
        self.label.setMovie(self.walk_movie)
        self.walk_movie.start()
        self.walk_movie.jumpToFrame(0)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(150)
        
    def update_animation(self):
        if self.i >= 375:
            self.direction = -15
        elif self.i <= 15:
            self.direction = 15
        self.i += self.direction
        self.label.move(self.i, 0)
        
    def on_mouse_press(self, event):
        self.timer.stop()
        self.label.setMovie(self.hey_movie)
        self.hey_movie.start()
        self.hey_movie.frameChanged.connect(self.stop_hey)

    def stop_hey(self):
        if self.hey_movie.currentFrameNumber() == self.hey_movie.frameCount() - 1:
            self.hey_movie.stop()
            self.label.setMovie(self.walk_movie)
            self.timer.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tux_walk = TuxWalk()
    tux_walk.show()
    sys.exit(app.exec_())
