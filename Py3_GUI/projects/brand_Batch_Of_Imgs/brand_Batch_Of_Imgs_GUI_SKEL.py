#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from brand_Batch_Of_Imgs import *

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except ModuleNotFoundError:
    try:
        from PyQt5.QtWidgets import *
        from PyQt5.QtGui import *
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Cannot import neither PyQt4 nor PyQt5. Go HOME!")

# x coord and increments
X0 = 20; X1 = 170; INC_X_LABEL = 5; X_BOX_INC = 120;
# Widths
W0 = 130; W1 = 140; W2 = 480
# Height (universal)
H0 = 30
# y coord and increments for it
Y_MAIN = 20; Y_INC_0 = 10; Y_INC_1 = 20; Y_INC_2 = 50

class BranderGUI(QMainWindow):
    def __init__(self, parent=None):
        # TODO 13.
        super(BranderGUI, self).__init__(parent)
        # call init_local_vars
        self. init_local_vars()
        # Y_MAIN will change and it is a local variable so...
        global Y_MAIN

        # Instantiate background object
        self.brander = Brander()

        ''' TODO 13.1. a) Add label 'Consider extensions' 
                         at (X0 + INC_X_LABEL, Y_MAIN), with size (W1, H0)'''
        lbl1 = self.add_label_to_main_window('Consider extensions', X0 + INC_X_LABEL, Y_MAIN, W1, H0)
        ''' TODO 13.1. b) Check boxes group with the possible extensions
                         at pos (X1, Y_INC_0) with increments of (X_BOX_INC, Y_INC_1)'''
        self.extBoxesGroup = None

        Y_MAIN += Y_INC_2

        ''' TODO 13.2. a) srcBtn - "Source Directory" of the images to brand
                         connect to on_srcBtn_clicked and add at position (X0, Y_MAIN)
                         with size (W0, H0)'''
        self.srcBtn = None
        ''' TODO 13.2. b) leSrc - QLineEdit - write the path to source directory
                          add at position (X1, Y_MAIN) with size (W2, H0)'''
        self.leSrc = None
        Y_MAIN += Y_INC_2

        ''' TODO 13.3. a) logoBtn - "Logo Path", connected to on_logoBtn_clicked
                          add at position (X0, Y_MAIN) with size (W0, H0)'''
        self.logoBtn = None
        ''' TODO 13.3. b) leLogo - path to the logo (text)
                           add at position (X1, Y_MAIN) with size (W2, H0)'''
        self.leLogo = None

        Y_MAIN += Y_INC_2

        ''' TODO 13.4. a) lblLogo - "Scale Logo", 
                          at position (X0 + INC_X_LABEL, Y_MAIN) with size (W1, H0)'''
        lblLogo =  None
        ''' TODO 13.4.b) logoScaleGroup - which "scales" are accepted?
                         text from accepted_logo_scales list, connected to on_logoScaleBox_toggled
                         add at position (X1, Y_MAIN), with increment X_BOX_INC
                         and with each item size (W0, H0)'''
        self.logoScaleGroup = None

        Y_MAIN += Y_INC_0 + Y_INC_1

        ''' TODO 13.5. a) lblLogoPos - 'Logo Position', 
                          add at (X0 + INC_X_LABEL, Y_MAIN) with size (W1, H0)
        '''
        lblLogoPos = None
        ''' TODO 13.5. b) logoPosGroup - where to place the logo?
                          text from accepted_logo_pos list, connected to on_logoPosBox_toggled
                          add at position (X1, Y_MAIN), with increment X_BOX_INC
                          and with each item size (W0, H0)'''
        self.logoPosGroup = None

        Y_MAIN += Y_INC_2

        self.lblLogoX = self.add_label_to_main_window('Set logo x coord',
                                                      X0, Y_MAIN, W0, H0)
        self.leLogoX = self.add_line_edit_to_main_window(X1, Y_MAIN, W0, H0)

        self.lblLogoY = self.add_label_to_main_window('Set logo y coord',
                                                      X1 + W0 + 16*INC_X_LABEL,
                                                      Y_MAIN, W0, H0)
        self.leLogoY = self.add_line_edit_to_main_window(X1 + 2*W0 + 18*INC_X_LABEL,
                                                         Y_MAIN, W0, H0)

        Y_MAIN += Y_INC_2
        ''' TODO 13.6. a) destBtn - "Dest Directory" of the images to brand
                          connected to on_destBtn_clicked
                          add at position (X0, Y_MAIN) with size (W0, H0)'''
        self.destBtn = None

        ''' TODO 13.6. b) leDest - QLineEdit - write the path to destination directory
            add at position (X1, Y_MAIN) with size (W2, H0)'''
        self.leDest = None

        Y_MAIN += Y_INC_2
        ''' TODO 13.7. destBtn - "Dest Directory" of the images to brand
            connected to on_destBtn_clicked
            add at position (X0, Y_MAIN) with size (W0, H0)'''
        self.brandBtn = None

        # initialize statusBar()
        self.statusBar()

        self.setWindowTitle('Pie Brander')
        self.setGeometry(500, 100, 670, 430)

    def init_local_vars(self):
        # give this path to the backend
        self.srcDirPath = ''

        # extensions of images to be considered in the source directory
        self.accepted_ext = \
            [".jpg", ".jpeg", ".png", ".bmp", ".ppm", ".pgm", ".pbm", ".pnm"]
        # accepted "scales": smaller (/2), same, bigger (*2)
        self.accepted_logo_scales = ['smaller', 'same', 'bigger']
        # accepted postitions for the logo
        self.accepted_logo_pos = ["UP LEFT", "UP RIGHT", "DOWN LEFT", "DOWN RIGHT"]

    # TODO 1.
    def add_label_to_main_window(self, text, x, y, w, h):
        # TODO 1.1. Create QLabel with text and self as parent
        lbl = None
        # TODO 1.2. Move label to (x, y)

        # TODO 1.3. Resize label to (w, h)

        return lbl

    # TODO 2.
    def add_ext_boxes_to_main_window(self, x0, y0, x_inc, y_inc):
        # TODO 2.1. Create QButtonGroup with self as parent
        extBoxesGroup = None
        x = x0; y = y0;
        # nothing TODO 2.2.
        for ext in self.accepted_ext:
            # TODO 2.2.1. Create QCheckBox with ext as text ans self as parent
            elem = None
            # TODO 2.2.2. Set not checked

            # TODO 2.2.3. Move check box to (x, y)

            # TODO 2.2.4. Add button to extBoxesGroup

            # increase x (the horizontal coord)
            x += x_inc

            # at each four check-boxes added on a row
            if ((x - x0) / x_inc) % 4 == 0:
                # start a new row
                x = x0
                y += y_inc

        # TODO 2.3. Connect the buttonClicked signal of the boxes group to button_clicked

        # TODO 2.4. Set not exclusive choice

        return extBoxesGroup

    # TODO 3.
    def add_button_to_main_window(self, text, func, x, y, w, h):
        # TODO 3.1. Create QPushButton with text, having as parent this MainWindow
        btn = None
        # TODO 3.2. Move the button to (x,y)

        # TODO 3.3. Resize button to (w, h)

        # TODO 3.4. Connect the clicked signal to func

        return btn

    # TODO 4.
    def add_line_edit_to_main_window(self, x, y, w, h):
        # TODO 4.1. Create QLineEdit having this class as parent
        le = None
        # TODO 4.2. Move the line edit to (x, y)

        # TODO 4.3. Resize to (w, h)

        return le

    # TODO 5.
    def add_radio_boxes_to_main_window(self, txt_list, func, x0, y0, x_inc, w, h):
        # TODO 5.1. Create QButtonGroup with self as parent
        rbGroup = None
        x = x0; y = y0;
        for ext in txt_list:
            # TODO 5.2. Create QRadioButton with test ext and self as parent

            # TODO 5.3. Move elem to (x, y)

            # TODO 5.4. Resize elem to (w, h)

            # go to next position
            x += x_inc
            # TODO 5.5. Add elem as button to the group

        # TODO 5.6. Connect the buttonClicked signal of the group to func

        # TODO 5.7. Only one box can be checked at a time

        return rbGroup

    # TODO 6
    def on_srcBtn_clicked(self):
        # TODO 6.1. "Select Source Dirctory" - Get source directory using QFileDialog
        srcDirPath = None
        # nothing TODO 6.2. If there is a path selected
        if srcDirPath != '':
            # TODO 6.2.1. Set srcDirPath in brander

            # TODO 6.2.2. Set srcDirPath as text for leSrc
            pass

    # TODO 7
    def on_logoBtn_clicked(self):
        # TODO 7.1. Open file name in QFileDialog with title "Select Logo File Path"
        logoPath = None
        # nothing TODO 7.2.
        if str(logoPath) != '':
            # TODO 7.2.1. Set logo path in brander

            # TODO 7.2.2. Set logo path as text in leLogo
            pass

    # TODO 8
    def on_destBtn_clicked(self):
        # TODO 8.1. "Select Dest Directory" - get existing directory using QFileDialog
        destDirPath = None
        # nothing TODO 8.2.
        if destDirPath != '':
            # TODO 8.2.1. Set destDirPath

            # TODO 8.2.2. Set dest dir path as text in leDest
            pass

    # nothing TODO 9.
    def on_brandBtn_clicked(self):
        # Check if everything is ok and you can start branding
        if self.brander.canBrand():
            if self.leLogoX.text() != '':
                self.brander.x = int(self.leLogoX.text())

            if self.leLogoY.text() != '':
                self.brander.y = int(self.leLogoY.text())

            self.brander.brandAndSave()
        else:
            self.statusBar().showMessage("Error: not all the fields have values.")

    # TODO 10.
    @pyqtSlot(QAbstractButton)
    def button_clicked(self, b):
        # TODO 10.1. if the text in b is not in the extensions list and b is checked
        ext = str(b.text()).lower()
        if True:
            # TODO 10.1.1. => append it to extensions
            pass
        # nothing TODO 10.2. else
        else:
            # TODO 10.2.1 => remove it from extensions (the box was unchecked)
            pass

    # TODO 11.
    @pyqtSlot(QAbstractButton)
    def on_logoScaleBox_toggled(self, b):
        # TODO 11.1. if box b is checked
        if True:
            # TODO 11.2. => set scaleLogo to the text in b
            pass

    # TODO 12.
    @pyqtSlot(QAbstractButton)
    def on_logoPosBox_toggled(self, b):
        # TODO 12.1. if box b is checked
        if True:
            # TODO 12.1.1. => set posLogo to the text in b
            pass

def main():
    # create a QApplication object
    app = QApplication(sys.argv)
    # create the main window
    ex = BranderGUI()
    # show it
    ex.show()
    # then exec the app or else nothing will happen :)
    app.exec_()

if __name__ == '__main__':
    main()