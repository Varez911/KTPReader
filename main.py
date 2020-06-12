# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import math
import pandas as pd
from tkinter import filedialog
import tkinter as tk
import cv2 as cv
import numpy as np
import pytesseract
from PIL import Image
from PyQt5.QtGui import QPixmap, QImage
from matplotlib import pyplot as plot
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imageOut = QtWidgets.QLabel(self.centralwidget)
        self.imageOut.setGeometry(QtCore.QRect(60, 10, 451, 251))
        self.imageOut.setFrameShape(QtWidgets.QFrame.Box)
        self.imageOut.setText("")
        self.imageOut.setObjectName("imageOut")
        self.textOut = QtWidgets.QLineEdit(self.centralwidget)
        self.textOut.setGeometry(QtCore.QRect(520, 10, 231, 251))
        self.textOut.setText("")
        self.textOut.setObjectName("textOut")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(60, 280, 101, 51))
        self.openButton.setObjectName("openButton")
        self.binerSlider = QtWidgets.QSlider(self.centralwidget)
        self.binerSlider.setGeometry(QtCore.QRect(60, 460, 451, 22))
        self.binerSlider.setMaximum(255)
        self.binerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.binerSlider.setObjectName("binerSlider")
        self.readButton = QtWidgets.QPushButton(self.centralwidget)
        self.readButton.setGeometry(QtCore.QRect(410, 280, 101, 51))
        self.readButton.setObjectName("readButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.kontrastSlider = QtWidgets.QSlider(self.centralwidget)
        self.kontrastSlider.setGeometry(QtCore.QRect(60, 390, 451, 22))
        self.kontrastSlider.setMaximum(4000)
        self.kontrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.kontrastSlider.setObjectName("kontrastSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 390, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 460, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 430, 90, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 360, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.imageOut.setScaledContents(True)
        self.clickButton()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openButton.setText(_translate("MainWindow", "Open Image"))
        self.readButton.setText(_translate("MainWindow", "Read Image"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Threshold Biner"))
        self.label_4.setText(_translate("MainWindow", "Kontrast Dahulu"))

    def clickButton(self):
        self.openButton.clicked.connect(self.openImage)
        self.binerSlider.valueChanged.connect(self.binerImage)
        self.kontrastSlider.valueChanged.connect(self.kontrastImage)
        self.readButton.clicked.connect(self.readImage)

    def readImage(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
        TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'

        img = Image.open("temp.png")
        text = pytesseract.image_to_string(img)
        print('=======================================================')
        print(text)
        print('=======================================================')
        self.textOut.setText(text)
        # plot.imshow(self.image, cmap='gray', interpolation='bicubic')
        # plot.show()

    def kontrastImage(self):
        contrast = self.kontrastSlider.value() / 1000
        self.label.setText(str(contrast))
        h, w = self.image2.shape[:2]
        biner_ZeroTwo = np.zeros((h, w), np.uint8)
        for i in range(h):
            for j in range(w):
                a = self.image2.item(i,j)
                b = math.ceil(a * contrast)
                if b > 255:
                    b = 255
                elif b < 0:
                    b = 0
                else:
                    b = b
                biner_ZeroTwo.itemset((i,j), b)
        self.image = biner_ZeroTwo
        self.image3 = biner_ZeroTwo
        print('=====Kontrast=====')
        print(self.image[260:265, 350:355])
        self.display(1)

    def binerImage(self):
        tresshold = self.binerSlider.value()
        self.label_2.setText(str(tresshold))
        h, w = self.image2.shape[:2]
        biner_Zero = np.zeros((h, w), np.uint8)
        for i in range(h):
            for j in range(w):
                a = self.image3.item(i, j)
                if a < tresshold:
                    a = 0
                else:
                    a = 255
                biner_Zero.itemset((i,j), a)
        self.image = biner_Zero
        print('=====Biner=====')
        print(self.image[260:265, 350:355])
        self.display(1)

    def openImage(self):
        self.image = cv.imread(self.openWWindow())
        print('=====Awal=====')
        print(self.image[260:265, 350:355, 2])
        print(self.image[260:265, 350:355, 1])
        print(self.image[260:265, 350:355, 0])
        self.grayImage()

    def grayImage(self):
        h, w = self.image.shape[:2]
        gray = np.zeros((h, w), np.uint8)
        for i in range(h):
            for j in range(w):
                gray[i, j] = np.clip(0.333 * self.image[i, j, 0] + 0.333 * self.image[i, j, 1] + 0.333 * self.image[i, j, 2], 0, 255)
        self.image = gray
        self.image2 = self.image
        print('=====Grayscale=====')
        print(self.image[260:265, 350:355])
        self.display(1)

    def openWWindow(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

    def display(self, windows):
        qformat = QImage.Format_Indexed8
        if len(self.image.shape) == 3:
            if (self.image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888  # Format_Grayscale8
            else:
                qformat = QImage.Format_RGB888  # Format_Grayscale16
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
        img2 = QImage()
        img = img.rgbSwapped()
        if windows == 1:
            self.imageOut.setPixmap(QPixmap.fromImage(img))
            cv.imwrite('temp.png',self.image)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
