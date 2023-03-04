import sys
from PyQt5 import QtGui, QtCore, uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import random as r
import threading, time
from PyQt5.QtCore import pyqtSlot
from Tools.hotkeys import bind_hotkey_function, stop_hotkeys_listener
from PyQt5 import QtOpenGL
#import PySide6.QtOpenGL as QtOpenGL

import OpenGL.GL as GL        # python wrapping of OpenGL
from OpenGL import GLU        # OpenGL Utility Library, extends OpenGL functionality

from Tools.audio_noise import play_noise_1
threading.Thread(target=play_noise_1).start()

class GLWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        self.parent = parent
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

    def initializeGL(self):
        # GL.glEnable(GL.GL_ALPHA_TEST)    
        # GL.glEnable(GL.GL_DEPTH_TEST)  
        # GL.glEnable(GL.GL_COLOR_MATERIAL)
        # GL.glEnable(GL.GL_LIGHTING)       
        # GL.glEnable(GL.GL_LIGHT0)      
        # GL.glEnable(GL.GL_BLEND)      
        # GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        self.qglClearColor(QtGui.QColor(0, 0, 255, 0))
        GL.glClearColor(0, 0, 255, 0)

    def resizeGL(self, w, h):
        GL.glViewport(0, 0, w, h)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        x = float(w) / h
        GL.glFrustum(-x, x, -1.0, 1.0, 1.0, 10.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)   
        GL.glPushMatrix()
        GL.glBegin(GL.GL_TRIANGLES)
        GL.glColor3f(1.0, 0.0, 0.0, 0)
        GL.glVertex3f(-1.0, 1.0, -3.0, 0)
        GL.glColor3f(0.0, 1.0, 0.0, 0)
        GL.glVertex3f(1.0, 1.0, -3.0, 0)
        GL.glColor3f(0.0, 0.0, 1.0, 0)
        GL.glVertex3f(0.0, -1.0, -3.0, 0)
        GL.glEnd()
        GL.glPopMatrix()
        GL.glFlush()

        W = H = 400
        data = [r.randint(0, 255) for _ in range (0, H*W*3)]
        GL.glDrawPixels(W, H, GL.GL_RGB, GL.GL_UNSIGNED_BYTE, (GL.GLubyte * len(data))(*data))


class MainWindow(QMainWindow):

    def __init__(self, screen_size):
        QMainWindow.__init__(self)

        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
            | QtCore.Qt.WindowTransparentForInput
        )
        self.size = size  + QtCore.QSize(220, 102)
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                self.size,
                QtWidgets.qApp.desktop().availableGeometry()
        ))
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.updater = True
        def update_widget():
            while self.updater:
               time.sleep(.2)
               self.update()
        self.update_thread = threading.Thread(target=update_widget)
        self.update_thread.start()
        #from Tools.audio_noise import audio_noise_thread_executor
        #self.audio_noise_thread = audio_noise_thread_executor()

    def _close_event_method(self):
        QtWidgets.qApp.quit()
        self.app.quit()
        self.updater = False
        self.audio_noise_thread.data['do'] = False
        stop_hotkeys_listener()

    def paintEvent(self, event):
        width, height = r.randint(120, 170), r.randint(20, 30)
        qp = QtGui.QPainter(self) 
        for i in range(int(self.size.width() / width)):
            for j in range(int(self.size.height() / height) + 1):
                #qp.setBrush()    
                #if r.randint(1, 1) == 1:
                qp.fillRect( QtCore.QRect(i*width, j*height, width, height),
                     QtGui.QBrush(QtGui.QColor(r.randint(0, 255),r.randint(0, 255),r.randint(0, 255), 40)))
                #else:
                #    qp.drawEllipse(i*width, j*height, width, height)


    def gen_image_object(self):
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    print('Available: %d x %d' % (rect.width(), rect.height()))
    mywindow = MainWindow(size)
    mywindow.app = app
    mywindow.show()


    bind_hotkey_function("Ctrl+M", mywindow._close_event_method)

    sys.exit(app.exec())
