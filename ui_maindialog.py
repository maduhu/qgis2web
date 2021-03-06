# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_maindialog.ui'
#
# Created: Tue Jul 14 13:58:00 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtWebKit
import resources_rc

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName(_fromUtf8("MainDialog"))
        MainDialog.resize(994, 736)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/qgis2web/icons/qgis2web.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainDialog.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(MainDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter_2 = QtGui.QSplitter(MainDialog)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layersTree = QtGui.QTreeWidget(self.splitter)
        self.layersTree.setMinimumSize(QtCore.QSize(400, 300))
        self.layersTree.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.layersTree.setObjectName(_fromUtf8("layersTree"))
        self.layersTree.headerItem().setText(0, _fromUtf8("1"))
        self.layersTree.header().setVisible(False)
        self.layersTree.header().setDefaultSectionSize(200)
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.paramsTreeOL = QtGui.QTreeWidget(self.widget)
        self.paramsTreeOL.setMinimumSize(QtCore.QSize(300, 0))
        self.paramsTreeOL.setFrameShape(QtGui.QFrame.StyledPanel)
        self.paramsTreeOL.setFrameShadow(QtGui.QFrame.Sunken)
        self.paramsTreeOL.setObjectName(_fromUtf8("paramsTreeOL"))
        self.paramsTreeOL.header().setVisible(True)
        self.paramsTreeOL.header().setCascadingSectionResizes(False)
        self.paramsTreeOL.header().setDefaultSectionSize(200)
        self.verticalLayout_5.addWidget(self.paramsTreeOL)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ol3 = QtGui.QRadioButton(self.widget)
        self.ol3.setChecked(True)
        self.ol3.setObjectName(_fromUtf8("ol3"))
        self.mapFormat = QtGui.QButtonGroup(MainDialog)
        self.mapFormat.setObjectName(_fromUtf8("mapFormat"))
        self.mapFormat.addButton(self.ol3)
        self.horizontalLayout_2.addWidget(self.ol3)
        self.leaflet = QtGui.QRadioButton(self.widget)
        self.leaflet.setObjectName(_fromUtf8("leaflet"))
        self.mapFormat.addButton(self.leaflet)
        self.horizontalLayout_2.addWidget(self.leaflet)
        self.buttonPreview = QtGui.QPushButton(self.widget)
        self.buttonPreview.setMinimumSize(QtCore.QSize(0, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/qgis2web/icons/preview.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPreview.setIcon(icon1)
        self.buttonPreview.setObjectName(_fromUtf8("buttonPreview"))
        self.horizontalLayout_2.addWidget(self.buttonPreview)
        self.buttonExport = QtGui.QPushButton(self.widget)
        self.buttonExport.setIcon(icon)
        self.buttonExport.setObjectName(_fromUtf8("buttonExport"))
        self.horizontalLayout_2.addWidget(self.buttonExport)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.splitter)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.splitter_2)
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.preview = QtWebKit.QWebView(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview.sizePolicy().hasHeightForWidth())
        self.preview.setSizePolicy(sizePolicy)
        self.preview.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.preview.setObjectName(_fromUtf8("preview"))
        self.verticalLayout_2.addWidget(self.preview)
        self.verticalLayout_3.addWidget(self.splitter_2)

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(_translate("MainDialog", "Export to web map", None))
        self.layersTree.headerItem().setText(1, _translate("MainDialog", "2", None))
        self.paramsTreeOL.headerItem().setText(0, _translate("MainDialog", "Setting", None))
        self.paramsTreeOL.headerItem().setText(1, _translate("MainDialog", "Value", None))
        self.ol3.setText(_translate("MainDialog", "OpenLayers 3", None))
        self.leaflet.setText(_translate("MainDialog", "Leaflet", None))
        self.buttonPreview.setText(_translate("MainDialog", "Update preview", None))
        self.buttonExport.setText(_translate("MainDialog", "Export", None))
