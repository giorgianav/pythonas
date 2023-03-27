#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except ModuleNotFoundError:
    try:
        from PyQt5.QtWidgets import *
        from PyQt5.QtGui import *
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Cannot import neither PyQt4 nor PyQt5. Go HOME!")

class Tutorial1(QMainWindow):
    """
    Tutorial1 has as parent the QWidget class from the QtGui module.
    """
    def __init__(self):
        '''
        __init__ is a constructor, used to create an instance of this class.
        '''
        # inheritance => 2 constructors:
        # super() returns the parent of the object Tutorial1.
        # and we call its constructor using __init__().
        super(Tutorial1, self).__init__()
        self.initUI()

    def initUI(self):
        ''''''
        '''
        TODO 1: Tooltips. 
        '''
        # TODO 1.1. Set 10px Courier Font for our nex tooltips
        QToolTip.setFont(QFont('Courier', 10))

        # TODO 1.2. Set tooltip for the main window (self)
        self.setToolTip('This is a <b>QWidget</b>. \
                        It doesn\'t do much but hosting the useful stuff.')

        # TODO 1.3. Create QPushButton
        btn = QPushButton('PieButton', self)

        # TODO 1.4. Set tooltip for btn. Use rich text format (the <b></b>).
        btn.setToolTip('This is a <b>QPushButton</b> widget. Press for pie :)')

        # TODO 1.5. Resize btn to the recommended size for the tooltip.
        btn.resize(btn.sizeHint())

        # TODO 1.6. Move btn to x = 10, y = 10
        btn.move(10, 10)

        ######################## TODO 1: End of TODO 1 ########################

        '''
        TODO 2: Quit Buttons
        '''
        # TODO 2.1. Create a push button with label 'PieQuit'
        qbtn = QPushButton('PieQuit', self)

        # TODO 2.2. Connect the clicked signal of qbtn to the quit() method.
        qbtn.clicked.connect(self.close)

        # TODO 2.3. Set tooltip for qbtn
        qbtn.setToolTip('Press to quit pie :(')

        # TODO 2.4. Resize qbtn to sizeHint()
        qbtn.resize(qbtn.sizeHint())

        # TODO 2.5. Move qbtn to x = 170, y = 10
        qbtn.move(170, 10)

        ######################## TODO 2: End of TODO 2 ########################

        # The main window starts at position (500, 300) with size 270 x 100.
        self.setGeometry(500, 300, 270, 100)

        # TODO 4.1. Uncomment.
        self.center()

        self.setWindowTitle('Py@Codette Tutorial #1')
        # don't forget to 'show' all the stuff.
        self.show()

    '''
    TODO 3: Message Box
    - display this for the user to confirm exit on X-press.
    '''
    def closeEvent(self, event):
        # TODO 3.1. Ask question in message box. Set options Yes / No. No = default.
        reply = QMessageBox.question(self, 'Pie Quit :(',
                                           "Are you sure to quit pie? :((",
                                           QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.No)

        # TODO 3.2. If the value of the reply is YES
        if reply == QMessageBox.Yes:
            # TODO 3.2.1. Accept event
            event.accept()
        else:
            # TODO 3.2.2. Otherwise ignore the close event.
            event.ignore()

        ######################## TODO 3: End of TODO 3 ########################

    '''
        TODO 4: Center window on screen.
    '''
    def center(self):
        # TODO 4.2. Get a rectangle specifying the geometry of the main window
        qr = self.frameGeometry()

        # TODO 4.3. Use QDesktopWidget to find out some info about the available
        # geometry (aka the center)
        cp = QDesktopWidget().availableGeometry().center()

        # TODO 4.4. Move to center
        qr.moveCenter(cp)

        #  TODO 4.5. Move top left of the application window (self) to the top left of qr
        self.move(qr.topLeft())

        ######################## TODO 4: End of TODO 4 ########################

def main():
    # create a QApplication object
    app = QApplication(sys.argv)
    # create main window
    ex = Tutorial1()
    # enter the mainloop of the app, where event handling starts.
    app.exec_()

if __name__ == '__main__':
    main()
