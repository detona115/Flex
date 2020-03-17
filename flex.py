# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flex.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../WORKSPACE LICLIPSE/Flex/fleximg2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QScrollBar{\n"
"     \n"
"     border: 2px solid #ccc;\n"
"       border-radius: 7px;\n"
"     background-color: #f8f8f8;\n"
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tabUsers = QtWidgets.QWidget()
        self.tabUsers.setObjectName("tabUsers")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabUsers)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidgetListUsers = QtWidgets.QTableWidget(self.tabUsers)
        self.tableWidgetListUsers.setStyleSheet("\n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;")
        self.tableWidgetListUsers.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidgetListUsers.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetListUsers.setObjectName("tableWidgetListUsers")
        self.tableWidgetListUsers.setColumnCount(8)
        self.tableWidgetListUsers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUsers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUsers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUsers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUsers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUsers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUsers.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUsers.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUsers.setHorizontalHeaderItem(7, item)
        self.tableWidgetListUsers.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableWidgetListUsers, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButtonListAllUsers = QtWidgets.QPushButton(self.tabUsers)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonListAllUsers.setFont(font)
        self.pushButtonListAllUsers.setStyleSheet("\n"
"#pushButtonListAllUsers{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;}\n"
"\n"
"#pushButtonListAllUsers:hover{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #e0e0e0;}\n"
"\n"
"#pushButtonListAllUsers:pressed{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #a0a0a0;}")
        self.pushButtonListAllUsers.setObjectName("pushButtonListAllUsers")
        self.gridLayout_2.addWidget(self.pushButtonListAllUsers, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tabUsers, "")
        self.tabNewDebt = QtWidgets.QWidget()
        self.tabNewDebt.setObjectName("tabNewDebt")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabNewDebt)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 2, 3, 1, 2)
        self.pushButtonSalvarDebt = QtWidgets.QPushButton(self.tabNewDebt)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSalvarDebt.setFont(font)
        self.pushButtonSalvarDebt.setStyleSheet("#pushButtonSalvarDebt{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;}\n"
"\n"
"#pushButtonSalvarDebt:hover{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #e0e0e0;}\n"
"\n"
"#pushButtonSalvarDebt:pressed{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #a0a0a0;}")
        self.pushButtonSalvarDebt.setObjectName("pushButtonSalvarDebt")
        self.gridLayout_4.addWidget(self.pushButtonSalvarDebt, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 2, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.tabNewDebt)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditMotivo = QtWidgets.QLineEdit(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditMotivo.sizePolicy().hasHeightForWidth())
        self.lineEditMotivo.setSizePolicy(sizePolicy)
        self.lineEditMotivo.setStyleSheet("padding: 5px 5px;\n"
"  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;")
        self.lineEditMotivo.setText("")
        self.lineEditMotivo.setObjectName("lineEditMotivo")
        self.gridLayout_3.addWidget(self.splitter_2, 1, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBoxClient = QtWidgets.QComboBox(self.splitter)
        self.comboBoxClient.setStyleSheet("padding: 5px 5px;\n"
"  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;")
        self.comboBoxClient.setEditable(False)
        self.comboBoxClient.setObjectName("comboBoxClient")
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.doubleSpinBoxValor = QtWidgets.QDoubleSpinBox(self.splitter_3)
        self.doubleSpinBoxValor.setStyleSheet("padding: 5px 5px;\n"
"  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;")
        self.doubleSpinBoxValor.setMaximum(1000000000000000.0)
        self.doubleSpinBoxValor.setObjectName("doubleSpinBoxValor")
        self.gridLayout_3.addWidget(self.splitter_3, 2, 0, 1, 1)
        self.splitter_4 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label_4 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dateEditData = QtWidgets.QDateEdit(self.splitter_4)
        self.dateEditData.setStyleSheet("padding: 5px 5px;\n"
"  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;")
        self.dateEditData.setObjectName("dateEditData")
        self.gridLayout_3.addWidget(self.splitter_4, 3, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 1, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem8, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tabNewDebt, "")
        self.tabUserDebt = QtWidgets.QWidget()
        self.tabUserDebt.setObjectName("tabUserDebt")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tabUserDebt)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem9, 2, 0, 1, 1)
        self.tableWidgetListUserDebt = QtWidgets.QTableWidget(self.tabUserDebt)
        self.tableWidgetListUserDebt.setStyleSheet("\n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;")
        self.tableWidgetListUserDebt.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetListUserDebt.setObjectName("tableWidgetListUserDebt")
        self.tableWidgetListUserDebt.setColumnCount(4)
        self.tableWidgetListUserDebt.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUserDebt.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUserDebt.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUserDebt.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUserDebt.setHorizontalHeaderItem(3, item)
        self.tableWidgetListUserDebt.verticalHeader().setVisible(False)
        self.gridLayout_7.addWidget(self.tableWidgetListUserDebt, 0, 2, 8, 1)
        self.splitter_5 = QtWidgets.QSplitter(self.tabUserDebt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_5.sizePolicy().hasHeightForWidth())
        self.splitter_5.setSizePolicy(sizePolicy)
        self.splitter_5.setMinimumSize(QtCore.QSize(281, 61))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.label_5 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBoxSelectClient = QtWidgets.QComboBox(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSelectClient.sizePolicy().hasHeightForWidth())
        self.comboBoxSelectClient.setSizePolicy(sizePolicy)
        self.comboBoxSelectClient.setStyleSheet("padding: 5px 5px;\n"
"  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;")
        self.comboBoxSelectClient.setObjectName("comboBoxSelectClient")
        self.gridLayout_7.addWidget(self.splitter_5, 0, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabUserDebt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.splitter_6 = QtWidgets.QSplitter(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_6.sizePolicy().hasHeightForWidth())
        self.splitter_6.setSizePolicy(sizePolicy)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.label_6 = QtWidgets.QLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.comboBoxIdDivida = QtWidgets.QComboBox(self.splitter_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxIdDivida.sizePolicy().hasHeightForWidth())
        self.comboBoxIdDivida.setSizePolicy(sizePolicy)
        self.comboBoxIdDivida.setStyleSheet("padding: 5px 5px;\n"
"  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;")
        self.comboBoxIdDivida.setObjectName("comboBoxIdDivida")
        self.gridLayout_5.addWidget(self.splitter_6, 0, 0, 1, 1)
        self.pushButtonExcluirDivida = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonExcluirDivida.sizePolicy().hasHeightForWidth())
        self.pushButtonExcluirDivida.setSizePolicy(sizePolicy)
        self.pushButtonExcluirDivida.setMinimumSize(QtCore.QSize(117, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonExcluirDivida.setFont(font)
        self.pushButtonExcluirDivida.setStyleSheet("#pushButtonExcluirDivida{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;}\n"
"\n"
"#pushButtonExcluirDivida:hover{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #e0e0e0;}\n"
"\n"
"#pushButtonExcluirDivida:pressed{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #a0a0a0;}")
        self.pushButtonExcluirDivida.setObjectName("pushButtonExcluirDivida")
        self.gridLayout_5.addWidget(self.pushButtonExcluirDivida, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.pushButtonListClientDebts = QtWidgets.QPushButton(self.tabUserDebt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonListClientDebts.sizePolicy().hasHeightForWidth())
        self.pushButtonListClientDebts.setSizePolicy(sizePolicy)
        self.pushButtonListClientDebts.setMinimumSize(QtCore.QSize(117, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonListClientDebts.setFont(font)
        self.pushButtonListClientDebts.setStyleSheet("#pushButtonListClientDebts{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;}\n"
"\n"
"#pushButtonListClientDebts:hover{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #e0e0e0;}\n"
"\n"
"#pushButtonListClientDebts:pressed{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #a0a0a0;}")
        self.pushButtonListClientDebts.setObjectName("pushButtonListClientDebts")
        self.gridLayout_7.addWidget(self.pushButtonListClientDebts, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem10, 4, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabUserDebt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.splitter_7 = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.label_7 = QtWidgets.QLabel(self.splitter_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter_7)
        self.lineEdit.setStyleSheet("padding: 5px 5px;\n"
"  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.splitter_7, 0, 0, 1, 1)
        self.splitter_8 = QtWidgets.QSplitter(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_8.sizePolicy().hasHeightForWidth())
        self.splitter_8.setSizePolicy(sizePolicy)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.label_8 = QtWidgets.QLabel(self.splitter_8)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.dateEdit = QtWidgets.QDateEdit(self.splitter_8)
        self.dateEdit.setStyleSheet("padding: 5px 5px;\n"
"  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;")
        self.dateEdit.setWrapping(True)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_6.addWidget(self.splitter_8, 0, 1, 1, 1)
        self.splitter_9 = QtWidgets.QSplitter(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_9.sizePolicy().hasHeightForWidth())
        self.splitter_9.setSizePolicy(sizePolicy)
        self.splitter_9.setOrientation(QtCore.Qt.Vertical)
        self.splitter_9.setObjectName("splitter_9")
        self.label_9 = QtWidgets.QLabel(self.splitter_9)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.splitter_9)
        self.doubleSpinBox.setStyleSheet("padding: 5px 5px;\n"
"  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;")
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_6.addWidget(self.splitter_9, 0, 2, 1, 1)
        self.pushButtonAlterarDivida = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAlterarDivida.sizePolicy().hasHeightForWidth())
        self.pushButtonAlterarDivida.setSizePolicy(sizePolicy)
        self.pushButtonAlterarDivida.setMinimumSize(QtCore.QSize(117, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAlterarDivida.setFont(font)
        self.pushButtonAlterarDivida.setStyleSheet("#pushButtonAlterarDivida{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #f8f8f8;}\n"
"\n"
"#pushButtonAlterarDivida:hover{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #e0e0e0;}\n"
"\n"
"#pushButtonAlterarDivida:pressed{\n"
"  padding: 5px 5px;  \n"
"  border: 2px solid #ccc;\n"
"  border-radius: 4px;\n"
"  background-color: #a0a0a0;}")
        self.pushButtonAlterarDivida.setAutoRepeat(True)
        self.pushButtonAlterarDivida.setAutoExclusive(False)
        self.pushButtonAlterarDivida.setAutoDefault(False)
        self.pushButtonAlterarDivida.setDefault(False)
        self.pushButtonAlterarDivida.setFlat(False)
        self.pushButtonAlterarDivida.setObjectName("pushButtonAlterarDivida")
        self.gridLayout_6.addWidget(self.pushButtonAlterarDivida, 1, 0, 1, 2)
        self.gridLayout_7.addWidget(self.groupBox_3, 5, 0, 1, 2)
        self.tabWidget.addTab(self.tabUserDebt, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FLEX CONTACT"))
        item = self.tableWidgetListUsers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidgetListUsers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetListUsers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "User Name"))
        item = self.tableWidgetListUsers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidgetListUsers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidgetListUsers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Street"))
        item = self.tableWidgetListUsers.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Zip Code"))
        item = self.tableWidgetListUsers.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Phone"))
        self.pushButtonListAllUsers.setText(_translate("MainWindow", "List All Users"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUsers), _translate("MainWindow", "List Users"))
        self.pushButtonSalvarDebt.setText(_translate("MainWindow", "Salvar"))
        self.groupBox.setTitle(_translate("MainWindow", "Inserir Nova Dívida"))
        self.label_2.setText(_translate("MainWindow", "Motivo"))
        self.label.setText(_translate("MainWindow", "Cliente"))
        self.label_3.setText(_translate("MainWindow", "Valor"))
        self.label_4.setText(_translate("MainWindow", "Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNewDebt), _translate("MainWindow", "New Debt"))
        item = self.tableWidgetListUserDebt.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidgetListUserDebt.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Motivo da dívida"))
        item = self.tableWidgetListUserDebt.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Data da dívida"))
        item = self.tableWidgetListUserDebt.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Valor"))
        self.label_5.setText(_translate("MainWindow", "Select Client"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Deletar Dívida"))
        self.label_6.setText(_translate("MainWindow", "ID Dívida"))
        self.pushButtonExcluirDivida.setText(_translate("MainWindow", "Excluir Dívida"))
        self.pushButtonListClientDebts.setText(_translate("MainWindow", "List Client Debts"))
        self.groupBox_3.setToolTip(_translate("MainWindow", "Selecionar ID Dívida antes de alterar uma dívida"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Alterar Dívida"))
        self.label_7.setText(_translate("MainWindow", "Motivo"))
        self.label_8.setText(_translate("MainWindow", "Data"))
        self.label_9.setText(_translate("MainWindow", "Valor"))
        self.pushButtonAlterarDivida.setText(_translate("MainWindow", "Alterar Dívida"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUserDebt), _translate("MainWindow", "List User Debt"))

        ### Alinhando as colunas da tabela list users

        self.tableWidgetListUsers.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidgetListUsers.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidgetListUsers.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidgetListUsers.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidgetListUsers.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidgetListUsers.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidgetListUsers.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.tableWidgetListUsers.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)

        ### Alinhando as colunas da tabela list user

        self.tableWidgetListUserDebt.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidgetListUserDebt.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidgetListUserDebt.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidgetListUserDebt.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)


