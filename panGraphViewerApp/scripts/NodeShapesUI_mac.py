# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NodeShapes_mac.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_nodeShapes(object):
    def setupUi(self, nodeShapes):
        nodeShapes.setObjectName("nodeShapes")
        nodeShapes.resize(380, 700)
        nodeShapes.setMinimumSize(QtCore.QSize(380, 700))
        nodeShapes.setMaximumSize(QtCore.QSize(380, 700))
        self.label = QtWidgets.QLabel(nodeShapes)
        self.label.setGeometry(QtCore.QRect(10, 10, 311, 25))
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(nodeShapes)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 361, 245))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(120, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 25))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 25))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(0, 25))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.visBB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.visBB.setMinimumSize(QtCore.QSize(0, 30))
        self.visBB.setObjectName("visBB")
        self.visBB.addItem("")
        self.visBB.addItem("")
        self.visBB.addItem("")
        self.visBB.addItem("")
        self.visBB.addItem("")
        self.visBB.addItem("")
        self.visBB.addItem("")
        self.visBB.addItem("")
        self.visBB.addItem("")
        self.visBB.addItem("")
        self.gridLayout.addWidget(self.visBB, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(0, 25))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.visSNP = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.visSNP.setMinimumSize(QtCore.QSize(0, 30))
        self.visSNP.setObjectName("visSNP")
        self.visSNP.addItem("")
        self.visSNP.addItem("")
        self.visSNP.addItem("")
        self.visSNP.addItem("")
        self.visSNP.addItem("")
        self.visSNP.addItem("")
        self.visSNP.addItem("")
        self.visSNP.addItem("")
        self.visSNP.addItem("")
        self.visSNP.addItem("")
        self.gridLayout.addWidget(self.visSNP, 1, 2, 1, 1)
        self.visDEL = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.visDEL.setMinimumSize(QtCore.QSize(0, 30))
        self.visDEL.setObjectName("visDEL")
        self.visDEL.addItem("")
        self.visDEL.addItem("")
        self.visDEL.addItem("")
        self.visDEL.addItem("")
        self.visDEL.addItem("")
        self.visDEL.addItem("")
        self.visDEL.addItem("")
        self.visDEL.addItem("")
        self.visDEL.addItem("")
        self.visDEL.addItem("")
        self.gridLayout.addWidget(self.visDEL, 2, 2, 1, 1)
        self.visINS = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.visINS.setMinimumSize(QtCore.QSize(0, 30))
        self.visINS.setObjectName("visINS")
        self.visINS.addItem("")
        self.visINS.addItem("")
        self.visINS.addItem("")
        self.visINS.addItem("")
        self.visINS.addItem("")
        self.visINS.addItem("")
        self.visINS.addItem("")
        self.visINS.addItem("")
        self.visINS.addItem("")
        self.visINS.addItem("")
        self.gridLayout.addWidget(self.visINS, 3, 2, 1, 1)
        self.visINV = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.visINV.setMinimumSize(QtCore.QSize(0, 30))
        self.visINV.setObjectName("visINV")
        self.visINV.addItem("")
        self.visINV.addItem("")
        self.visINV.addItem("")
        self.visINV.addItem("")
        self.visINV.addItem("")
        self.visINV.addItem("")
        self.visINV.addItem("")
        self.visINV.addItem("")
        self.visINV.addItem("")
        self.visINV.addItem("")
        self.gridLayout.addWidget(self.visINV, 4, 2, 1, 1)
        self.visDUP = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.visDUP.setMinimumSize(QtCore.QSize(0, 30))
        self.visDUP.setObjectName("visDUP")
        self.visDUP.addItem("")
        self.visDUP.addItem("")
        self.visDUP.addItem("")
        self.visDUP.addItem("")
        self.visDUP.addItem("")
        self.visDUP.addItem("")
        self.visDUP.addItem("")
        self.visDUP.addItem("")
        self.visDUP.addItem("")
        self.visDUP.addItem("")
        self.gridLayout.addWidget(self.visDUP, 5, 2, 1, 1)
        self.visTRANS = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.visTRANS.setMinimumSize(QtCore.QSize(0, 30))
        self.visTRANS.setObjectName("visTRANS")
        self.visTRANS.addItem("")
        self.visTRANS.addItem("")
        self.visTRANS.addItem("")
        self.visTRANS.addItem("")
        self.visTRANS.addItem("")
        self.visTRANS.addItem("")
        self.visTRANS.addItem("")
        self.visTRANS.addItem("")
        self.visTRANS.addItem("")
        self.visTRANS.addItem("")
        self.gridLayout.addWidget(self.visTRANS, 6, 2, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(nodeShapes)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 630, 361, 66))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.reset = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.reset.setMinimumSize(QtCore.QSize(0, 30))
        self.reset.setMaximumSize(QtCore.QSize(60, 16777215))
        self.reset.setObjectName("reset")
        self.gridLayout_2.addWidget(self.reset, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setMinimumSize(QtCore.QSize(0, 25))
        self.label_9.setMaximumSize(QtCore.QSize(215, 16777215))
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.change = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.change.setMinimumSize(QtCore.QSize(0, 30))
        self.change.setMaximumSize(QtCore.QSize(50, 16777215))
        self.change.setObjectName("change")
        self.gridLayout_2.addWidget(self.change, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(nodeShapes)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 361, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(nodeShapes)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 330, 361, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(nodeShapes)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 380, 361, 241))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_16.setMinimumSize(QtCore.QSize(0, 25))
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_14.setMinimumSize(QtCore.QSize(0, 25))
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_12.setMinimumSize(QtCore.QSize(120, 25))
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_17.setMinimumSize(QtCore.QSize(0, 25))
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 5, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setMinimumSize(QtCore.QSize(0, 25))
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_15.setMinimumSize(QtCore.QSize(0, 25))
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 3, 0, 1, 1)
        self.cyBB = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cyBB.setMinimumSize(QtCore.QSize(0, 30))
        self.cyBB.setObjectName("cyBB")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.cyBB.addItem("")
        self.gridLayout_3.addWidget(self.cyBB, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_18.setMinimumSize(QtCore.QSize(0, 25))
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 6, 0, 1, 1)
        self.cySNP = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cySNP.setMinimumSize(QtCore.QSize(0, 30))
        self.cySNP.setObjectName("cySNP")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.cySNP.addItem("")
        self.gridLayout_3.addWidget(self.cySNP, 1, 2, 1, 1)
        self.cyDEL = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cyDEL.setMinimumSize(QtCore.QSize(0, 30))
        self.cyDEL.setObjectName("cyDEL")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.cyDEL.addItem("")
        self.gridLayout_3.addWidget(self.cyDEL, 2, 2, 1, 1)
        self.cyINS = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cyINS.setMinimumSize(QtCore.QSize(0, 30))
        self.cyINS.setObjectName("cyINS")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.cyINS.addItem("")
        self.gridLayout_3.addWidget(self.cyINS, 3, 2, 1, 1)
        self.cyINV = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cyINV.setMinimumSize(QtCore.QSize(0, 30))
        self.cyINV.setObjectName("cyINV")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.cyINV.addItem("")
        self.gridLayout_3.addWidget(self.cyINV, 4, 2, 1, 1)
        self.cyDUP = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cyDUP.setMinimumSize(QtCore.QSize(0, 30))
        self.cyDUP.setObjectName("cyDUP")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.cyDUP.addItem("")
        self.gridLayout_3.addWidget(self.cyDUP, 5, 2, 1, 1)
        self.cyTRANS = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.cyTRANS.setMinimumSize(QtCore.QSize(0, 30))
        self.cyTRANS.setObjectName("cyTRANS")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.cyTRANS.addItem("")
        self.gridLayout_3.addWidget(self.cyTRANS, 6, 2, 1, 1)

        self.retranslateUi(nodeShapes)
        QtCore.QMetaObject.connectSlotsByName(nodeShapes)

    def retranslateUi(self, nodeShapes):
        _translate = QtCore.QCoreApplication.translate
        nodeShapes.setWindowTitle(_translate("nodeShapes", "Node Shapes"))
        self.label.setText(_translate("nodeShapes", "Node shapes showing in the graph"))
        self.label_2.setText(_translate("nodeShapes", "Backbone Nodes"))
        self.label_4.setText(_translate("nodeShapes", "Deletion "))
        self.label_5.setText(_translate("nodeShapes", "Insertion"))
        self.label_6.setText(_translate("nodeShapes", "Inversion"))
        self.label_7.setText(_translate("nodeShapes", "Duplication"))
        self.visBB.setItemText(0, _translate("nodeShapes", "dot"))
        self.visBB.setItemText(1, _translate("nodeShapes", "ellipse"))
        self.visBB.setItemText(2, _translate("nodeShapes", "circle"))
        self.visBB.setItemText(3, _translate("nodeShapes", "database"))
        self.visBB.setItemText(4, _translate("nodeShapes", "box"))
        self.visBB.setItemText(5, _translate("nodeShapes", "text"))
        self.visBB.setItemText(6, _translate("nodeShapes", "diamond"))
        self.visBB.setItemText(7, _translate("nodeShapes", "star"))
        self.visBB.setItemText(8, _translate("nodeShapes", "triangle"))
        self.visBB.setItemText(9, _translate("nodeShapes", "trangleDown"))
        self.label_3.setText(_translate("nodeShapes", "SNP"))
        self.label_8.setText(_translate("nodeShapes", "Translocation"))
        self.visSNP.setItemText(0, _translate("nodeShapes", "dot"))
        self.visSNP.setItemText(1, _translate("nodeShapes", "ellipse"))
        self.visSNP.setItemText(2, _translate("nodeShapes", "circle"))
        self.visSNP.setItemText(3, _translate("nodeShapes", "database"))
        self.visSNP.setItemText(4, _translate("nodeShapes", "box"))
        self.visSNP.setItemText(5, _translate("nodeShapes", "text"))
        self.visSNP.setItemText(6, _translate("nodeShapes", "diamond"))
        self.visSNP.setItemText(7, _translate("nodeShapes", "star"))
        self.visSNP.setItemText(8, _translate("nodeShapes", "trangle"))
        self.visSNP.setItemText(9, _translate("nodeShapes", "trangleDown"))
        self.visDEL.setItemText(0, _translate("nodeShapes", "triangle"))
        self.visDEL.setItemText(1, _translate("nodeShapes", "dot"))
        self.visDEL.setItemText(2, _translate("nodeShapes", "ellipse"))
        self.visDEL.setItemText(3, _translate("nodeShapes", "circle"))
        self.visDEL.setItemText(4, _translate("nodeShapes", "database"))
        self.visDEL.setItemText(5, _translate("nodeShapes", "box"))
        self.visDEL.setItemText(6, _translate("nodeShapes", "text"))
        self.visDEL.setItemText(7, _translate("nodeShapes", "diamond"))
        self.visDEL.setItemText(8, _translate("nodeShapes", "star"))
        self.visDEL.setItemText(9, _translate("nodeShapes", "triangleDown"))
        self.visINS.setItemText(0, _translate("nodeShapes", "triangleDown"))
        self.visINS.setItemText(1, _translate("nodeShapes", "dot"))
        self.visINS.setItemText(2, _translate("nodeShapes", "ellipse"))
        self.visINS.setItemText(3, _translate("nodeShapes", "circle"))
        self.visINS.setItemText(4, _translate("nodeShapes", "database"))
        self.visINS.setItemText(5, _translate("nodeShapes", "box"))
        self.visINS.setItemText(6, _translate("nodeShapes", "text"))
        self.visINS.setItemText(7, _translate("nodeShapes", "diamond"))
        self.visINS.setItemText(8, _translate("nodeShapes", "star"))
        self.visINS.setItemText(9, _translate("nodeShapes", "triangle"))
        self.visINV.setItemText(0, _translate("nodeShapes", "text"))
        self.visINV.setItemText(1, _translate("nodeShapes", "dot"))
        self.visINV.setItemText(2, _translate("nodeShapes", "ellipse"))
        self.visINV.setItemText(3, _translate("nodeShapes", "circle"))
        self.visINV.setItemText(4, _translate("nodeShapes", "database"))
        self.visINV.setItemText(5, _translate("nodeShapes", "box"))
        self.visINV.setItemText(6, _translate("nodeShapes", "diamond"))
        self.visINV.setItemText(7, _translate("nodeShapes", "star"))
        self.visINV.setItemText(8, _translate("nodeShapes", "triangle"))
        self.visINV.setItemText(9, _translate("nodeShapes", "triangleDown"))
        self.visDUP.setItemText(0, _translate("nodeShapes", "database"))
        self.visDUP.setItemText(1, _translate("nodeShapes", "dot"))
        self.visDUP.setItemText(2, _translate("nodeShapes", "ellipse"))
        self.visDUP.setItemText(3, _translate("nodeShapes", "circle"))
        self.visDUP.setItemText(4, _translate("nodeShapes", "box"))
        self.visDUP.setItemText(5, _translate("nodeShapes", "text"))
        self.visDUP.setItemText(6, _translate("nodeShapes", "diamond"))
        self.visDUP.setItemText(7, _translate("nodeShapes", "star"))
        self.visDUP.setItemText(8, _translate("nodeShapes", "triangle"))
        self.visDUP.setItemText(9, _translate("nodeShapes", "triangleDown"))
        self.visTRANS.setItemText(0, _translate("nodeShapes", "star"))
        self.visTRANS.setItemText(1, _translate("nodeShapes", "dot"))
        self.visTRANS.setItemText(2, _translate("nodeShapes", "ellipse"))
        self.visTRANS.setItemText(3, _translate("nodeShapes", "circle"))
        self.visTRANS.setItemText(4, _translate("nodeShapes", "database"))
        self.visTRANS.setItemText(5, _translate("nodeShapes", "box"))
        self.visTRANS.setItemText(6, _translate("nodeShapes", "text"))
        self.visTRANS.setItemText(7, _translate("nodeShapes", "diamond"))
        self.visTRANS.setItemText(8, _translate("nodeShapes", "triangle"))
        self.visTRANS.setItemText(9, _translate("nodeShapes", "triangleDown"))
        self.reset.setText(_translate("nodeShapes", "Reset"))
        self.label_9.setText(_translate("nodeShapes", "Do you want to keep the changes? "))
        self.change.setText(_translate("nodeShapes", "Yes"))
        self.label_10.setText(_translate("nodeShapes", "Vis.js Graph"))
        self.label_11.setText(_translate("nodeShapes", "Cytoscape.js Graph"))
        self.label_16.setText(_translate("nodeShapes", "Inversion"))
        self.label_14.setText(_translate("nodeShapes", "Deletion"))
        self.label_12.setText(_translate("nodeShapes", "Backbone Nodes"))
        self.label_17.setText(_translate("nodeShapes", "Duplication"))
        self.label_13.setText(_translate("nodeShapes", "SNP"))
        self.label_15.setText(_translate("nodeShapes", "Insertion"))
        self.cyBB.setItemText(0, _translate("nodeShapes", "ellipse"))
        self.cyBB.setItemText(1, _translate("nodeShapes", "triangle"))
        self.cyBB.setItemText(2, _translate("nodeShapes", "round-triangle"))
        self.cyBB.setItemText(3, _translate("nodeShapes", "rectangle"))
        self.cyBB.setItemText(4, _translate("nodeShapes", "round-rectangle"))
        self.cyBB.setItemText(5, _translate("nodeShapes", "bottom-round-rectangle"))
        self.cyBB.setItemText(6, _translate("nodeShapes", "cut-rectangle"))
        self.cyBB.setItemText(7, _translate("nodeShapes", "barrel"))
        self.cyBB.setItemText(8, _translate("nodeShapes", "rhomboid"))
        self.cyBB.setItemText(9, _translate("nodeShapes", "diamond"))
        self.cyBB.setItemText(10, _translate("nodeShapes", "round-diamond"))
        self.cyBB.setItemText(11, _translate("nodeShapes", "pentagon"))
        self.cyBB.setItemText(12, _translate("nodeShapes", "round-pentagon"))
        self.cyBB.setItemText(13, _translate("nodeShapes", "hexagon"))
        self.cyBB.setItemText(14, _translate("nodeShapes", "round-hexagon"))
        self.cyBB.setItemText(15, _translate("nodeShapes", "concave-hexagon"))
        self.cyBB.setItemText(16, _translate("nodeShapes", "heptagon"))
        self.cyBB.setItemText(17, _translate("nodeShapes", "round-heptagon"))
        self.cyBB.setItemText(18, _translate("nodeShapes", "octagon"))
        self.cyBB.setItemText(19, _translate("nodeShapes", "round-octagon"))
        self.cyBB.setItemText(20, _translate("nodeShapes", "star"))
        self.cyBB.setItemText(21, _translate("nodeShapes", "tag"))
        self.cyBB.setItemText(22, _translate("nodeShapes", "round-tag"))
        self.cyBB.setItemText(23, _translate("nodeShapes", "vee"))
        self.label_18.setText(_translate("nodeShapes", "Translocation"))
        self.cySNP.setItemText(0, _translate("nodeShapes", "ellipse"))
        self.cySNP.setItemText(1, _translate("nodeShapes", "triangle"))
        self.cySNP.setItemText(2, _translate("nodeShapes", "round-triangle"))
        self.cySNP.setItemText(3, _translate("nodeShapes", "rectangle"))
        self.cySNP.setItemText(4, _translate("nodeShapes", "round-rectangle"))
        self.cySNP.setItemText(5, _translate("nodeShapes", "bottom-round-rectangle"))
        self.cySNP.setItemText(6, _translate("nodeShapes", "cut-rectangle"))
        self.cySNP.setItemText(7, _translate("nodeShapes", "barrel"))
        self.cySNP.setItemText(8, _translate("nodeShapes", "rhomboid"))
        self.cySNP.setItemText(9, _translate("nodeShapes", "diamond"))
        self.cySNP.setItemText(10, _translate("nodeShapes", "round-diamond"))
        self.cySNP.setItemText(11, _translate("nodeShapes", "pentagon"))
        self.cySNP.setItemText(12, _translate("nodeShapes", "round-pentagon"))
        self.cySNP.setItemText(13, _translate("nodeShapes", "hexagon"))
        self.cySNP.setItemText(14, _translate("nodeShapes", "round-hexagon"))
        self.cySNP.setItemText(15, _translate("nodeShapes", "concave-hexagon"))
        self.cySNP.setItemText(16, _translate("nodeShapes", "heptagon"))
        self.cySNP.setItemText(17, _translate("nodeShapes", "round-heptagon"))
        self.cySNP.setItemText(18, _translate("nodeShapes", "octagon"))
        self.cySNP.setItemText(19, _translate("nodeShapes", "round-octagon"))
        self.cySNP.setItemText(20, _translate("nodeShapes", "star"))
        self.cySNP.setItemText(21, _translate("nodeShapes", "tag"))
        self.cySNP.setItemText(22, _translate("nodeShapes", "round-tag"))
        self.cySNP.setItemText(23, _translate("nodeShapes", "vee"))
        self.cyDEL.setItemText(0, _translate("nodeShapes", "concave-hexagon"))
        self.cyDEL.setItemText(1, _translate("nodeShapes", "ellipse"))
        self.cyDEL.setItemText(2, _translate("nodeShapes", "triangle"))
        self.cyDEL.setItemText(3, _translate("nodeShapes", "round-triangle"))
        self.cyDEL.setItemText(4, _translate("nodeShapes", "rectangle"))
        self.cyDEL.setItemText(5, _translate("nodeShapes", "round-rectangle"))
        self.cyDEL.setItemText(6, _translate("nodeShapes", "bottom-round-rectangle"))
        self.cyDEL.setItemText(7, _translate("nodeShapes", "cut-rectangle"))
        self.cyDEL.setItemText(8, _translate("nodeShapes", "barrel"))
        self.cyDEL.setItemText(9, _translate("nodeShapes", "rhomboid"))
        self.cyDEL.setItemText(10, _translate("nodeShapes", "diamond"))
        self.cyDEL.setItemText(11, _translate("nodeShapes", "round-diamond"))
        self.cyDEL.setItemText(12, _translate("nodeShapes", "pentagon"))
        self.cyDEL.setItemText(13, _translate("nodeShapes", "round-pentagon"))
        self.cyDEL.setItemText(14, _translate("nodeShapes", "hexagon"))
        self.cyDEL.setItemText(15, _translate("nodeShapes", "round-hexagon"))
        self.cyDEL.setItemText(16, _translate("nodeShapes", "heptagon"))
        self.cyDEL.setItemText(17, _translate("nodeShapes", "round-heptagon"))
        self.cyDEL.setItemText(18, _translate("nodeShapes", "octagon"))
        self.cyDEL.setItemText(19, _translate("nodeShapes", "round-octagon"))
        self.cyDEL.setItemText(20, _translate("nodeShapes", "star"))
        self.cyDEL.setItemText(21, _translate("nodeShapes", "tag"))
        self.cyDEL.setItemText(22, _translate("nodeShapes", "round-tag"))
        self.cyDEL.setItemText(23, _translate("nodeShapes", "vee"))
        self.cyINS.setItemText(0, _translate("nodeShapes", "triangle"))
        self.cyINS.setItemText(1, _translate("nodeShapes", "ellipse"))
        self.cyINS.setItemText(2, _translate("nodeShapes", "round-triangle"))
        self.cyINS.setItemText(3, _translate("nodeShapes", "rectangle"))
        self.cyINS.setItemText(4, _translate("nodeShapes", "round-rectangle"))
        self.cyINS.setItemText(5, _translate("nodeShapes", "bottom-round-rectangle"))
        self.cyINS.setItemText(6, _translate("nodeShapes", "cut-rectangle"))
        self.cyINS.setItemText(7, _translate("nodeShapes", "barrel"))
        self.cyINS.setItemText(8, _translate("nodeShapes", "rhomboid"))
        self.cyINS.setItemText(9, _translate("nodeShapes", "diamond"))
        self.cyINS.setItemText(10, _translate("nodeShapes", "round-diamond"))
        self.cyINS.setItemText(11, _translate("nodeShapes", "pentagon"))
        self.cyINS.setItemText(12, _translate("nodeShapes", "round-pentagon"))
        self.cyINS.setItemText(13, _translate("nodeShapes", "hexagon"))
        self.cyINS.setItemText(14, _translate("nodeShapes", "round-hexagon"))
        self.cyINS.setItemText(15, _translate("nodeShapes", "concave-hexagon"))
        self.cyINS.setItemText(16, _translate("nodeShapes", "heptagon"))
        self.cyINS.setItemText(17, _translate("nodeShapes", "round-heptagon"))
        self.cyINS.setItemText(18, _translate("nodeShapes", "octagon"))
        self.cyINS.setItemText(19, _translate("nodeShapes", "round-octagon"))
        self.cyINS.setItemText(20, _translate("nodeShapes", "star"))
        self.cyINS.setItemText(21, _translate("nodeShapes", "tag"))
        self.cyINS.setItemText(22, _translate("nodeShapes", "round-tag"))
        self.cyINS.setItemText(23, _translate("nodeShapes", "vee"))
        self.cyINV.setItemText(0, _translate("nodeShapes", "vee"))
        self.cyINV.setItemText(1, _translate("nodeShapes", "ellipse"))
        self.cyINV.setItemText(2, _translate("nodeShapes", "triangle"))
        self.cyINV.setItemText(3, _translate("nodeShapes", "round-triangle"))
        self.cyINV.setItemText(4, _translate("nodeShapes", "rectangle"))
        self.cyINV.setItemText(5, _translate("nodeShapes", "round-rectangle"))
        self.cyINV.setItemText(6, _translate("nodeShapes", "bottom-round-rectangle"))
        self.cyINV.setItemText(7, _translate("nodeShapes", "cut-rectangle"))
        self.cyINV.setItemText(8, _translate("nodeShapes", "barrel"))
        self.cyINV.setItemText(9, _translate("nodeShapes", "rhomboid"))
        self.cyINV.setItemText(10, _translate("nodeShapes", "diamond"))
        self.cyINV.setItemText(11, _translate("nodeShapes", "round-diamond"))
        self.cyINV.setItemText(12, _translate("nodeShapes", "pentagon"))
        self.cyINV.setItemText(13, _translate("nodeShapes", "round-pentagon"))
        self.cyINV.setItemText(14, _translate("nodeShapes", "hexagon"))
        self.cyINV.setItemText(15, _translate("nodeShapes", "round-hexagon"))
        self.cyINV.setItemText(16, _translate("nodeShapes", "concave-hexagon"))
        self.cyINV.setItemText(17, _translate("nodeShapes", "heptagon"))
        self.cyINV.setItemText(18, _translate("nodeShapes", "round-heptagon"))
        self.cyINV.setItemText(19, _translate("nodeShapes", "octagon"))
        self.cyINV.setItemText(20, _translate("nodeShapes", "round-octagon"))
        self.cyINV.setItemText(21, _translate("nodeShapes", "star"))
        self.cyINV.setItemText(22, _translate("nodeShapes", "tag"))
        self.cyINV.setItemText(23, _translate("nodeShapes", "round-tag"))
        self.cyDUP.setItemText(0, _translate("nodeShapes", "diamond"))
        self.cyDUP.setItemText(1, _translate("nodeShapes", "ellipse"))
        self.cyDUP.setItemText(2, _translate("nodeShapes", "triangle"))
        self.cyDUP.setItemText(3, _translate("nodeShapes", "round-triangle"))
        self.cyDUP.setItemText(4, _translate("nodeShapes", "rectangle"))
        self.cyDUP.setItemText(5, _translate("nodeShapes", "round-rectangle"))
        self.cyDUP.setItemText(6, _translate("nodeShapes", "bottom-round-rectangle"))
        self.cyDUP.setItemText(7, _translate("nodeShapes", "cut-rectangle"))
        self.cyDUP.setItemText(8, _translate("nodeShapes", "barrel"))
        self.cyDUP.setItemText(9, _translate("nodeShapes", "rhomboid"))
        self.cyDUP.setItemText(10, _translate("nodeShapes", "round-diamond"))
        self.cyDUP.setItemText(11, _translate("nodeShapes", "pentagon"))
        self.cyDUP.setItemText(12, _translate("nodeShapes", "round-pentagon"))
        self.cyDUP.setItemText(13, _translate("nodeShapes", "hexagon"))
        self.cyDUP.setItemText(14, _translate("nodeShapes", "round-hexagon"))
        self.cyDUP.setItemText(15, _translate("nodeShapes", "concave-hexagon"))
        self.cyDUP.setItemText(16, _translate("nodeShapes", "heptagon"))
        self.cyDUP.setItemText(17, _translate("nodeShapes", "round-heptagon"))
        self.cyDUP.setItemText(18, _translate("nodeShapes", "octagon"))
        self.cyDUP.setItemText(19, _translate("nodeShapes", "round-octagon"))
        self.cyDUP.setItemText(20, _translate("nodeShapes", "star"))
        self.cyDUP.setItemText(21, _translate("nodeShapes", "tag"))
        self.cyDUP.setItemText(22, _translate("nodeShapes", "round-tag"))
        self.cyDUP.setItemText(23, _translate("nodeShapes", "vee"))
        self.cyTRANS.setItemText(0, _translate("nodeShapes", "star"))
        self.cyTRANS.setItemText(1, _translate("nodeShapes", "ellipse"))
        self.cyTRANS.setItemText(2, _translate("nodeShapes", "triangle"))
        self.cyTRANS.setItemText(3, _translate("nodeShapes", "round-triangle"))
        self.cyTRANS.setItemText(4, _translate("nodeShapes", "rectangle"))
        self.cyTRANS.setItemText(5, _translate("nodeShapes", "round-rectangle"))
        self.cyTRANS.setItemText(6, _translate("nodeShapes", "bottom-round-rectangle"))
        self.cyTRANS.setItemText(7, _translate("nodeShapes", "cut-rectangle"))
        self.cyTRANS.setItemText(8, _translate("nodeShapes", "barrel"))
        self.cyTRANS.setItemText(9, _translate("nodeShapes", "rhomboid"))
        self.cyTRANS.setItemText(10, _translate("nodeShapes", "diamond"))
        self.cyTRANS.setItemText(11, _translate("nodeShapes", "round-diamond"))
        self.cyTRANS.setItemText(12, _translate("nodeShapes", "pentagon"))
        self.cyTRANS.setItemText(13, _translate("nodeShapes", "round-pentagon"))
        self.cyTRANS.setItemText(14, _translate("nodeShapes", "hexagon"))
        self.cyTRANS.setItemText(15, _translate("nodeShapes", "round-hexagon"))
        self.cyTRANS.setItemText(16, _translate("nodeShapes", "concave-hexagon"))
        self.cyTRANS.setItemText(17, _translate("nodeShapes", "heptagon"))
        self.cyTRANS.setItemText(18, _translate("nodeShapes", "round-heptagon"))
        self.cyTRANS.setItemText(19, _translate("nodeShapes", "octagon"))
        self.cyTRANS.setItemText(20, _translate("nodeShapes", "round-octagon"))
        self.cyTRANS.setItemText(21, _translate("nodeShapes", "tag"))
        self.cyTRANS.setItemText(22, _translate("nodeShapes", "round-tag"))
        self.cyTRANS.setItemText(23, _translate("nodeShapes", "vee"))
