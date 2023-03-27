"""
PyQt4 widgets
    - basic building blocks of an application. 
    - in PyQt4 there are various widgets:
        - buttons
        - check boxes
        - sliders, or list boxes. 
"""
import sys

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except ModuleNotFoundError:
    try:
        from PyQt5.QtGui import *
        from PyQt5.QtCore import *
        from PyQt5.QtWidgets import *
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Cannot import neither PyQt4 nor PyQt5. Go HOME!")

class Tutorial5(QMainWindow):
    def __init__(self):
        super(Tutorial5, self).__init__()
        self.initUI()

    def initUI(self):
        """"""
        """
        TODO 1: Checkbox
        """
        # TODO 1.1.1. a) - Create 'There is pie here!' checkbox
        cb = QCheckBox('There is pie here!', self)

        # TODO 1.1.1. b) - Move box to x = 20, y = 20
        cb.move(20, 20)
        cb.resize(150, 20)

        # TODO 1.1.2. Check the box
        # the window title is set, so the checkbox MUST be checked.
        # by default, the window title is not set and the checkbox is unchecked.
        cb.toggle()

        # TODO 1.1.3. Toggle the title -
        # connect the user defined changeTitle() method to the stateChanged signal.
        cb.stateChanged.connect(self.changeTitle)

        ######################################## TODO 1.1.: END TODO 1.1. ########################################

        '''
        LESSON 2: Toggle Button
            - QPushButton in a special mode
            - has two states: pressed and not pressed. 
            We toggle between these two states by clicking on it.
        '''

        # the initial colour is black.
        self.col = QColor(0, 0, 0)

        # TODO 2.1.1. a) Create a QPushButton 'Red Pie'
        redb = QPushButton('Red Pie', self)

        # TODO 2.1.1. b) Make it checkable by calling the setCheckable() method.
        redb.setCheckable(True)

        # TODO 2.1.1. c) Move to x = 20, y = 70
        redb.move(20, 70)

        # connect a clicked signal to our user defined method.
        # and use the clicked signal that operates with a Boolean value.
        # TODO 2.1.2.
        redb.clicked[bool].connect(self.setColor)

        # TODO 2.1.3 - Create 'Green Pie' QPushButton + set checkable + move to x = 20, y = 130
        greenb = QPushButton('Green Pie', self)
        greenb.setCheckable(True)
        greenb.move(20, 130)

        # TODO 2.1.4 - Connect button to boolean handler (setColor)
        greenb.clicked[bool].connect(self.setColor)

        # TODO 2.1.5 - Create 'Blue Pie' QPushButton + set checkable + move to x = 20, y = 180
        blueb = QPushButton('Blue Pie', self)
        blueb.setCheckable(True)
        blueb.move(20, 180)

        # TODO 2.1.6 - Connect button to boolean handler (setColor)
        blueb.clicked[bool].connect(self.setColor)

        # TODO 2.1.7. = Create a rectangle at x = 150, y = 70, with w = 130, h = 140
        self.square = QFrame(self)
        self.square.setGeometry(150, 70, 130, 140)
        # Uncomment this
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())

        ######################################## TODO 2.1.: END TODO 2.1. ########################################
        '''
        TODO 3.1.: QLineEdit
        '''
        # TODO 3.1.1. Create label and move to x = 25, y = 230
        self.lbl = QLabel(self)
        self.lbl.move(25, 230)

        # TODO 3.1.2. Create qline edit and move to x = 20, y = 250
        qle = QLineEdit(self)
        qle.move(20, 250)

        # TODO 3.1.3. If the text in the line edit widget changes, we call the onChanged() method.
        qle.textChanged[str].connect(self.onChanged)

        ######################################## TODO 3.1.: END TODO 3.1. ########################################

        '''
        TODO 4.1.: QComboBox
            - widget that allows a user to choose from a list of options.
        '''
        self.lbl = QLabel("Py@Codette", self)
        self.lbl.move(25, 330)

        # TODO 4.1.1. Create a QComboBox widget
        combo = QComboBox(self)

        # TODO 4.1.2. Add Py@Codette, IoT4Girls, JS4HS, Celebration Day, Codette Stories to the Combo
        combo.addItem("Py@Codette")
        combo.addItem("IoT4Girls")
        combo.addItem("JS4HS")
        combo.addItem("Celebration Day")
        combo.addItem("Codette Stories")

        # Uncomment this
        combo.move(20, 300)

        # TODO 4.1.3. Upon an item selection, we call the onActivated() method.
        combo.activated[str].connect(self.onChanged)

        ######################################### TODO 4.1.: END TODO 4.1. ########################################

        self.setGeometry(500, 300, 300, 370)
        self.setWindowTitle('Py@Codette Tutorial #5')
        self.show()

    '''
    TODO 1.2.
    '''
    def changeTitle(self, state):
        '''
        The state of the widget is given to the changeTitle() method in the state variable. 
        If the widget is checked, we set a title of the window. 
        Otherwise, we set an empty string to the titlebar. 
        '''
        if state == Qt.Checked:
            self.setWindowTitle('Py@Codette Tutorial #5')
        else:
            self.setWindowTitle('')

    ######################################### TODO 1.2.: END TODO 1.2. ########################################

    '''
    TODO 2.2.
    '''
    def setColor(self, pressed):
        # TODO 2.2.1. Use  sender() to get the button which was toggled.
        source = self.sender()

        # TODO 2.2.2. Check the value of pressed. If True => val = 255, else val = 0
        if pressed:
            val = 255
        else:
            val = 0

        # TODO 2.2.3. In case it is a x button, we update the x part of the colour accordingly.
        if source.text() == "Red Pie":
            self.col.setRed(val)
        elif source.text() == "Green Pie":
            self.col.setGreen(val)
        elif source.text() == "Blue Pie":
            self.col.setBlue(val)

        # TODO 2.2.4. Use style sheets to change the background colour.
        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())

    ######################################### TODO 2.2.: END TODO 2.2. ########################################

    '''
    TODO 3. 2. & 4. 2.
    '''
    def onChanged(self, text):
        '''
        Set the typed text to the label widget.
        Call the adjustSize() method to adjust the size of the label to the length of the text.
        '''
        # TODO
        self.lbl.setText(text)
        self.lbl.adjustSize()

    ######################################### TODO 3.2. & 4.2.: END TODO 3.2. & 4.2. ########################################


def main():
    app = QApplication(sys.argv)
    ex = Tutorial5()
    app.exec_()


if __name__ == '__main__':
    main()
