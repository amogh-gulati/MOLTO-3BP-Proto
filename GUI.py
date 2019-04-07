from __future__ import unicode_literals
import sys
import os
import random
import numpy as np
from matplotlib.backends import qt_compat
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if use_pyside:
    from PySide import QtGui, QtCore
else:
    from PyQt4 import QtGui, QtCore

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self):
        """t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t, s)"""
        x = []
        for i in range(100):
            x.append(i)
        y = []
        for i in x:
            y.append(i**2)
        self.axes.plot(x,y)


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.cla()
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        #window setup
        self.setGeometry(50,50,700,500)
        self.setWindowTitle("MOLTO-3BP")
        #status bar
        self.statusBar()
        #main menu
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        saveAction = QtGui.QAction("&save",self)
        fileMenu.addAction(saveAction)
        self.main_widget = QtGui.QWidget(self)
        l = QtGui.QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=5, height=10, dpi=100)
        sc.resize(sc.sizeHint())
        #dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(sc)
        #l.addWidget(dc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)
        self.home()
    def home(self):
        self.label1 = QtGui.QLabel("var1",self)
        self.label1.move(550,50)
        self.textVar1 = QtGui.QLineEdit(self)
        self.textVar1.move(550,100)
        self.label1 = QtGui.QLabel("var2",self)
        self.label1.move(550,150)
        self.textVar2 = QtGui.QLineEdit(self)
        self.textVar2.move(550,200)
        self.label1 = QtGui.QLabel("var3",self)
        self.label1.move(550,250)
        self.textVar1 = QtGui.QLineEdit(self)
        self.textVar1.move(550,300)
        self.label1 = QtGui.QLabel("var4",self)
        self.label1.move(550,350)
        self.textVar2 = QtGui.QLineEdit(self)
        self.textVar2.move(550,400)
        self.EnterBtn = QtGui.QPushButton('Enter', self)
        self.EnterBtn.move(550,450)
        self.show()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__=='__main__':
    run()
