# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowBase.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowBase(object):
	def setupUi(self, MainWindowBase):
		MainWindowBase.setObjectName("MainWindowBase")
		MainWindowBase.resize(846, 569)
		self.centralwidget = QtWidgets.QWidget(MainWindowBase)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		self.tabWidget.setObjectName("tabWidget")
		self.imageTab = QtWidgets.QWidget()
		self.imageTab.setAccessibleName("")
		self.imageTab.setObjectName("imageTab")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.imageTab)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.blockEditorBox = QtWidgets.QGroupBox(self.imageTab)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(1)
		sizePolicy.setHeightForWidth(self.blockEditorBox.sizePolicy().hasHeightForWidth())
		self.blockEditorBox.setSizePolicy(sizePolicy)
		self.blockEditorBox.setObjectName("blockEditorBox")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.blockEditorBox)
		self.verticalLayout.setObjectName("verticalLayout")
		self.blocklyWebView = QtWebKitWidgets.QWebView(self.blockEditorBox)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(1)
		sizePolicy.setHeightForWidth(self.blocklyWebView.sizePolicy().hasHeightForWidth())
		self.blocklyWebView.setSizePolicy(sizePolicy)
		self.blocklyWebView.setUrl(QtCore.QUrl("about:blank"))
		self.blocklyWebView.setObjectName("blocklyWebView")
		self.verticalLayout.addWidget(self.blocklyWebView)
		self.generateBlockXMLButton = QtWidgets.QPushButton(self.blockEditorBox)
		self.generateBlockXMLButton.setObjectName("generateBlockXMLButton")
		self.verticalLayout.addWidget(self.generateBlockXMLButton)
		self.horizontalLayout.addWidget(self.blockEditorBox)
		self.graphicsBox = QtWidgets.QGroupBox(self.imageTab)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(1)
		sizePolicy.setHeightForWidth(self.graphicsBox.sizePolicy().hasHeightForWidth())
		self.graphicsBox.setSizePolicy(sizePolicy)
		self.graphicsBox.setObjectName("graphicsBox")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.graphicsBox)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.inputGraphicsView = QtWidgets.QGraphicsView(self.graphicsBox)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(1)
		sizePolicy.setHeightForWidth(self.inputGraphicsView.sizePolicy().hasHeightForWidth())
		self.inputGraphicsView.setSizePolicy(sizePolicy)
		self.inputGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.inputGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.inputGraphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
		self.inputGraphicsView.setObjectName("inputGraphicsView")
		self.verticalLayout_2.addWidget(self.inputGraphicsView)
		self.outputGraphicsView = QtWidgets.QGraphicsView(self.graphicsBox)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(1)
		sizePolicy.setHeightForWidth(self.outputGraphicsView.sizePolicy().hasHeightForWidth())
		self.outputGraphicsView.setSizePolicy(sizePolicy)
		self.outputGraphicsView.setObjectName("outputGraphicsView")
		self.verticalLayout_2.addWidget(self.outputGraphicsView)
		self.horizontalLayout.addWidget(self.graphicsBox)
		self.tabWidget.addTab(self.imageTab, "")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.tabWidget.addTab(self.tab_2, "")
		self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
		MainWindowBase.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindowBase)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 21))
		self.menubar.setObjectName("menubar")
		self.menuFiles = QtWidgets.QMenu(self.menubar)
		self.menuFiles.setObjectName("menuFiles")
		MainWindowBase.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindowBase)
		self.statusbar.setObjectName("statusbar")
		MainWindowBase.setStatusBar(self.statusbar)
		self.actionOpenVideo = QtWidgets.QAction(MainWindowBase)
		self.actionOpenVideo.setObjectName("actionOpenVideo")
		self.actionOpenImage = QtWidgets.QAction(MainWindowBase)
		self.actionOpenImage.setObjectName("actionOpenImage")
		self.actionOpenBlockData = QtWidgets.QAction(MainWindowBase)
		self.actionOpenBlockData.setObjectName("actionOpenBlockData")
		self.actionSaveBlockData = QtWidgets.QAction(MainWindowBase)
		self.actionSaveBlockData.setObjectName("actionSaveBlockData")
		self.actionQuit = QtWidgets.QAction(MainWindowBase)
		self.actionQuit.setObjectName("actionQuit")
		self.menuFiles.addAction(self.actionOpenVideo)
		self.menuFiles.addAction(self.actionOpenImage)
		self.menuFiles.addSeparator()
		self.menuFiles.addAction(self.actionOpenBlockData)
		self.menuFiles.addAction(self.actionSaveBlockData)
		self.menuFiles.addSeparator()
		self.menuFiles.addAction(self.actionQuit)
		self.menubar.addAction(self.menuFiles.menuAction())

		self.retranslateUi(MainWindowBase)
		self.tabWidget.setCurrentIndex(0)
		self.actionQuit.triggered.connect(MainWindowBase.close)
		QtCore.QMetaObject.connectSlotsByName(MainWindowBase)

	def retranslateUi(self, MainWindowBase):
		_translate = QtCore.QCoreApplication.translate
		MainWindowBase.setWindowTitle(_translate("MainWindowBase", "MainWindow"))
		self.blockEditorBox.setTitle(_translate("MainWindowBase", "Block Editor"))
		self.generateBlockXMLButton.setText(_translate("MainWindowBase", "Generate Block XML"))
		self.graphicsBox.setTitle(_translate("MainWindowBase", "Background"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageTab), _translate("MainWindowBase", "Image Processing"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindowBase", "Object Detection"))
		self.menuFiles.setTitle(_translate("MainWindowBase", "Files"))
		self.actionOpenVideo.setText(_translate("MainWindowBase", "Open Video"))
		self.actionOpenImage.setText(_translate("MainWindowBase", "Open Image"))
		self.actionOpenBlockData.setText(_translate("MainWindowBase", "Open Block Data"))
		self.actionSaveBlockData.setText(_translate("MainWindowBase", "Save Block Data"))
		self.actionQuit.setText(_translate("MainWindowBase", "Quit"))
		self.actionQuit.setShortcut(_translate("MainWindowBase", "Ctrl+Q"))

from PyQt5 import QtWebKitWidgets

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindowBase = QtWidgets.QMainWindow()
	ui = Ui_MainWindowBase()
	ui.setupUi(MainWindowBase)
	MainWindowBase.show()
	sys.exit(app.exec_())

