import pyqrcode
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5 import QtCore,QtWidgets

# Author : Suleiman AlOthman
# Date : 2018/8/9
# Twitter : https://www.twitter.com/SuleAlOthman
# Website : www.sliemerez.net - www.suleiman.me
# Qr Reader and Generator with GUI - simple example


class qrForm(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QrGenerator")

		self.setMinimumSize(QtCore.QSize(600,800))
		self.setMaximumSize(QtCore.QSize(1500,900))
		self.resize(600,800)

		self.centralwidget = QWidget(self)
		
		self.horizontalLayout = QHBoxLayout(self.centralwidget)

		self.verticalLayout = QVBoxLayout()

		self.qrTextEdit = QLineEdit(self.centralwidget)
		self.verticalLayout.addWidget(self.qrTextEdit)

		self.genQrButton = QPushButton(self.centralwidget)
		self.genQrButton.setText("Generate QRCode")
		self.verticalLayout.addWidget(self.genQrButton)

		self.decodeQrButton = QPushButton(self.centralwidget)
		self.decodeQrButton.setText("Read QRCode")
		self.verticalLayout.addWidget(self.decodeQrButton)

		self.decodeText = QLabel(self.centralwidget)
		self.decodeText.setText("..")
		self.decodeText.setAlignment(QtCore.Qt.AlignCenter)
		self.verticalLayout.addWidget(self.decodeText)

		self.qrCodeImage = QLabel(self.centralwidget)

		self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		self.sizePolicy.setHorizontalStretch(1)
		self.sizePolicy.setVerticalStretch(1)
		self.sizePolicy.setHeightForWidth(self.qrCodeImage.sizePolicy().hasHeightForWidth())

		self.qrCodeImage.setSizePolicy(self.sizePolicy)
		self.qrCodeImage.setText("")
		self.qrCodeImage.setAlignment(QtCore.Qt.AlignCenter)

		self.verticalLayout.addWidget(self.qrCodeImage)
		self.horizontalLayout.addLayout(self.verticalLayout)

		self.setCentralWidget(self.centralwidget)

		self.genQrButton.clicked.connect(self.genButton)
		self.decodeQrButton.clicked.connect(self.decQrButton)

	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"Open QRCode Image", "","Images (*.png);;All Files (*)", options=options)
		if fileName:
			return fileName
		else:
			return None


	def genButton(self):
		if(len(self.qrTextEdit.text()) < 1):
			return
		rQR = self.generateQR(self.qrTextEdit.text())
		self.qrCodeImage.setPixmap(QPixmap("test.png").scaled(429,429))

	def decQrButton(self):
		fName = self.openFileNameDialog()
		if (fName == None):
			return
		qr = decode(Image.open(fName), symbols=[ZBarSymbol.QRCODE])
		extractString = str(qr[0].data)
		self.decodeText.setText(extractString[2:-1])

	def generateQR(self,str):
		q = pyqrcode.create(str)
		q.png("test.png",scale=13)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pForm = qrForm()
    pForm.show()
    sys.exit(app.exec_())


