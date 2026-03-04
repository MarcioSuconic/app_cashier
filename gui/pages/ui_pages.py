# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesxExSlF.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QDateEdit, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(833, 680)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(application_pages.sizePolicy().hasHeightForWidth())
        application_pages.setSizePolicy(sizePolicy)
        application_pages.setStyleSheet(u"")
        self.ver_despesas_cx = QWidget()
        self.ver_despesas_cx.setObjectName(u"ver_despesas_cx")
        self.verticalLayout_6 = QVBoxLayout(self.ver_despesas_cx)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_ver_despesas = QFrame(self.ver_despesas_cx)
        self.frame_ver_despesas.setObjectName(u"frame_ver_despesas")
        self.frame_ver_despesas.setMinimumSize(QSize(600, 600))
        self.frame_ver_despesas.setMaximumSize(QSize(600, 600))
        self.frame_ver_despesas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ver_despesas.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_ver_despesas)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_16)

        self.label_26 = QLabel(self.frame_ver_despesas)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: white;")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_26)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_34 = QLabel(self.frame_ver_despesas)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.label_34, 0, Qt.AlignmentFlag.AlignHCenter)

        self.data_cx_ver_despesa = QDateEdit(self.frame_ver_despesas)
        self.data_cx_ver_despesa.setObjectName(u"data_cx_ver_despesa")
        self.data_cx_ver_despesa.setMinimumSize(QSize(120, 0))
        self.data_cx_ver_despesa.setMaximumSize(QSize(120, 16777215))
        self.data_cx_ver_despesa.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(0,0,0);")
        self.data_cx_ver_despesa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_cx_ver_despesa.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.data_cx_ver_despesa, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.table_ver_despesas = QTableView(self.frame_ver_despesas)
        self.table_ver_despesas.setObjectName(u"table_ver_despesas")
        self.table_ver_despesas.setMinimumSize(QSize(540, 220))
        self.table_ver_despesas.setMaximumSize(QSize(540, 220))
        self.table_ver_despesas.setStyleSheet(u"QTableView {\n"
"	alternate-background-color: #f8f9fa;\n"
"	background-color: white;\n"
"	gridline-color: #dee2e6;\n"
"}\n"
"\n"
"QTableView::item {\n"
"	padding: 5px;\n"
"	border-bottom: 1px solid #dee2e6;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"	background-color: #007bff;\n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: #6c757d;\n"
"	color: white;\n"
"	padding: 5px;\n"
"	border: 1px solid #5a6268;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_11.addWidget(self.table_ver_despesas, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_25 = QLabel(self.frame_ver_despesas)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.label_25)

        self.input_id_despesa_caixa_a_deletar = QLineEdit(self.frame_ver_despesas)
        self.input_id_despesa_caixa_a_deletar.setObjectName(u"input_id_despesa_caixa_a_deletar")
        self.input_id_despesa_caixa_a_deletar.setMinimumSize(QSize(40, 0))
        self.input_id_despesa_caixa_a_deletar.setMaximumSize(QSize(40, 16777215))
        self.input_id_despesa_caixa_a_deletar.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: rgb(68,71,90);\n"
"")
        self.input_id_despesa_caixa_a_deletar.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.input_id_despesa_caixa_a_deletar)

        self.btn_deletar_despesa_cx = QPushButton(self.frame_ver_despesas)
        self.btn_deletar_despesa_cx.setObjectName(u"btn_deletar_despesa_cx")
        self.btn_deletar_despesa_cx.setMinimumSize(QSize(140, 0))
        self.btn_deletar_despesa_cx.setMaximumSize(QSize(140, 16777215))
        self.btn_deletar_despesa_cx.setStyleSheet(u"QPushButton {\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	background-color: rgb(110,40,40);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_deletar_despesa_cx)

        self.btn_inserir_despesa_cx = QPushButton(self.frame_ver_despesas)
        self.btn_inserir_despesa_cx.setObjectName(u"btn_inserir_despesa_cx")
        self.btn_inserir_despesa_cx.setStyleSheet(u"QPushButton {\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	background-color: rgb(50,50,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_inserir_despesa_cx)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_8)


        self.verticalLayout_6.addWidget(self.frame_ver_despesas, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        application_pages.addWidget(self.ver_despesas_cx)
        self.observacao_cx = QWidget()
        self.observacao_cx.setObjectName(u"observacao_cx")
        self.verticalLayout_5 = QVBoxLayout(self.observacao_cx)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.observacao_cx)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_17)

        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(360, 0))
        self.label_23.setMaximumSize(QSize(360, 16777215))
        self.label_23.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_23, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_15)

        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(175, 0))
        self.label_24.setMaximumSize(QSize(175, 16777215))
        self.label_24.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_24)

        self.data_cx_observacao = QDateEdit(self.frame_2)
        self.data_cx_observacao.setObjectName(u"data_cx_observacao")
        self.data_cx_observacao.setEnabled(True)
        sizePolicy.setHeightForWidth(self.data_cx_observacao.sizePolicy().hasHeightForWidth())
        self.data_cx_observacao.setSizePolicy(sizePolicy)
        self.data_cx_observacao.setMinimumSize(QSize(120, 0))
        self.data_cx_observacao.setMaximumSize(QSize(120, 16777215))
        self.data_cx_observacao.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(0,0,0);")
        self.data_cx_observacao.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_cx_observacao.setReadOnly(True)

        self.horizontalLayout.addWidget(self.data_cx_observacao)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_16)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_24)

        self.label_76 = QLabel(self.frame_2)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_76.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_76)

        self.textEdit_observacao_cx = QTextEdit(self.frame_2)
        self.textEdit_observacao_cx.setObjectName(u"textEdit_observacao_cx")
        self.textEdit_observacao_cx.setMinimumSize(QSize(0, 80))
        self.textEdit_observacao_cx.setMaximumSize(QSize(16777215, 80))
        self.textEdit_observacao_cx.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 1px;\n"
"border-radius: 10px;")

        self.verticalLayout_4.addWidget(self.textEdit_observacao_cx)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_25)

        self.tableView_observacoes_cx = QTableView(self.frame_2)
        self.tableView_observacoes_cx.setObjectName(u"tableView_observacoes_cx")
        self.tableView_observacoes_cx.setStyleSheet(u"QTableView {\n"
"	alternate-background-color: #f8f9fa;\n"
"	background-color: white;\n"
"	gridline-color: #dee2e6;\n"
"}\n"
"\n"
"QTableView::item {\n"
"	padding: 5px;\n"
"	border-bottom: 1px solid #dee2e6;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"	background-color: #007bff;\n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: #6c757d;\n"
"	color: white;\n"
"	padding: 5px;\n"
"	border: 1px solid #5a6268;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_4.addWidget(self.tableView_observacoes_cx)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.label_44 = QLabel(self.frame_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_14.addWidget(self.label_44)

        self.input_id_observacao_a_deletar = QLineEdit(self.frame_2)
        self.input_id_observacao_a_deletar.setObjectName(u"input_id_observacao_a_deletar")
        self.input_id_observacao_a_deletar.setMinimumSize(QSize(40, 0))
        self.input_id_observacao_a_deletar.setMaximumSize(QSize(40, 16777215))
        self.input_id_observacao_a_deletar.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_id_observacao_a_deletar.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.input_id_observacao_a_deletar)

        self.btn_deletar_observacao = QPushButton(self.frame_2)
        self.btn_deletar_observacao.setObjectName(u"btn_deletar_observacao")
        self.btn_deletar_observacao.setMinimumSize(QSize(180, 0))
        self.btn_deletar_observacao.setMaximumSize(QSize(180, 16777215))
        self.btn_deletar_observacao.setStyleSheet(u"QPushButton {\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	background-color: rgb(110,40,40);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_14.addWidget(self.btn_deletar_observacao)

        self.btn_inserir_observacao = QPushButton(self.frame_2)
        self.btn_inserir_observacao.setObjectName(u"btn_inserir_observacao")
        self.btn_inserir_observacao.setMinimumSize(QSize(180, 0))
        self.btn_inserir_observacao.setMaximumSize(QSize(180, 16777215))
        self.btn_inserir_observacao.setStyleSheet(u"QPushButton {\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	background-color: rgb(50,50,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_14.addWidget(self.btn_inserir_observacao)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.verticalLayout_5.addWidget(self.frame_2)

        application_pages.addWidget(self.observacao_cx)
        self.fecham_cx = QWidget()
        self.fecham_cx.setObjectName(u"fecham_cx")
        self.frame_fechamento_caixa = QFrame(self.fecham_cx)
        self.frame_fechamento_caixa.setObjectName(u"frame_fechamento_caixa")
        self.frame_fechamento_caixa.setGeometry(QRect(0, 0, 840, 580))
        self.frame_fechamento_caixa.setMinimumSize(QSize(840, 580))
        self.frame_fechamento_caixa.setMaximumSize(QSize(840, 580))
        self.frame_fechamento_caixa.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fechamento_caixa.setFrameShadow(QFrame.Shadow.Raised)
        self.groupBox = QGroupBox(self.frame_fechamento_caixa)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(440, 10, 248, 91))
        self.groupBox.setStyleSheet(u"color: white;")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.label_28)

        self.data_cx_fechamento_cx = QDateEdit(self.groupBox)
        self.data_cx_fechamento_cx.setObjectName(u"data_cx_fechamento_cx")
        self.data_cx_fechamento_cx.setMinimumSize(QSize(120, 0))
        self.data_cx_fechamento_cx.setMaximumSize(QSize(120, 16777215))
        self.data_cx_fechamento_cx.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(0,0,0);")
        self.data_cx_fechamento_cx.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_cx_fechamento_cx.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.data_cx_fechamento_cx)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_29 = QLabel(self.groupBox)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.label_29)

        self.vendas_lida_dia_fecham_cx = QLineEdit(self.groupBox)
        self.vendas_lida_dia_fecham_cx.setObjectName(u"vendas_lida_dia_fecham_cx")
        self.vendas_lida_dia_fecham_cx.setMinimumSize(QSize(120, 0))
        self.vendas_lida_dia_fecham_cx.setMaximumSize(QSize(120, 16777215))
        self.vendas_lida_dia_fecham_cx.setStyleSheet(u"color: lightblue;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.vendas_lida_dia_fecham_cx.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vendas_lida_dia_fecham_cx.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.vendas_lida_dia_fecham_cx)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.groupBox_despesas_cx = QGroupBox(self.frame_fechamento_caixa)
        self.groupBox_despesas_cx.setObjectName(u"groupBox_despesas_cx")
        self.groupBox_despesas_cx.setGeometry(QRect(20, 490, 381, 71))
        self.groupBox_despesas_cx.setStyleSheet(u"color: white;")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_despesas_cx)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.label_47 = QLabel(self.groupBox_despesas_cx)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")

        self.horizontalLayout_7.addWidget(self.label_47)

        self.input_total_despesas_caixa_fecham_cx = QLineEdit(self.groupBox_despesas_cx)
        self.input_total_despesas_caixa_fecham_cx.setObjectName(u"input_total_despesas_caixa_fecham_cx")
        self.input_total_despesas_caixa_fecham_cx.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_total_despesas_caixa_fecham_cx.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_total_despesas_caixa_fecham_cx.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.input_total_despesas_caixa_fecham_cx)

        self.btn_ver_despesas = QPushButton(self.groupBox_despesas_cx)
        self.btn_ver_despesas.setObjectName(u"btn_ver_despesas")
        self.btn_ver_despesas.setMinimumSize(QSize(40, 28))
        self.btn_ver_despesas.setMaximumSize(QSize(40, 28))
        self.btn_ver_despesas.setStyleSheet(u"QPushButton {\n"
"	font: 350 7pt \"Segoe UI\";\n"
"	background-color: rgb(50,90,50);\n"
"	padding: 2px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_ver_despesas)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.groupBox_troco = QGroupBox(self.frame_fechamento_caixa)
        self.groupBox_troco.setObjectName(u"groupBox_troco")
        self.groupBox_troco.setGeometry(QRect(20, 170, 351, 141))
        self.groupBox_troco.setStyleSheet(u"color: white;")
        self.input_troco_fecham_cx = QLineEdit(self.groupBox_troco)
        self.input_troco_fecham_cx.setObjectName(u"input_troco_fecham_cx")
        self.input_troco_fecham_cx.setGeometry(QRect(170, 32, 120, 16))
        self.input_troco_fecham_cx.setMinimumSize(QSize(120, 0))
        self.input_troco_fecham_cx.setMaximumSize(QSize(120, 16777215))
        self.input_troco_fecham_cx.setStyleSheet(u"color: white;\n"
"background-color: #5a7a5a;\n"
"border: solid gray 2px;")
        self.input_troco_fecham_cx.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_18 = QLabel(self.groupBox_troco)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 30, 151, 16))
        self.label_18.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_estoque_troco_fecham_cx = QLineEdit(self.groupBox_troco)
        self.input_estoque_troco_fecham_cx.setObjectName(u"input_estoque_troco_fecham_cx")
        self.input_estoque_troco_fecham_cx.setGeometry(QRect(170, 72, 120, 16))
        self.input_estoque_troco_fecham_cx.setMinimumSize(QSize(120, 0))
        self.input_estoque_troco_fecham_cx.setMaximumSize(QSize(120, 16777215))
        self.input_estoque_troco_fecham_cx.setStyleSheet(u"color: white;\n"
"background-color: #9a5a9a;\n"
"border: solid gray 2px;")
        self.input_estoque_troco_fecham_cx.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_37 = QLabel(self.groupBox_troco)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 70, 151, 16))
        self.label_37.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_38 = QLabel(self.groupBox_troco)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 50, 151, 16))
        self.label_38.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_troco_fecham_cx_anterior = QLineEdit(self.groupBox_troco)
        self.input_troco_fecham_cx_anterior.setObjectName(u"input_troco_fecham_cx_anterior")
        self.input_troco_fecham_cx_anterior.setGeometry(QRect(170, 52, 120, 16))
        self.input_troco_fecham_cx_anterior.setMinimumSize(QSize(120, 0))
        self.input_troco_fecham_cx_anterior.setMaximumSize(QSize(120, 16777215))
        self.input_troco_fecham_cx_anterior.setStyleSheet(u"color: white;\n"
"background-color: #5a7a5a;\n"
"border: solid gray 2px;")
        self.input_troco_fecham_cx_anterior.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_troco_fecham_cx_anterior.setReadOnly(True)
        self.label_39 = QLabel(self.groupBox_troco)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 90, 151, 16))
        self.label_39.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_est_troco_fecham_cx_ant = QLineEdit(self.groupBox_troco)
        self.input_est_troco_fecham_cx_ant.setObjectName(u"input_est_troco_fecham_cx_ant")
        self.input_est_troco_fecham_cx_ant.setGeometry(QRect(170, 92, 120, 16))
        self.input_est_troco_fecham_cx_ant.setMinimumSize(QSize(120, 0))
        self.input_est_troco_fecham_cx_ant.setMaximumSize(QSize(120, 16777215))
        self.input_est_troco_fecham_cx_ant.setStyleSheet(u"color: white;\n"
"background-color: #7a5a7a;\n"
"border: solid gray 2px;")
        self.input_est_troco_fecham_cx_ant.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_est_troco_fecham_cx_ant.setReadOnly(True)
        self.label_40 = QLabel(self.groupBox_troco)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 112, 151, 16))
        self.label_40.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.result_troco_fechamento_cx = QLineEdit(self.groupBox_troco)
        self.result_troco_fechamento_cx.setObjectName(u"result_troco_fechamento_cx")
        self.result_troco_fechamento_cx.setGeometry(QRect(170, 114, 120, 16))
        self.result_troco_fechamento_cx.setMinimumSize(QSize(120, 0))
        self.result_troco_fechamento_cx.setMaximumSize(QSize(120, 16777215))
        self.result_troco_fechamento_cx.setStyleSheet(u"color: white;\n"
"background-color: #884444;\n"
"border: solid gray 2px;")
        self.result_troco_fechamento_cx.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_troco_fechamento_cx.setReadOnly(True)
        self.btn_repetir_troco_cx = QPushButton(self.groupBox_troco)
        self.btn_repetir_troco_cx.setObjectName(u"btn_repetir_troco_cx")
        self.btn_repetir_troco_cx.setGeometry(QRect(300, 40, 48, 28))
        self.btn_repetir_troco_cx.setMinimumSize(QSize(48, 28))
        self.btn_repetir_troco_cx.setMaximumSize(QSize(48, 28))
        self.btn_repetir_troco_cx.setStyleSheet(u"QPushButton {\n"
"	font: 350 7pt \"Segoe UI\";\n"
"	background-color: #5a8a5a;\n"
"	padding: 2px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        self.btn_repetir_estoque_troco_cx = QPushButton(self.groupBox_troco)
        self.btn_repetir_estoque_troco_cx.setObjectName(u"btn_repetir_estoque_troco_cx")
        self.btn_repetir_estoque_troco_cx.setGeometry(QRect(300, 80, 48, 28))
        self.btn_repetir_estoque_troco_cx.setMinimumSize(QSize(48, 28))
        self.btn_repetir_estoque_troco_cx.setMaximumSize(QSize(48, 28))
        self.btn_repetir_estoque_troco_cx.setStyleSheet(u"QPushButton {\n"
"	font: 350 7pt \"Segoe UI\";\n"
"	background-color: #6a5a6a;\n"
"	padding: 2px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        self.groupBox_entradas = QGroupBox(self.frame_fechamento_caixa)
        self.groupBox_entradas.setObjectName(u"groupBox_entradas")
        self.groupBox_entradas.setGeometry(QRect(20, 10, 351, 161))
        self.groupBox_entradas.setStyleSheet(u"color: white;")
        self.label_31 = QLabel(self.groupBox_entradas)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(23, 33, 143, 16))
        self.label_31.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")
        self.label_35 = QLabel(self.groupBox_entradas)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(23, 56, 143, 16))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy1)
        self.label_35.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_vendas_dinheiro_dia_fecham_cx = QLineEdit(self.groupBox_entradas)
        self.input_vendas_dinheiro_dia_fecham_cx.setObjectName(u"input_vendas_dinheiro_dia_fecham_cx")
        self.input_vendas_dinheiro_dia_fecham_cx.setGeometry(QRect(172, 56, 120, 16))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_vendas_dinheiro_dia_fecham_cx.sizePolicy().hasHeightForWidth())
        self.input_vendas_dinheiro_dia_fecham_cx.setSizePolicy(sizePolicy2)
        self.input_vendas_dinheiro_dia_fecham_cx.setMinimumSize(QSize(120, 0))
        self.input_vendas_dinheiro_dia_fecham_cx.setMaximumSize(QSize(120, 16777215))
        self.input_vendas_dinheiro_dia_fecham_cx.setStyleSheet(u"color: lightblue;\n"
"background-color: #5a7a5a;\n"
"border: solid gray 2px;")
        self.input_vendas_dinheiro_dia_fecham_cx.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_vendas_dinheiro_dia_fecham_cx.setReadOnly(True)
        self.label_36 = QLabel(self.groupBox_entradas)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(20, 76, 141, 20))
        sizePolicy1.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy1)
        self.label_36.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_vendas_pix_direto_cnpj_dia_fecham_cx = QLineEdit(self.groupBox_entradas)
        self.input_vendas_pix_direto_cnpj_dia_fecham_cx.setObjectName(u"input_vendas_pix_direto_cnpj_dia_fecham_cx")
        self.input_vendas_pix_direto_cnpj_dia_fecham_cx.setGeometry(QRect(172, 76, 120, 17))
        sizePolicy2.setHeightForWidth(self.input_vendas_pix_direto_cnpj_dia_fecham_cx.sizePolicy().hasHeightForWidth())
        self.input_vendas_pix_direto_cnpj_dia_fecham_cx.setSizePolicy(sizePolicy2)
        self.input_vendas_pix_direto_cnpj_dia_fecham_cx.setMinimumSize(QSize(120, 0))
        self.input_vendas_pix_direto_cnpj_dia_fecham_cx.setMaximumSize(QSize(120, 16777215))
        self.input_vendas_pix_direto_cnpj_dia_fecham_cx.setBaseSize(QSize(0, 0))
        self.input_vendas_pix_direto_cnpj_dia_fecham_cx.setStyleSheet(u"color: lightblue;\n"
"background-color: #5a7a5a;\n"
"border: solid gray 2px;")
        self.input_vendas_pix_direto_cnpj_dia_fecham_cx.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_vendas_pix_direto_cnpj_dia_fecham_cx.setReadOnly(True)
        self.input_total_maq_cartoes_fecham_cx = QLineEdit(self.groupBox_entradas)
        self.input_total_maq_cartoes_fecham_cx.setObjectName(u"input_total_maq_cartoes_fecham_cx")
        self.input_total_maq_cartoes_fecham_cx.setGeometry(QRect(172, 33, 120, 18))
        self.input_total_maq_cartoes_fecham_cx.setMinimumSize(QSize(120, 0))
        self.input_total_maq_cartoes_fecham_cx.setMaximumSize(QSize(120, 16777215))
        self.input_total_maq_cartoes_fecham_cx.setStyleSheet(u"color: lightblue;\n"
"background-color: #5a5a5a;\n"
"border: solid gray 2px;")
        self.input_total_maq_cartoes_fecham_cx.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_69 = QLabel(self.groupBox_entradas)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(90, 120, 71, 16))
        self.label_69.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: #7a5a5a;")
        self.label_69.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_diferenca = QLineEdit(self.groupBox_entradas)
        self.input_diferenca.setObjectName(u"input_diferenca")
        self.input_diferenca.setGeometry(QRect(172, 120, 120, 17))
        sizePolicy2.setHeightForWidth(self.input_diferenca.sizePolicy().hasHeightForWidth())
        self.input_diferenca.setSizePolicy(sizePolicy2)
        self.input_diferenca.setMinimumSize(QSize(120, 0))
        self.input_diferenca.setMaximumSize(QSize(120, 16777215))
        self.input_diferenca.setBaseSize(QSize(0, 0))
        self.input_diferenca.setStyleSheet(u"color: lightblue;\n"
"background-color: #7a5a5a;\n"
"border: solid gray 2px;")
        self.input_diferenca.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_diferenca.setReadOnly(True)
        self.label_73 = QLabel(self.groupBox_entradas)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(30, 98, 131, 20))
        sizePolicy1.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy1)
        self.label_73.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")
        self.label_73.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_vendas_pix_direto_cpf_dia_fecham_cx = QLineEdit(self.groupBox_entradas)
        self.input_vendas_pix_direto_cpf_dia_fecham_cx.setObjectName(u"input_vendas_pix_direto_cpf_dia_fecham_cx")
        self.input_vendas_pix_direto_cpf_dia_fecham_cx.setGeometry(QRect(172, 98, 120, 18))
        sizePolicy2.setHeightForWidth(self.input_vendas_pix_direto_cpf_dia_fecham_cx.sizePolicy().hasHeightForWidth())
        self.input_vendas_pix_direto_cpf_dia_fecham_cx.setSizePolicy(sizePolicy2)
        self.input_vendas_pix_direto_cpf_dia_fecham_cx.setMinimumSize(QSize(120, 0))
        self.input_vendas_pix_direto_cpf_dia_fecham_cx.setMaximumSize(QSize(120, 16777215))
        self.input_vendas_pix_direto_cpf_dia_fecham_cx.setBaseSize(QSize(0, 0))
        self.input_vendas_pix_direto_cpf_dia_fecham_cx.setStyleSheet(u"color: lightblue;\n"
"background-color: #5a7a5a;\n"
"border: solid gray 2px;")
        self.input_vendas_pix_direto_cpf_dia_fecham_cx.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_vendas_pix_direto_cpf_dia_fecham_cx.setReadOnly(True)
        self.btn_ver_entrada_n_operadora = QPushButton(self.groupBox_entradas)
        self.btn_ver_entrada_n_operadora.setObjectName(u"btn_ver_entrada_n_operadora")
        self.btn_ver_entrada_n_operadora.setGeometry(QRect(300, 70, 40, 28))
        self.btn_ver_entrada_n_operadora.setMinimumSize(QSize(40, 28))
        self.btn_ver_entrada_n_operadora.setMaximumSize(QSize(40, 28))
        self.btn_ver_entrada_n_operadora.setStyleSheet(u"QPushButton {\n"
"	font: 350 7pt \"Segoe UI\";\n"
"	background-color: rgb(50,90,50);\n"
"	padding: 2px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        self.groupBox_resultado_caixa = QGroupBox(self.frame_fechamento_caixa)
        self.groupBox_resultado_caixa.setObjectName(u"groupBox_resultado_caixa")
        self.groupBox_resultado_caixa.setGeometry(QRect(580, 440, 111, 121))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_resultado_caixa.sizePolicy().hasHeightForWidth())
        self.groupBox_resultado_caixa.setSizePolicy(sizePolicy3)
        self.groupBox_resultado_caixa.setStyleSheet(u"color: white;")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_resultado_caixa)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.input_resultado_fecham_cx = QLineEdit(self.groupBox_resultado_caixa)
        self.input_resultado_fecham_cx.setObjectName(u"input_resultado_fecham_cx")
        sizePolicy3.setHeightForWidth(self.input_resultado_fecham_cx.sizePolicy().hasHeightForWidth())
        self.input_resultado_fecham_cx.setSizePolicy(sizePolicy3)
        self.input_resultado_fecham_cx.setMinimumSize(QSize(90, 60))
        self.input_resultado_fecham_cx.setMaximumSize(QSize(90, 60))
        self.input_resultado_fecham_cx.setStyleSheet(u"color: lightgreen;\n"
"background-color: #222288;\n"
"border: solid gray 2px;\n"
"font: 700 24pts \"Segoe UI\";")
        self.input_resultado_fecham_cx.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_resultado_fecham_cx.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.input_resultado_fecham_cx)

        self.groupBox_trocas_devolucoes = QGroupBox(self.frame_fechamento_caixa)
        self.groupBox_trocas_devolucoes.setObjectName(u"groupBox_trocas_devolucoes")
        self.groupBox_trocas_devolucoes.setGeometry(QRect(20, 320, 388, 161))
        self.groupBox_trocas_devolucoes.setStyleSheet(u"color: white;")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_trocas_devolucoes)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.label_48 = QLabel(self.groupBox_trocas_devolucoes)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(180, 0))
        self.label_48.setMaximumSize(QSize(180, 16777215))
        self.label_48.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_48)

        self.input_trocas_devolucoes_produtos = QLineEdit(self.groupBox_trocas_devolucoes)
        self.input_trocas_devolucoes_produtos.setObjectName(u"input_trocas_devolucoes_produtos")
        self.input_trocas_devolucoes_produtos.setMinimumSize(QSize(90, 0))
        self.input_trocas_devolucoes_produtos.setMaximumSize(QSize(90, 16777215))
        self.input_trocas_devolucoes_produtos.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_trocas_devolucoes_produtos.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_trocas_devolucoes_produtos.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.input_trocas_devolucoes_produtos)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)

        self.label_49 = QLabel(self.groupBox_trocas_devolucoes)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(180, 0))
        self.label_49.setMaximumSize(QSize(180, 16777215))
        self.label_49.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_49)

        self.input_trocas_devolucoes_dinheiro = QLineEdit(self.groupBox_trocas_devolucoes)
        self.input_trocas_devolucoes_dinheiro.setObjectName(u"input_trocas_devolucoes_dinheiro")
        self.input_trocas_devolucoes_dinheiro.setMinimumSize(QSize(90, 0))
        self.input_trocas_devolucoes_dinheiro.setMaximumSize(QSize(90, 16777215))
        self.input_trocas_devolucoes_dinheiro.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_trocas_devolucoes_dinheiro.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_trocas_devolucoes_dinheiro.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.input_trocas_devolucoes_dinheiro)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_18)


        self.verticalLayout_14.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_19)

        self.label_50 = QLabel(self.groupBox_trocas_devolucoes)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(180, 0))
        self.label_50.setMaximumSize(QSize(180, 16777215))
        self.label_50.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_50)

        self.input_trocas_devolucoes_debito = QLineEdit(self.groupBox_trocas_devolucoes)
        self.input_trocas_devolucoes_debito.setObjectName(u"input_trocas_devolucoes_debito")
        self.input_trocas_devolucoes_debito.setMinimumSize(QSize(90, 0))
        self.input_trocas_devolucoes_debito.setMaximumSize(QSize(90, 16777215))
        self.input_trocas_devolucoes_debito.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_trocas_devolucoes_debito.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_trocas_devolucoes_debito.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.input_trocas_devolucoes_debito)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_20)


        self.verticalLayout_14.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_21)

        self.label_51 = QLabel(self.groupBox_trocas_devolucoes)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(180, 0))
        self.label_51.setMaximumSize(QSize(180, 16777215))
        self.label_51.setStyleSheet(u"font: 550 8pt \"Segoe UI\";\n"
"color: white;")
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_51)

        self.input_trocas_devolucoes_credito = QLineEdit(self.groupBox_trocas_devolucoes)
        self.input_trocas_devolucoes_credito.setObjectName(u"input_trocas_devolucoes_credito")
        self.input_trocas_devolucoes_credito.setMinimumSize(QSize(90, 0))
        self.input_trocas_devolucoes_credito.setMaximumSize(QSize(90, 16777215))
        self.input_trocas_devolucoes_credito.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_trocas_devolucoes_credito.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_trocas_devolucoes_credito.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.input_trocas_devolucoes_credito)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_22)


        self.verticalLayout_14.addLayout(self.horizontalLayout_17)

        self.btn_ver_trocas_dev = QPushButton(self.groupBox_trocas_devolucoes)
        self.btn_ver_trocas_dev.setObjectName(u"btn_ver_trocas_dev")
        self.btn_ver_trocas_dev.setStyleSheet(u"QPushButton {\n"
"	font: 350 7pt \"Segoe UI\";\n"
"	background-color: rgb(50,90,50);\n"
"	padding: 2px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.verticalLayout_14.addWidget(self.btn_ver_trocas_dev)

        self.btn_apurar_resultado_caixa = QPushButton(self.frame_fechamento_caixa)
        self.btn_apurar_resultado_caixa.setObjectName(u"btn_apurar_resultado_caixa")
        self.btn_apurar_resultado_caixa.setGeometry(QRect(440, 130, 251, 31))
        self.btn_apurar_resultado_caixa.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(75,51,60);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        self.btn_enviar_fechamento_caixa = QPushButton(self.frame_fechamento_caixa)
        self.btn_enviar_fechamento_caixa.setObjectName(u"btn_enviar_fechamento_caixa")
        self.btn_enviar_fechamento_caixa.setGeometry(QRect(440, 250, 251, 31))
        self.btn_enviar_fechamento_caixa.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50,50,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        self.btn_enviar_fechamento_parcial_caixa = QPushButton(self.frame_fechamento_caixa)
        self.btn_enviar_fechamento_parcial_caixa.setObjectName(u"btn_enviar_fechamento_parcial_caixa")
        self.btn_enviar_fechamento_parcial_caixa.setGeometry(QRect(440, 210, 251, 31))
        self.btn_enviar_fechamento_parcial_caixa.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50,50,50);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        self.btn_caixa_visto = QPushButton(self.frame_fechamento_caixa)
        self.btn_caixa_visto.setObjectName(u"btn_caixa_visto")
        self.btn_caixa_visto.setGeometry(QRect(440, 170, 251, 31))
        self.btn_caixa_visto.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50,71,50);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        self.groupBox_fechamentos_parciais = QGroupBox(self.frame_fechamento_caixa)
        self.groupBox_fechamentos_parciais.setObjectName(u"groupBox_fechamentos_parciais")
        self.groupBox_fechamentos_parciais.setGeometry(QRect(440, 360, 251, 71))
        self.groupBox_fechamentos_parciais.setStyleSheet(u"color: white;")
        self.btn_ver_fechamentos_parciais = QPushButton(self.groupBox_fechamentos_parciais)
        self.btn_ver_fechamentos_parciais.setObjectName(u"btn_ver_fechamentos_parciais")
        self.btn_ver_fechamentos_parciais.setGeometry(QRect(200, 20, 40, 28))
        self.btn_ver_fechamentos_parciais.setMinimumSize(QSize(40, 28))
        self.btn_ver_fechamentos_parciais.setMaximumSize(QSize(40, 28))
        self.btn_ver_fechamentos_parciais.setStyleSheet(u"QPushButton {\n"
"	font: 350 7pt \"Segoe UI\";\n"
"	background-color: rgb(50,90,50);\n"
"	padding: 2px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        self.label_fecham_parc_cx = QLabel(self.groupBox_fechamentos_parciais)
        self.label_fecham_parc_cx.setObjectName(u"label_fecham_parc_cx")
        self.label_fecham_parc_cx.setGeometry(QRect(10, 40, 171, 20))
        self.groupBox_2 = QGroupBox(self.frame_fechamento_caixa)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(430, 500, 141, 61))
        self.groupBox_2.setStyleSheet(u"color: white;")
        self.input_user_name = QLineEdit(self.groupBox_2)
        self.input_user_name.setObjectName(u"input_user_name")
        self.input_user_name.setGeometry(QRect(10, 30, 121, 22))
        self.input_user_name.setStyleSheet(u"font: 500 8pt \"Segoe UI\";\n"
"color: blue;\n"
"background-color: white;")
        self.input_user_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_user_name.setReadOnly(True)
        self.groupBox_observacoes = QGroupBox(self.frame_fechamento_caixa)
        self.groupBox_observacoes.setObjectName(u"groupBox_observacoes")
        self.groupBox_observacoes.setGeometry(QRect(440, 290, 251, 51))
        self.groupBox_observacoes.setStyleSheet(u"color: white;")
        self.btn_ver_observacoes = QPushButton(self.groupBox_observacoes)
        self.btn_ver_observacoes.setObjectName(u"btn_ver_observacoes")
        self.btn_ver_observacoes.setGeometry(QRect(200, 10, 40, 28))
        self.btn_ver_observacoes.setMinimumSize(QSize(40, 28))
        self.btn_ver_observacoes.setMaximumSize(QSize(40, 28))
        self.btn_ver_observacoes.setStyleSheet(u"QPushButton {\n"
"	font: 350 7pt \"Segoe UI\";\n"
"	background-color: rgb(50,90,50);\n"
"	padding: 2px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        self.label_observacoes = QLabel(self.groupBox_observacoes)
        self.label_observacoes.setObjectName(u"label_observacoes")
        self.label_observacoes.setGeometry(QRect(10, 30, 151, 20))
        self.btn_atualizar_vendas = QPushButton(self.frame_fechamento_caixa)
        self.btn_atualizar_vendas.setObjectName(u"btn_atualizar_vendas")
        self.btn_atualizar_vendas.setGeometry(QRect(570, 100, 120, 28))
        self.btn_atualizar_vendas.setMinimumSize(QSize(120, 28))
        self.btn_atualizar_vendas.setMaximumSize(QSize(120, 28))
        self.btn_atualizar_vendas.setStyleSheet(u"QPushButton {\n"
"	font: 350 7pt \"Segoe UI\";\n"
"	background-color: rgb(90,90,90);\n"
"	padding: 2px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        application_pages.addWidget(self.fecham_cx)
        self.page_fechamentos_parciais_cx = QWidget()
        self.page_fechamentos_parciais_cx.setObjectName(u"page_fechamentos_parciais_cx")
        self.frame_6 = QFrame(self.page_fechamentos_parciais_cx)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(6, 343, 821, 331))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_46 = QLabel(self.page_fechamentos_parciais_cx)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(20, 0, 243, 22))
        self.label_46.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.tableView_fecham_parciais = QTableView(self.page_fechamentos_parciais_cx)
        self.tableView_fecham_parciais.setObjectName(u"tableView_fecham_parciais")
        self.tableView_fecham_parciais.setGeometry(QRect(20, 30, 600, 240))
        self.tableView_fecham_parciais.setMinimumSize(QSize(600, 240))
        self.tableView_fecham_parciais.setMaximumSize(QSize(600, 240))
        self.tableView_fecham_parciais.setStyleSheet(u"QTableView {\n"
"	alternate-background-color: #f8f9fa;\n"
"	background-color: white;\n"
"	gridline-color: #dee2e6;\n"
"	font: 550 9pt \"Segoe UI\";\n"
"	color: blue;\n"
"}\n"
"\n"
"QTableView::item {\n"
"	padding: 5px;\n"
"	border-bottom: 1px solid #dee2e6;\n"
"	font: 550 9pt \"Segoe UI\";\n"
"	color: blue;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"	background-color: #007bff;\n"
"	color: white;\n"
"	font: 550 9pt \"Segoe UI\";\n"
"	color: blue;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: #6c757d;\n"
"	font: 550 9pt \"Segoe UI\";\n"
"	color: orange;\n"
"	padding: 5px;\n"
"	border: 1px solid #5a6268;\n"
"	font-weight: bold;\n"
"}")
        application_pages.addWidget(self.page_fechamentos_parciais_cx)
        self.visualizacao_fechamento_parcial = QWidget()
        self.visualizacao_fechamento_parcial.setObjectName(u"visualizacao_fechamento_parcial")
        self.frame_fechamento_caixa_parc = QFrame(self.visualizacao_fechamento_parcial)
        self.frame_fechamento_caixa_parc.setObjectName(u"frame_fechamento_caixa_parc")
        self.frame_fechamento_caixa_parc.setGeometry(QRect(10, 10, 720, 580))
        self.frame_fechamento_caixa_parc.setMinimumSize(QSize(720, 580))
        self.frame_fechamento_caixa_parc.setMaximumSize(QSize(720, 580))
        self.frame_fechamento_caixa_parc.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fechamento_caixa_parc.setFrameShadow(QFrame.Shadow.Raised)
        self.groupBox_3 = QGroupBox(self.frame_fechamento_caixa_parc)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(440, 10, 248, 83))
        self.groupBox_3.setStyleSheet(u"color: white;")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_53 = QLabel(self.groupBox_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_3.addWidget(self.label_53)

        self.data_cx_fechamento_cx_parc = QDateEdit(self.groupBox_3)
        self.data_cx_fechamento_cx_parc.setObjectName(u"data_cx_fechamento_cx_parc")
        self.data_cx_fechamento_cx_parc.setMinimumSize(QSize(120, 0))
        self.data_cx_fechamento_cx_parc.setMaximumSize(QSize(120, 16777215))
        self.data_cx_fechamento_cx_parc.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(0,0,0);")
        self.data_cx_fechamento_cx_parc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_cx_fechamento_cx_parc.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.data_cx_fechamento_cx_parc)


        self.verticalLayout_17.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_54 = QLabel(self.groupBox_3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")

        self.horizontalLayout_18.addWidget(self.label_54)

        self.vendas_lida_dia_fecham_cx_parc = QLineEdit(self.groupBox_3)
        self.vendas_lida_dia_fecham_cx_parc.setObjectName(u"vendas_lida_dia_fecham_cx_parc")
        self.vendas_lida_dia_fecham_cx_parc.setMinimumSize(QSize(120, 0))
        self.vendas_lida_dia_fecham_cx_parc.setMaximumSize(QSize(120, 16777215))
        self.vendas_lida_dia_fecham_cx_parc.setStyleSheet(u"color: lightblue;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.vendas_lida_dia_fecham_cx_parc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vendas_lida_dia_fecham_cx_parc.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.vendas_lida_dia_fecham_cx_parc)


        self.verticalLayout_17.addLayout(self.horizontalLayout_18)

        self.groupBox_despesas_cx_parc = QGroupBox(self.frame_fechamento_caixa_parc)
        self.groupBox_despesas_cx_parc.setObjectName(u"groupBox_despesas_cx_parc")
        self.groupBox_despesas_cx_parc.setGeometry(QRect(20, 490, 381, 71))
        self.groupBox_despesas_cx_parc.setStyleSheet(u"color: white;")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_despesas_cx_parc)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_23)

        self.label_55 = QLabel(self.groupBox_despesas_cx_parc)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")

        self.horizontalLayout_19.addWidget(self.label_55)

        self.input_total_despesas_caixa_fecham_cx_parc = QLineEdit(self.groupBox_despesas_cx_parc)
        self.input_total_despesas_caixa_fecham_cx_parc.setObjectName(u"input_total_despesas_caixa_fecham_cx_parc")
        self.input_total_despesas_caixa_fecham_cx_parc.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_total_despesas_caixa_fecham_cx_parc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_total_despesas_caixa_fecham_cx_parc.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.input_total_despesas_caixa_fecham_cx_parc)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_24)


        self.verticalLayout_18.addLayout(self.horizontalLayout_19)

        self.groupBox_troco_parc = QGroupBox(self.frame_fechamento_caixa_parc)
        self.groupBox_troco_parc.setObjectName(u"groupBox_troco_parc")
        self.groupBox_troco_parc.setGeometry(QRect(20, 130, 311, 181))
        self.groupBox_troco_parc.setStyleSheet(u"color: white;")
        self.input_troco_fecham_cx_2 = QLineEdit(self.groupBox_troco_parc)
        self.input_troco_fecham_cx_2.setObjectName(u"input_troco_fecham_cx_2")
        self.input_troco_fecham_cx_2.setGeometry(QRect(170, 30, 120, 22))
        self.input_troco_fecham_cx_2.setMinimumSize(QSize(120, 0))
        self.input_troco_fecham_cx_2.setMaximumSize(QSize(120, 16777215))
        self.input_troco_fecham_cx_2.setStyleSheet(u"color: white;\n"
"background-color: #5a5a5a;\n"
"border: solid gray 2px;")
        self.input_troco_fecham_cx_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_56 = QLabel(self.groupBox_troco_parc)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(10, 30, 151, 16))
        self.label_56.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")
        self.label_56.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_estoque_troco_fecham_cx_2 = QLineEdit(self.groupBox_troco_parc)
        self.input_estoque_troco_fecham_cx_2.setObjectName(u"input_estoque_troco_fecham_cx_2")
        self.input_estoque_troco_fecham_cx_2.setGeometry(QRect(170, 90, 120, 22))
        self.input_estoque_troco_fecham_cx_2.setMinimumSize(QSize(120, 0))
        self.input_estoque_troco_fecham_cx_2.setMaximumSize(QSize(120, 16777215))
        self.input_estoque_troco_fecham_cx_2.setStyleSheet(u"color: white;\n"
"background-color: #5a5a5a;\n"
"border: solid gray 2px;")
        self.input_estoque_troco_fecham_cx_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_57 = QLabel(self.groupBox_troco_parc)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(10, 90, 151, 16))
        self.label_57.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")
        self.label_57.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_58 = QLabel(self.groupBox_troco_parc)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(10, 60, 151, 16))
        self.label_58.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")
        self.label_58.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_troco_fecham_cx_anterior_2 = QLineEdit(self.groupBox_troco_parc)
        self.input_troco_fecham_cx_anterior_2.setObjectName(u"input_troco_fecham_cx_anterior_2")
        self.input_troco_fecham_cx_anterior_2.setGeometry(QRect(170, 60, 120, 22))
        self.input_troco_fecham_cx_anterior_2.setMinimumSize(QSize(120, 0))
        self.input_troco_fecham_cx_anterior_2.setMaximumSize(QSize(120, 16777215))
        self.input_troco_fecham_cx_anterior_2.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_troco_fecham_cx_anterior_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_troco_fecham_cx_anterior_2.setReadOnly(True)
        self.label_59 = QLabel(self.groupBox_troco_parc)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(10, 120, 151, 16))
        self.label_59.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")
        self.label_59.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_est_troco_fecham_cx_ant_2 = QLineEdit(self.groupBox_troco_parc)
        self.input_est_troco_fecham_cx_ant_2.setObjectName(u"input_est_troco_fecham_cx_ant_2")
        self.input_est_troco_fecham_cx_ant_2.setGeometry(QRect(170, 120, 120, 22))
        self.input_est_troco_fecham_cx_ant_2.setMinimumSize(QSize(120, 0))
        self.input_est_troco_fecham_cx_ant_2.setMaximumSize(QSize(120, 16777215))
        self.input_est_troco_fecham_cx_ant_2.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_est_troco_fecham_cx_ant_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_est_troco_fecham_cx_ant_2.setReadOnly(True)
        self.label_60 = QLabel(self.groupBox_troco_parc)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(10, 150, 151, 16))
        self.label_60.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")
        self.label_60.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.result_troco_fechamento_cx_2 = QLineEdit(self.groupBox_troco_parc)
        self.result_troco_fechamento_cx_2.setObjectName(u"result_troco_fechamento_cx_2")
        self.result_troco_fechamento_cx_2.setGeometry(QRect(170, 150, 120, 22))
        self.result_troco_fechamento_cx_2.setMinimumSize(QSize(120, 0))
        self.result_troco_fechamento_cx_2.setMaximumSize(QSize(120, 16777215))
        self.result_troco_fechamento_cx_2.setStyleSheet(u"color: white;\n"
"background-color: #884444;\n"
"border: solid gray 2px;")
        self.result_troco_fechamento_cx_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_troco_fechamento_cx_2.setReadOnly(True)
        self.groupBox_entradas_parc = QGroupBox(self.frame_fechamento_caixa_parc)
        self.groupBox_entradas_parc.setObjectName(u"groupBox_entradas_parc")
        self.groupBox_entradas_parc.setGeometry(QRect(20, 10, 311, 121))
        self.groupBox_entradas_parc.setStyleSheet(u"color: white;")
        self.label_61 = QLabel(self.groupBox_entradas_parc)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(11, 27, 143, 16))
        self.label_62 = QLabel(self.groupBox_entradas_parc)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(11, 50, 143, 16))
        sizePolicy1.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy1)
        self.label_62.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_vendas_dinheiro_dia_fecham_cx_parc = QLineEdit(self.groupBox_entradas_parc)
        self.input_vendas_dinheiro_dia_fecham_cx_parc.setObjectName(u"input_vendas_dinheiro_dia_fecham_cx_parc")
        self.input_vendas_dinheiro_dia_fecham_cx_parc.setGeometry(QRect(160, 50, 120, 16))
        sizePolicy2.setHeightForWidth(self.input_vendas_dinheiro_dia_fecham_cx_parc.sizePolicy().hasHeightForWidth())
        self.input_vendas_dinheiro_dia_fecham_cx_parc.setSizePolicy(sizePolicy2)
        self.input_vendas_dinheiro_dia_fecham_cx_parc.setMinimumSize(QSize(120, 0))
        self.input_vendas_dinheiro_dia_fecham_cx_parc.setMaximumSize(QSize(120, 16777215))
        self.input_vendas_dinheiro_dia_fecham_cx_parc.setStyleSheet(u"color: lightblue;\n"
"background-color: #5a5a5a;\n"
"border: solid gray 2px;")
        self.input_vendas_dinheiro_dia_fecham_cx_parc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_63 = QLabel(self.groupBox_entradas_parc)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(48, 70, 101, 20))
        sizePolicy1.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy1)
        self.label_63.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_vendas_pix_direto_dia_fecham_cx_parc = QLineEdit(self.groupBox_entradas_parc)
        self.input_vendas_pix_direto_dia_fecham_cx_parc.setObjectName(u"input_vendas_pix_direto_dia_fecham_cx_parc")
        self.input_vendas_pix_direto_dia_fecham_cx_parc.setGeometry(QRect(160, 70, 120, 17))
        sizePolicy2.setHeightForWidth(self.input_vendas_pix_direto_dia_fecham_cx_parc.sizePolicy().hasHeightForWidth())
        self.input_vendas_pix_direto_dia_fecham_cx_parc.setSizePolicy(sizePolicy2)
        self.input_vendas_pix_direto_dia_fecham_cx_parc.setMinimumSize(QSize(120, 0))
        self.input_vendas_pix_direto_dia_fecham_cx_parc.setMaximumSize(QSize(120, 16777215))
        self.input_vendas_pix_direto_dia_fecham_cx_parc.setBaseSize(QSize(0, 0))
        self.input_vendas_pix_direto_dia_fecham_cx_parc.setStyleSheet(u"color: lightblue;\n"
"background-color: #5a5a5a;\n"
"border: solid gray 2px;")
        self.input_vendas_pix_direto_dia_fecham_cx_parc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_total_maq_cartoes_fecham_cx_parc = QLineEdit(self.groupBox_entradas_parc)
        self.input_total_maq_cartoes_fecham_cx_parc.setObjectName(u"input_total_maq_cartoes_fecham_cx_parc")
        self.input_total_maq_cartoes_fecham_cx_parc.setGeometry(QRect(160, 27, 120, 18))
        self.input_total_maq_cartoes_fecham_cx_parc.setMinimumSize(QSize(120, 0))
        self.input_total_maq_cartoes_fecham_cx_parc.setMaximumSize(QSize(120, 16777215))
        self.input_total_maq_cartoes_fecham_cx_parc.setStyleSheet(u"color: lightblue;\n"
"background-color: #5a5a5a;\n"
"border: solid gray 2px;")
        self.input_total_maq_cartoes_fecham_cx_parc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_resultado_caixa_2 = QGroupBox(self.frame_fechamento_caixa_parc)
        self.groupBox_resultado_caixa_2.setObjectName(u"groupBox_resultado_caixa_2")
        self.groupBox_resultado_caixa_2.setGeometry(QRect(600, 440, 111, 121))
        sizePolicy3.setHeightForWidth(self.groupBox_resultado_caixa_2.sizePolicy().hasHeightForWidth())
        self.groupBox_resultado_caixa_2.setSizePolicy(sizePolicy3)
        self.groupBox_resultado_caixa_2.setStyleSheet(u"color: white;")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_resultado_caixa_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_64 = QLabel(self.groupBox_resultado_caixa_2)
        self.label_64.setObjectName(u"label_64")
        sizePolicy.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy)

        self.verticalLayout_19.addWidget(self.label_64)

        self.input_resultado_fecham_cx_parc = QLineEdit(self.groupBox_resultado_caixa_2)
        self.input_resultado_fecham_cx_parc.setObjectName(u"input_resultado_fecham_cx_parc")
        sizePolicy3.setHeightForWidth(self.input_resultado_fecham_cx_parc.sizePolicy().hasHeightForWidth())
        self.input_resultado_fecham_cx_parc.setSizePolicy(sizePolicy3)
        self.input_resultado_fecham_cx_parc.setMinimumSize(QSize(90, 60))
        self.input_resultado_fecham_cx_parc.setMaximumSize(QSize(90, 60))
        self.input_resultado_fecham_cx_parc.setStyleSheet(u"color: lightgreen;\n"
"background-color: #222288;\n"
"border: solid gray 2px;\n"
"font: 700 24pts \"Segoe UI\";")
        self.input_resultado_fecham_cx_parc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_resultado_fecham_cx_parc.setReadOnly(True)

        self.verticalLayout_19.addWidget(self.input_resultado_fecham_cx_parc)

        self.groupBox_trocas_devolucoes_parc = QGroupBox(self.frame_fechamento_caixa_parc)
        self.groupBox_trocas_devolucoes_parc.setObjectName(u"groupBox_trocas_devolucoes_parc")
        self.groupBox_trocas_devolucoes_parc.setGeometry(QRect(20, 320, 388, 142))
        self.groupBox_trocas_devolucoes_parc.setStyleSheet(u"color: white;")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_trocas_devolucoes_parc)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_25)

        self.label_65 = QLabel(self.groupBox_trocas_devolucoes_parc)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(180, 0))
        self.label_65.setMaximumSize(QSize(180, 16777215))
        self.label_65.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")
        self.label_65.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_65)

        self.input_trocas_devolucoes_produtos_parc = QLineEdit(self.groupBox_trocas_devolucoes_parc)
        self.input_trocas_devolucoes_produtos_parc.setObjectName(u"input_trocas_devolucoes_produtos_parc")
        self.input_trocas_devolucoes_produtos_parc.setMinimumSize(QSize(90, 0))
        self.input_trocas_devolucoes_produtos_parc.setMaximumSize(QSize(90, 16777215))
        self.input_trocas_devolucoes_produtos_parc.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_trocas_devolucoes_produtos_parc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_trocas_devolucoes_produtos_parc.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.input_trocas_devolucoes_produtos_parc)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_26)


        self.verticalLayout_20.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_27)

        self.label_66 = QLabel(self.groupBox_trocas_devolucoes_parc)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(180, 0))
        self.label_66.setMaximumSize(QSize(180, 16777215))
        self.label_66.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")
        self.label_66.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_66)

        self.input_trocas_devolucoes_dinheiro_parc = QLineEdit(self.groupBox_trocas_devolucoes_parc)
        self.input_trocas_devolucoes_dinheiro_parc.setObjectName(u"input_trocas_devolucoes_dinheiro_parc")
        self.input_trocas_devolucoes_dinheiro_parc.setMinimumSize(QSize(90, 0))
        self.input_trocas_devolucoes_dinheiro_parc.setMaximumSize(QSize(90, 16777215))
        self.input_trocas_devolucoes_dinheiro_parc.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_trocas_devolucoes_dinheiro_parc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_trocas_devolucoes_dinheiro_parc.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.input_trocas_devolucoes_dinheiro_parc)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_28)


        self.verticalLayout_20.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_29)

        self.label_67 = QLabel(self.groupBox_trocas_devolucoes_parc)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(180, 0))
        self.label_67.setMaximumSize(QSize(180, 16777215))
        self.label_67.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")
        self.label_67.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_67)

        self.input_trocas_devolucoes_debito_parc = QLineEdit(self.groupBox_trocas_devolucoes_parc)
        self.input_trocas_devolucoes_debito_parc.setObjectName(u"input_trocas_devolucoes_debito_parc")
        self.input_trocas_devolucoes_debito_parc.setMinimumSize(QSize(90, 0))
        self.input_trocas_devolucoes_debito_parc.setMaximumSize(QSize(90, 16777215))
        self.input_trocas_devolucoes_debito_parc.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_trocas_devolucoes_debito_parc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_trocas_devolucoes_debito_parc.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.input_trocas_devolucoes_debito_parc)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_30)


        self.verticalLayout_20.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_31)

        self.label_68 = QLabel(self.groupBox_trocas_devolucoes_parc)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(180, 0))
        self.label_68.setMaximumSize(QSize(180, 16777215))
        self.label_68.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: white;")
        self.label_68.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_68)

        self.input_trocas_devolucoes_credito_parc = QLineEdit(self.groupBox_trocas_devolucoes_parc)
        self.input_trocas_devolucoes_credito_parc.setObjectName(u"input_trocas_devolucoes_credito_parc")
        self.input_trocas_devolucoes_credito_parc.setMinimumSize(QSize(90, 0))
        self.input_trocas_devolucoes_credito_parc.setMaximumSize(QSize(90, 16777215))
        self.input_trocas_devolucoes_credito_parc.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_trocas_devolucoes_credito_parc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_trocas_devolucoes_credito_parc.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.input_trocas_devolucoes_credito_parc)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_32)


        self.verticalLayout_20.addLayout(self.horizontalLayout_23)

        self.btn_caixa_visto_parc = QPushButton(self.frame_fechamento_caixa_parc)
        self.btn_caixa_visto_parc.setObjectName(u"btn_caixa_visto_parc")
        self.btn_caixa_visto_parc.setGeometry(QRect(440, 160, 251, 31))
        self.btn_caixa_visto_parc.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50,71,50);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        self.groupBox_usuario_parc = QGroupBox(self.frame_fechamento_caixa_parc)
        self.groupBox_usuario_parc.setObjectName(u"groupBox_usuario_parc")
        self.groupBox_usuario_parc.setGeometry(QRect(450, 500, 111, 61))
        self.input_user_name_parc = QLineEdit(self.groupBox_usuario_parc)
        self.input_user_name_parc.setObjectName(u"input_user_name_parc")
        self.input_user_name_parc.setGeometry(QRect(10, 30, 91, 22))
        self.input_user_name_parc.setStyleSheet(u"color: blue;\n"
"background-color: white;")
        self.input_user_name_parc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_user_name_parc.setReadOnly(True)
        application_pages.addWidget(self.visualizacao_fechamento_parcial)
        self.inserir_despesas_cx = QWidget()
        self.inserir_despesas_cx.setObjectName(u"inserir_despesas_cx")
        self.verticalLayout_9 = QVBoxLayout(self.inserir_despesas_cx)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_13)

        self.label_52 = QLabel(self.inserir_despesas_cx)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")

        self.verticalLayout_9.addWidget(self.label_52, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_14)

        self.frame_4 = QFrame(self.inserir_despesas_cx)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(600, 300))
        self.frame_4.setMaximumSize(QSize(600, 300))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_enviar_despesa_caixa = QPushButton(self.frame_4)
        self.btn_enviar_despesa_caixa.setObjectName(u"btn_enviar_despesa_caixa")
        self.btn_enviar_despesa_caixa.setGeometry(QRect(40, 230, 491, 41))
        self.btn_enviar_despesa_caixa.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68,71,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(40, 190, 101, 20))
        self.label_22.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 70, 121, 20))
        self.label_20.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(60, 10, 81, 20))
        self.label_19.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.valor_despesa_input = QLineEdit(self.frame_4)
        self.valor_despesa_input.setObjectName(u"valor_despesa_input")
        self.valor_despesa_input.setGeometry(QRect(150, 190, 141, 31))
        self.valor_despesa_input.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.descricao_despesa_input = QTextBrowser(self.frame_4)
        self.descricao_despesa_input.setObjectName(u"descricao_despesa_input")
        self.descricao_despesa_input.setGeometry(QRect(150, 70, 381, 111))
        self.descricao_despesa_input.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 1px;\n"
"border-radius: 10px;")
        self.descricao_despesa_input.setReadOnly(False)
        self.despesa_id_comboBox = QComboBox(self.frame_4)
        self.despesa_id_comboBox.setObjectName(u"despesa_id_comboBox")
        self.despesa_id_comboBox.setGeometry(QRect(150, 40, 281, 22))
        self.despesa_id_comboBox.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 1px;")
        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(70, 40, 71, 20))
        self.label_21.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.data_inserir_despesa = QDateEdit(self.frame_4)
        self.data_inserir_despesa.setObjectName(u"data_inserir_despesa")
        self.data_inserir_despesa.setGeometry(QRect(150, 10, 120, 22))
        self.data_inserir_despesa.setMinimumSize(QSize(120, 0))
        self.data_inserir_despesa.setMaximumSize(QSize(120, 16777215))
        self.data_inserir_despesa.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(0,0,0);")
        self.data_inserir_despesa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_inserir_despesa.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_15)

        application_pages.addWidget(self.inserir_despesas_cx)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.verticalLayout_3 = QVBoxLayout(self.login)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.login)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(320, 400))
        self.frame.setMaximumSize(QSize(320, 400))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_login = QLabel(self.frame)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")

        self.verticalLayout_2.addWidget(self.label_login)

        self.input_user_code = QLineEdit(self.frame)
        self.input_user_code.setObjectName(u"input_user_code")
        sizePolicy2.setHeightForWidth(self.input_user_code.sizePolicy().hasHeightForWidth())
        self.input_user_code.setSizePolicy(sizePolicy2)
        self.input_user_code.setMinimumSize(QSize(300, 0))
        self.input_user_code.setMaximumSize(QSize(300, 16777215))
        self.input_user_code.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(68,71,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}")
        self.input_user_code.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.input_user_code)

        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(300, 0))
        self.btn_login.setMaximumSize(QSize(300, 16777215))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68,71,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_login)

        self.lbl_ola = QLabel(self.frame)
        self.lbl_ola.setObjectName(u"lbl_ola")
        self.lbl_ola.setEnabled(False)
        self.lbl_ola.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.lbl_ola.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_ola)

        self.nome_usuario_login = QLabel(self.frame)
        self.nome_usuario_login.setObjectName(u"nome_usuario_login")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.nome_usuario_login.sizePolicy().hasHeightForWidth())
        self.nome_usuario_login.setSizePolicy(sizePolicy4)
        self.nome_usuario_login.setMinimumSize(QSize(240, 0))
        self.nome_usuario_login.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.nome_usuario_login.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.nome_usuario_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.nome_usuario_login, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_18)

        self.btn_selection_date = QPushButton(self.frame)
        self.btn_selection_date.setObjectName(u"btn_selection_date")
        self.btn_selection_date.setMinimumSize(QSize(300, 0))
        self.btn_selection_date.setMaximumSize(QSize(300, 16777215))
        self.btn_selection_date.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68,71,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_selection_date)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        application_pages.addWidget(self.login)
        self.trocas_devolucoes = QWidget()
        self.trocas_devolucoes.setObjectName(u"trocas_devolucoes")
        self.frame_trocas_devolucoes = QFrame(self.trocas_devolucoes)
        self.frame_trocas_devolucoes.setObjectName(u"frame_trocas_devolucoes")
        self.frame_trocas_devolucoes.setGeometry(QRect(57, 25, 680, 540))
        self.frame_trocas_devolucoes.setMinimumSize(QSize(680, 540))
        self.frame_trocas_devolucoes.setMaximumSize(QSize(680, 540))
        self.frame_trocas_devolucoes.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_trocas_devolucoes.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_trocas_devolucoes)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_32 = QLabel(self.frame_trocas_devolucoes)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_32)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_27 = QLabel(self.frame_trocas_devolucoes)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(175, 0))
        self.label_27.setMaximumSize(QSize(175, 16777215))
        self.label_27.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_27)

        self.data_cx_trocas_devolucoes = QDateEdit(self.frame_trocas_devolucoes)
        self.data_cx_trocas_devolucoes.setObjectName(u"data_cx_trocas_devolucoes")
        self.data_cx_trocas_devolucoes.setEnabled(True)
        sizePolicy.setHeightForWidth(self.data_cx_trocas_devolucoes.sizePolicy().hasHeightForWidth())
        self.data_cx_trocas_devolucoes.setSizePolicy(sizePolicy)
        self.data_cx_trocas_devolucoes.setMinimumSize(QSize(120, 0))
        self.data_cx_trocas_devolucoes.setMaximumSize(QSize(120, 16777215))
        self.data_cx_trocas_devolucoes.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(0,0,0);")
        self.data_cx_trocas_devolucoes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_cx_trocas_devolucoes.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.data_cx_trocas_devolucoes)


        self.verticalLayout_15.addLayout(self.horizontalLayout_9)

        self.tableView_troca_devolucoes_cx = QTableView(self.frame_trocas_devolucoes)
        self.tableView_troca_devolucoes_cx.setObjectName(u"tableView_troca_devolucoes_cx")
        self.tableView_troca_devolucoes_cx.setStyleSheet(u"QTableView {\n"
"	alternate-background-color: #f8f9fa;\n"
"	background-color: white;\n"
"	gridline-color: #dee2e6;\n"
"   color: black;\n"
"}\n"
"\n"
"QTableView::item {\n"
"	padding: 5px;\n"
"	border-bottom: 1px solid #dee2e6;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"	background-color: #007bff;\n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: #6c757d;\n"
"	color: white;\n"
"	padding: 5px;\n"
"	border: 1px solid #5a6268;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_15.addWidget(self.tableView_troca_devolucoes_cx)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_27)

        self.label_79 = QLabel(self.frame_trocas_devolucoes)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(190,190,255);")

        self.verticalLayout_15.addWidget(self.label_79)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_39)

        self.label_77 = QLabel(self.frame_trocas_devolucoes)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_10.addWidget(self.label_77)

        self.combo_entrada_troca_dev = QComboBox(self.frame_trocas_devolucoes)
        self.combo_entrada_troca_dev.setObjectName(u"combo_entrada_troca_dev")
        self.combo_entrada_troca_dev.setMinimumSize(QSize(90, 0))
        self.combo_entrada_troca_dev.setMaximumSize(QSize(90, 16777215))
        self.combo_entrada_troca_dev.setStyleSheet(u"color: white;\n"
"background-color: black;")

        self.horizontalLayout_10.addWidget(self.combo_entrada_troca_dev)

        self.label_41 = QLabel(self.frame_trocas_devolucoes)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(45, 0))
        self.label_41.setMaximumSize(QSize(45, 16777215))
        self.label_41.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_41)

        self.input_valor_entrada_troca_devol = QLineEdit(self.frame_trocas_devolucoes)
        self.input_valor_entrada_troca_devol.setObjectName(u"input_valor_entrada_troca_devol")
        self.input_valor_entrada_troca_devol.setMinimumSize(QSize(60, 0))
        self.input_valor_entrada_troca_devol.setMaximumSize(QSize(60, 16777215))
        self.input_valor_entrada_troca_devol.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")

        self.horizontalLayout_10.addWidget(self.input_valor_entrada_troca_devol)

        self.label_33 = QLabel(self.frame_trocas_devolucoes)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(60, 0))
        self.label_33.setMaximumSize(QSize(60, 16777215))
        self.label_33.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_10.addWidget(self.label_33)

        self.input_descricao_entrada_troca_devol = QLineEdit(self.frame_trocas_devolucoes)
        self.input_descricao_entrada_troca_devol.setObjectName(u"input_descricao_entrada_troca_devol")
        self.input_descricao_entrada_troca_devol.setMinimumSize(QSize(90, 0))
        self.input_descricao_entrada_troca_devol.setMaximumSize(QSize(90, 16777215))
        self.input_descricao_entrada_troca_devol.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")

        self.horizontalLayout_10.addWidget(self.input_descricao_entrada_troca_devol)

        self.btn_inserir_entrada_troca_dev = QPushButton(self.frame_trocas_devolucoes)
        self.btn_inserir_entrada_troca_dev.setObjectName(u"btn_inserir_entrada_troca_dev")
        self.btn_inserir_entrada_troca_dev.setMinimumSize(QSize(120, 0))
        self.btn_inserir_entrada_troca_dev.setMaximumSize(QSize(120, 16777215))
        self.btn_inserir_entrada_troca_dev.setBaseSize(QSize(90, 0))
        self.btn_inserir_entrada_troca_dev.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50,50,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_inserir_entrada_troca_dev)

        self.checkBox_relevancia_entrada_cx = QCheckBox(self.frame_trocas_devolucoes)
        self.checkBox_relevancia_entrada_cx.setObjectName(u"checkBox_relevancia_entrada_cx")
        self.checkBox_relevancia_entrada_cx.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_10.addWidget(self.checkBox_relevancia_entrada_cx)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_40)


        self.verticalLayout_15.addLayout(self.horizontalLayout_10)

        self.label_80 = QLabel(self.frame_trocas_devolucoes)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,190,190);")

        self.verticalLayout_15.addWidget(self.label_80)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_41)

        self.label_78 = QLabel(self.frame_trocas_devolucoes)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_11.addWidget(self.label_78)

        self.combo_saida_troca_dev = QComboBox(self.frame_trocas_devolucoes)
        self.combo_saida_troca_dev.setObjectName(u"combo_saida_troca_dev")
        self.combo_saida_troca_dev.setMinimumSize(QSize(90, 0))
        self.combo_saida_troca_dev.setMaximumSize(QSize(90, 16777215))
        self.combo_saida_troca_dev.setStyleSheet(u"color: white;\n"
"background-color: black;")

        self.horizontalLayout_11.addWidget(self.combo_saida_troca_dev)

        self.label_43 = QLabel(self.frame_trocas_devolucoes)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(45, 0))
        self.label_43.setMaximumSize(QSize(45, 16777215))
        self.label_43.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_43)

        self.input_valor_saida_troca_devol = QLineEdit(self.frame_trocas_devolucoes)
        self.input_valor_saida_troca_devol.setObjectName(u"input_valor_saida_troca_devol")
        self.input_valor_saida_troca_devol.setMinimumSize(QSize(60, 0))
        self.input_valor_saida_troca_devol.setMaximumSize(QSize(60, 16777215))
        self.input_valor_saida_troca_devol.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")

        self.horizontalLayout_11.addWidget(self.input_valor_saida_troca_devol)

        self.label_42 = QLabel(self.frame_trocas_devolucoes)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(60, 0))
        self.label_42.setMaximumSize(QSize(60, 16777215))
        self.label_42.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_11.addWidget(self.label_42)

        self.input_descricao_saida_troca_devol = QLineEdit(self.frame_trocas_devolucoes)
        self.input_descricao_saida_troca_devol.setObjectName(u"input_descricao_saida_troca_devol")
        self.input_descricao_saida_troca_devol.setMinimumSize(QSize(90, 0))
        self.input_descricao_saida_troca_devol.setMaximumSize(QSize(90, 16777215))
        self.input_descricao_saida_troca_devol.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")

        self.horizontalLayout_11.addWidget(self.input_descricao_saida_troca_devol)

        self.btn_inserir_saida_troca_dev = QPushButton(self.frame_trocas_devolucoes)
        self.btn_inserir_saida_troca_dev.setObjectName(u"btn_inserir_saida_troca_dev")
        self.btn_inserir_saida_troca_dev.setMinimumSize(QSize(120, 0))
        self.btn_inserir_saida_troca_dev.setMaximumSize(QSize(120, 16777215))
        self.btn_inserir_saida_troca_dev.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70,50,50);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_inserir_saida_troca_dev)

        self.checkBox_relevancia_saida_cx = QCheckBox(self.frame_trocas_devolucoes)
        self.checkBox_relevancia_saida_cx.setObjectName(u"checkBox_relevancia_saida_cx")
        self.checkBox_relevancia_saida_cx.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_11.addWidget(self.checkBox_relevancia_saida_cx)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_42)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_37)

        self.label_75 = QLabel(self.frame_trocas_devolucoes)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(120, 20))
        self.label_75.setMaximumSize(QSize(120, 20))
        self.label_75.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_27.addWidget(self.label_75)

        self.input_diferenca_total_trocas_devol = QLineEdit(self.frame_trocas_devolucoes)
        self.input_diferenca_total_trocas_devol.setObjectName(u"input_diferenca_total_trocas_devol")
        self.input_diferenca_total_trocas_devol.setMinimumSize(QSize(90, 0))
        self.input_diferenca_total_trocas_devol.setMaximumSize(QSize(90, 16777215))
        self.input_diferenca_total_trocas_devol.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")

        self.horizontalLayout_27.addWidget(self.input_diferenca_total_trocas_devol, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_38)


        self.verticalLayout_15.addLayout(self.horizontalLayout_27)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_26)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_11)

        self.label_30 = QLabel(self.frame_trocas_devolucoes)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(60, 0))
        self.label_30.setMaximumSize(QSize(60, 16777215))
        self.label_30.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_12.addWidget(self.label_30)

        self.input_id_deletar_troca_devol = QLineEdit(self.frame_trocas_devolucoes)
        self.input_id_deletar_troca_devol.setObjectName(u"input_id_deletar_troca_devol")
        self.input_id_deletar_troca_devol.setMinimumSize(QSize(40, 0))
        self.input_id_deletar_troca_devol.setMaximumSize(QSize(40, 16777215))
        self.input_id_deletar_troca_devol.setStyleSheet(u"color: white;\n"
"background-color: black;\n"
"border: solid gray 2px;")
        self.input_id_deletar_troca_devol.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.input_id_deletar_troca_devol)

        self.btn_deletar_id_troca_devol = QPushButton(self.frame_trocas_devolucoes)
        self.btn_deletar_id_troca_devol.setObjectName(u"btn_deletar_id_troca_devol")
        self.btn_deletar_id_troca_devol.setMinimumSize(QSize(120, 0))
        self.btn_deletar_id_troca_devol.setMaximumSize(QSize(90, 16777215))
        self.btn_deletar_id_troca_devol.setBaseSize(QSize(90, 0))
        self.btn_deletar_id_troca_devol.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(110,40,40);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_deletar_id_troca_devol, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)


        self.verticalLayout_15.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_29)

        application_pages.addWidget(self.trocas_devolucoes)
        self.troco_cx = QWidget()
        self.troco_cx.setObjectName(u"troco_cx")
        self.label = QLabel(self.troco_cx)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 30, 161, 16))
        self.groupBox_moedas = QGroupBox(self.troco_cx)
        self.groupBox_moedas.setObjectName(u"groupBox_moedas")
        self.groupBox_moedas.setGeometry(QRect(60, 130, 191, 191))
        self.groupBox_moedas.setStyleSheet(u"color: white;")
        self.label_5 = QLabel(self.groupBox_moedas)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 30, 91, 20))
        self.label_5.setStyleSheet(u"color: lightblue;")
        self.input_moedas_005 = QLineEdit(self.groupBox_moedas)
        self.input_moedas_005.setObjectName(u"input_moedas_005")
        self.input_moedas_005.setGeometry(QRect(120, 30, 41, 22))
        self.input_moedas_005.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.label_6 = QLabel(self.groupBox_moedas)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 60, 91, 20))
        self.label_6.setStyleSheet(u"color: lightblue;")
        self.input_moedas_010 = QLineEdit(self.groupBox_moedas)
        self.input_moedas_010.setObjectName(u"input_moedas_010")
        self.input_moedas_010.setGeometry(QRect(120, 60, 41, 22))
        self.input_moedas_010.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.input_moedas_025 = QLineEdit(self.groupBox_moedas)
        self.input_moedas_025.setObjectName(u"input_moedas_025")
        self.input_moedas_025.setGeometry(QRect(120, 90, 41, 22))
        self.input_moedas_025.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.label_7 = QLabel(self.groupBox_moedas)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 90, 91, 20))
        self.label_7.setStyleSheet(u"color: lightblue;")
        self.label_8 = QLabel(self.groupBox_moedas)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 120, 91, 20))
        self.label_8.setStyleSheet(u"color: lightblue;")
        self.input_moedas_050 = QLineEdit(self.groupBox_moedas)
        self.input_moedas_050.setObjectName(u"input_moedas_050")
        self.input_moedas_050.setGeometry(QRect(120, 120, 41, 22))
        self.input_moedas_050.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.input_moedas_100 = QLineEdit(self.groupBox_moedas)
        self.input_moedas_100.setObjectName(u"input_moedas_100")
        self.input_moedas_100.setGeometry(QRect(120, 150, 41, 22))
        self.input_moedas_100.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.label_9 = QLabel(self.groupBox_moedas)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 150, 91, 20))
        self.label_9.setStyleSheet(u"color: lightblue;")
        self.groupBox_notas = QGroupBox(self.troco_cx)
        self.groupBox_notas.setObjectName(u"groupBox_notas")
        self.groupBox_notas.setGeometry(QRect(450, 80, 201, 251))
        self.groupBox_notas.setStyleSheet(u"color: white;")
        self.input_notas_2 = QLineEdit(self.groupBox_notas)
        self.input_notas_2.setObjectName(u"input_notas_2")
        self.input_notas_2.setGeometry(QRect(130, 30, 41, 22))
        self.input_notas_2.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.label_10 = QLabel(self.groupBox_notas)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 30, 91, 20))
        self.label_10.setStyleSheet(u"color: lightgreen;")
        self.label_11 = QLabel(self.groupBox_notas)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 60, 91, 20))
        self.label_11.setStyleSheet(u"color: lightgreen;")
        self.input_notas_5 = QLineEdit(self.groupBox_notas)
        self.input_notas_5.setObjectName(u"input_notas_5")
        self.input_notas_5.setGeometry(QRect(130, 60, 41, 22))
        self.input_notas_5.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.input_notas_10 = QLineEdit(self.groupBox_notas)
        self.input_notas_10.setObjectName(u"input_notas_10")
        self.input_notas_10.setGeometry(QRect(130, 90, 41, 22))
        self.input_notas_10.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.label_12 = QLabel(self.groupBox_notas)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 90, 91, 20))
        self.label_12.setStyleSheet(u"color: lightgreen;")
        self.label_13 = QLabel(self.groupBox_notas)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 120, 91, 20))
        self.label_13.setStyleSheet(u"color: lightgreen;")
        self.input_notas_20 = QLineEdit(self.groupBox_notas)
        self.input_notas_20.setObjectName(u"input_notas_20")
        self.input_notas_20.setGeometry(QRect(130, 120, 41, 22))
        self.input_notas_20.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.input_notas_50 = QLineEdit(self.groupBox_notas)
        self.input_notas_50.setObjectName(u"input_notas_50")
        self.input_notas_50.setGeometry(QRect(130, 150, 41, 22))
        self.input_notas_50.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.label_14 = QLabel(self.groupBox_notas)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 150, 91, 20))
        self.label_14.setStyleSheet(u"color: lightgreen;")
        self.input_notas_100 = QLineEdit(self.groupBox_notas)
        self.input_notas_100.setObjectName(u"input_notas_100")
        self.input_notas_100.setGeometry(QRect(130, 180, 41, 22))
        self.input_notas_100.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.label_15 = QLabel(self.groupBox_notas)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 180, 91, 20))
        self.label_15.setStyleSheet(u"color: lightgreen;")
        self.input_notas_200 = QLineEdit(self.groupBox_notas)
        self.input_notas_200.setObjectName(u"input_notas_200")
        self.input_notas_200.setGeometry(QRect(130, 210, 41, 22))
        self.input_notas_200.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.label_16 = QLabel(self.groupBox_notas)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 210, 91, 20))
        self.label_16.setStyleSheet(u"color: lightgreen;")
        self.groupBox_total_troco = QGroupBox(self.troco_cx)
        self.groupBox_total_troco.setObjectName(u"groupBox_total_troco")
        self.groupBox_total_troco.setGeometry(QRect(80, 330, 291, 141))
        self.groupBox_total_troco.setStyleSheet(u"color: white;")
        self.label_2 = QLabel(self.groupBox_total_troco)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 40, 81, 20))
        self.label_2.setStyleSheet(u"color: lightblue;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_3 = QLabel(self.groupBox_total_troco)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 70, 81, 20))
        self.label_3.setStyleSheet(u"color: lightgreen;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_4 = QLabel(self.groupBox_total_troco)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 100, 81, 20))
        self.label_4.setStyleSheet(u"color: pink;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.input_total_moedas = QLineEdit(self.groupBox_total_troco)
        self.input_total_moedas.setObjectName(u"input_total_moedas")
        self.input_total_moedas.setGeometry(QRect(140, 40, 113, 22))
        self.input_total_moedas.setStyleSheet(u"background-color: white;\n"
"color: blue;")
        self.input_total_moedas.setReadOnly(True)
        self.input_total_dinheiro = QLineEdit(self.groupBox_total_troco)
        self.input_total_dinheiro.setObjectName(u"input_total_dinheiro")
        self.input_total_dinheiro.setGeometry(QRect(140, 70, 113, 22))
        self.input_total_dinheiro.setStyleSheet(u"background-color: white;\n"
"color: green;")
        self.input_total_dinheiro.setReadOnly(True)
        self.input_total_troco = QLineEdit(self.groupBox_total_troco)
        self.input_total_troco.setObjectName(u"input_total_troco")
        self.input_total_troco.setGeometry(QRect(140, 100, 113, 22))
        self.input_total_troco.setStyleSheet(u"background-color: white;\n"
"color: red;")
        self.input_total_troco.setReadOnly(True)
        self.btn_limpar_campos_facilitador_troco_cx = QPushButton(self.troco_cx)
        self.btn_limpar_campos_facilitador_troco_cx.setObjectName(u"btn_limpar_campos_facilitador_troco_cx")
        self.btn_limpar_campos_facilitador_troco_cx.setGeometry(QRect(450, 380, 201, 41))
        self.btn_limpar_campos_facilitador_troco_cx.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70,50,70);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        self.opcao_troco_cx = QRadioButton(self.troco_cx)
        self.opcao_troco_cx.setObjectName(u"opcao_troco_cx")
        self.opcao_troco_cx.setGeometry(QRect(420, 60, 131, 20))
        self.opcao_troco_cx.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: white;")
        self.opcao_estoque_troco_cx = QRadioButton(self.troco_cx)
        self.opcao_estoque_troco_cx.setObjectName(u"opcao_estoque_troco_cx")
        self.opcao_estoque_troco_cx.setGeometry(QRect(210, 60, 171, 20))
        self.opcao_estoque_troco_cx.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: white;")
        self.btn_enviando_facilitador_troco_para_fechamento_caixa = QPushButton(self.troco_cx)
        self.btn_enviando_facilitador_troco_para_fechamento_caixa.setObjectName(u"btn_enviando_facilitador_troco_para_fechamento_caixa")
        self.btn_enviando_facilitador_troco_para_fechamento_caixa.setGeometry(QRect(450, 430, 201, 41))
        self.btn_enviando_facilitador_troco_para_fechamento_caixa.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50,50,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")
        application_pages.addWidget(self.troco_cx)
        self.initial_page = QWidget()
        self.initial_page.setObjectName(u"initial_page")
        self.verticalLayout_16 = QVBoxLayout(self.initial_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_9)

        self.label_45 = QLabel(self.initial_page)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(240, 0))
        self.label_45.setMaximumSize(QSize(240, 16777215))
        self.label_45.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: white;")
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_45, 0, Qt.AlignmentFlag.AlignHCenter)

        self.textBrowser_initial_page = QTextBrowser(self.initial_page)
        self.textBrowser_initial_page.setObjectName(u"textBrowser_initial_page")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textBrowser_initial_page.sizePolicy().hasHeightForWidth())
        self.textBrowser_initial_page.setSizePolicy(sizePolicy5)
        self.textBrowser_initial_page.setMinimumSize(QSize(360, 240))
        self.textBrowser_initial_page.setMaximumSize(QSize(360, 240))
        self.textBrowser_initial_page.setStyleSheet(u"font: 600 10pt \"Segoe UI\";\n"
"color: white;")

        self.verticalLayout_16.addWidget(self.textBrowser_initial_page, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_10)

        application_pages.addWidget(self.initial_page)
        self.escolha_data_cx = QWidget()
        self.escolha_data_cx.setObjectName(u"escolha_data_cx")
        self.escolha_data_cx.setMinimumSize(QSize(480, 360))
        self.escolha_data_cx.setBaseSize(QSize(480, 360))
        self.verticalLayout_8 = QVBoxLayout(self.escolha_data_cx)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.escolha_data_cx)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(420, 540))
        self.frame_3.setMaximumSize(QSize(420, 540))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 750 18pt \"Segoe UI\";\n"
"color: white;")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_17)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.opcao_cx_fechado = QRadioButton(self.frame_3)
        self.opcao_cx_fechado.setObjectName(u"opcao_cx_fechado")
        self.opcao_cx_fechado.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: white;")

        self.horizontalLayout_13.addWidget(self.opcao_cx_fechado)

        self.opcao_cx_a_fechar = QRadioButton(self.frame_3)
        self.opcao_cx_a_fechar.setObjectName(u"opcao_cx_a_fechar")
        sizePolicy.setHeightForWidth(self.opcao_cx_a_fechar.sizePolicy().hasHeightForWidth())
        self.opcao_cx_a_fechar.setSizePolicy(sizePolicy)
        self.opcao_cx_a_fechar.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: white;")

        self.horizontalLayout_13.addWidget(self.opcao_cx_a_fechar)

        self.opcao_cx_outros = QRadioButton(self.frame_3)
        self.opcao_cx_outros.setObjectName(u"opcao_cx_outros")
        self.opcao_cx_outros.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: white;")

        self.horizontalLayout_13.addWidget(self.opcao_cx_outros)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.calendario_widget = QCalendarWidget(self.frame_3)
        self.calendario_widget.setObjectName(u"calendario_widget")
        self.calendario_widget.setMinimumSize(QSize(360, 280))
        self.calendario_widget.setMaximumSize(QSize(360, 280))
        self.calendario_widget.setStyleSheet(u"QCalendarWidget {\n"
"                background-color: #f8f9fa;\n"
"                border: 2px solid #dee2e6;\n"
"                border-radius: 8px;\n"
"            }\n"
"           \n"
"            QCalendarWidget QToolButton {\n"
"                color: #495057;\n"
"                background-color: #e9ecef;\n"
"                border-radius: 4px;\n"
"                padding: 5px;\n"
"            }\n"
"           \n"
"            QCalendarWidget QToolButton:hover {\n"
"                background-color: #ced4da;\n"
"            }\n"
"           \n"
"            QCalendarWidget QMenu {\n"
"                background-color: white;\n"
"                border: 1px solid #dee2e6;\n"
"            }\n"
"           \n"
"            QCalendarWidget QSpinBox {\n"
"                background-color: #e9ecef;\n"
"                border-radius: 4px;\n"
"                padding: 3px;\n"
"            }\n"
"           \n"
"            QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"                background-color:"
                        " white;\n"
"                min-height: 40px;\n"
"            }\n"
"           \n"
"            QCalendarWidget QAbstractItemView:enabled {\n"
"                color: #212529;\n"
"                background-color: white;\n"
"                selection-background-color: #007bff;\n"
"                selection-color: white;\n"
"            }\n"
"          \n"
"")
        self.calendario_widget.setGridVisible(True)
        self.calendario_widget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendario_widget.setNavigationBarVisible(True)
        self.calendario_widget.setDateEditEnabled(True)

        self.verticalLayout.addWidget(self.calendario_widget, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.checkBox_loja_fechada = QCheckBox(self.frame_3)
        self.checkBox_loja_fechada.setObjectName(u"checkBox_loja_fechada")
        self.checkBox_loja_fechada.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: orange;")
        self.checkBox_loja_fechada.setChecked(False)

        self.verticalLayout.addWidget(self.checkBox_loja_fechada, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_11)

        self.btn_data_escolhida = QPushButton(self.frame_3)
        self.btn_data_escolhida.setObjectName(u"btn_data_escolhida")
        self.btn_data_escolhida.setMinimumSize(QSize(400, 0))
        self.btn_data_escolhida.setMaximumSize(QSize(400, 16777215))
        self.btn_data_escolhida.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68,71,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.verticalLayout.addWidget(self.btn_data_escolhida)


        self.verticalLayout_8.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignHCenter)

        application_pages.addWidget(self.escolha_data_cx)
        self.page_insercao_entradas_nao_operadora = QWidget()
        self.page_insercao_entradas_nao_operadora.setObjectName(u"page_insercao_entradas_nao_operadora")
        self.verticalLayout_21 = QVBoxLayout(self.page_insercao_entradas_nao_operadora)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_22)

        self.label_72 = QLabel(self.page_insercao_entradas_nao_operadora)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_72.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_72)

        self.frame_5 = QFrame(self.page_insercao_entradas_nao_operadora)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(600, 360))
        self.frame_5.setMaximumSize(QSize(600, 360))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_20)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_70 = QLabel(self.frame_5)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_70.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_70)

        self.data_cx_entradas_n_operadora = QDateEdit(self.frame_5)
        self.data_cx_entradas_n_operadora.setObjectName(u"data_cx_entradas_n_operadora")
        self.data_cx_entradas_n_operadora.setEnabled(True)
        sizePolicy.setHeightForWidth(self.data_cx_entradas_n_operadora.sizePolicy().hasHeightForWidth())
        self.data_cx_entradas_n_operadora.setSizePolicy(sizePolicy)
        self.data_cx_entradas_n_operadora.setMinimumSize(QSize(120, 0))
        self.data_cx_entradas_n_operadora.setMaximumSize(QSize(120, 16777215))
        self.data_cx_entradas_n_operadora.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(0,0,0);")
        self.data_cx_entradas_n_operadora.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_cx_entradas_n_operadora.setReadOnly(True)

        self.horizontalLayout_24.addWidget(self.data_cx_entradas_n_operadora)


        self.verticalLayout_22.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_21)

        self.tableView_entradas_n_operadora = QTableView(self.frame_5)
        self.tableView_entradas_n_operadora.setObjectName(u"tableView_entradas_n_operadora")
        self.tableView_entradas_n_operadora.setStyleSheet(u"QTableView {\n"
"	alternate-background-color: #f8f9fa;\n"
"	background-color: white;\n"
"	gridline-color: #dee2e6;\n"
"}\n"
"\n"
"QTableView::item {\n"
"	padding: 5px;\n"
"	border-bottom: 1px solid #dee2e6;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"	background-color: #007bff;\n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: #6c757d;\n"
"	color: white;\n"
"	padding: 5px;\n"
"	border: 1px solid #5a6268;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_22.addWidget(self.tableView_entradas_n_operadora)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_33)

        self.comboBox_entradas_n_operadora = QComboBox(self.frame_5)
        self.comboBox_entradas_n_operadora.setObjectName(u"comboBox_entradas_n_operadora")
        self.comboBox_entradas_n_operadora.setMinimumSize(QSize(120, 0))
        self.comboBox_entradas_n_operadora.setMaximumSize(QSize(120, 16777215))
        self.comboBox_entradas_n_operadora.setStyleSheet(u"font: 600 9pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: rgb(68,71,90);")

        self.horizontalLayout_25.addWidget(self.comboBox_entradas_n_operadora)

        self.label_74 = QLabel(self.frame_5)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(45, 0))
        self.label_74.setMaximumSize(QSize(45, 16777215))
        self.label_74.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_74.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_74)

        self.input_valor_entradas_n_operadora = QLineEdit(self.frame_5)
        self.input_valor_entradas_n_operadora.setObjectName(u"input_valor_entradas_n_operadora")
        self.input_valor_entradas_n_operadora.setMinimumSize(QSize(90, 0))
        self.input_valor_entradas_n_operadora.setMaximumSize(QSize(90, 16777215))
        self.input_valor_entradas_n_operadora.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: rgb(68,71,90);")
        self.input_valor_entradas_n_operadora.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.input_valor_entradas_n_operadora)

        self.btn_inserir_entradas_n_operadora = QPushButton(self.frame_5)
        self.btn_inserir_entradas_n_operadora.setObjectName(u"btn_inserir_entradas_n_operadora")
        self.btn_inserir_entradas_n_operadora.setMinimumSize(QSize(150, 0))
        self.btn_inserir_entradas_n_operadora.setMaximumSize(QSize(150, 16777215))
        self.btn_inserir_entradas_n_operadora.setStyleSheet(u"QPushButton {\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	background-color: rgb(50,50,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_25.addWidget(self.btn_inserir_entradas_n_operadora)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_34)


        self.verticalLayout_22.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_35)

        self.label_71 = QLabel(self.frame_5)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"font: 700 8pt \"Segoe UI\";\n"
"color: rgb(255,255,255);")
        self.label_71.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.label_71)

        self.input_id_deletar_entradas_n_operadora = QLineEdit(self.frame_5)
        self.input_id_deletar_entradas_n_operadora.setObjectName(u"input_id_deletar_entradas_n_operadora")
        self.input_id_deletar_entradas_n_operadora.setMinimumSize(QSize(45, 0))
        self.input_id_deletar_entradas_n_operadora.setMaximumSize(QSize(45, 16777215))
        self.input_id_deletar_entradas_n_operadora.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: rgb(68,71,90);")
        self.input_id_deletar_entradas_n_operadora.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_id_deletar_entradas_n_operadora.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.input_id_deletar_entradas_n_operadora)

        self.btn_deletar_entradas_n_operadora = QPushButton(self.frame_5)
        self.btn_deletar_entradas_n_operadora.setObjectName(u"btn_deletar_entradas_n_operadora")
        self.btn_deletar_entradas_n_operadora.setMinimumSize(QSize(150, 0))
        self.btn_deletar_entradas_n_operadora.setMaximumSize(QSize(150, 16777215))
        self.btn_deletar_entradas_n_operadora.setStyleSheet(u"QPushButton {\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	background-color: rgb(110,40,40);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.horizontalLayout_26.addWidget(self.btn_deletar_entradas_n_operadora)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_36)


        self.verticalLayout_22.addLayout(self.horizontalLayout_26)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_19)


        self.verticalLayout_21.addWidget(self.frame_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_23)

        application_pages.addWidget(self.page_insercao_entradas_nao_operadora)

        self.retranslateUi(application_pages)

        application_pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label_26.setText(QCoreApplication.translate("application_pages", u"Ver Despesa(s) do Caixa", None))
        self.label_34.setText(QCoreApplication.translate("application_pages", u"Data do Cx. :", None))
        self.label_25.setText(QCoreApplication.translate("application_pages", u"Digite o ID da Despesa de Caixa :", None))
        self.btn_deletar_despesa_cx.setText(QCoreApplication.translate("application_pages", u"Deletar Despesa", None))
        self.btn_inserir_despesa_cx.setText(QCoreApplication.translate("application_pages", u"Inserir Despesa", None))
        self.label_23.setText(QCoreApplication.translate("application_pages", u"Observa\u00e7\u00e3o do Cx. :", None))
        self.label_24.setText(QCoreApplication.translate("application_pages", u"Data do Cx. :", None))
        self.label_76.setText(QCoreApplication.translate("application_pages", u"digite a observa\u00e7\u00e3o a inserir...", None))
        self.textEdit_observacao_cx.setPlaceholderText("")
        self.label_44.setText(QCoreApplication.translate("application_pages", u"ID da observa\u00e7\u00e3o: ", None))
        self.btn_deletar_observacao.setText(QCoreApplication.translate("application_pages", u"Deletar Observacao", None))
        self.btn_inserir_observacao.setText(QCoreApplication.translate("application_pages", u"Inserir Observa\u00e7\u00e3o", None))
        self.groupBox.setTitle("")
        self.label_28.setText(QCoreApplication.translate("application_pages", u"Data do Cx. :", None))
        self.label_29.setText(QCoreApplication.translate("application_pages", u"Vendas do dia lida:", None))
        self.groupBox_despesas_cx.setTitle(QCoreApplication.translate("application_pages", u"Despesas", None))
        self.label_47.setText(QCoreApplication.translate("application_pages", u"Total das despesas de Caixa: ", None))
        self.btn_ver_despesas.setText(QCoreApplication.translate("application_pages", u"ver", None))
        self.groupBox_troco.setTitle(QCoreApplication.translate("application_pages", u"Troco", None))
        self.label_18.setText(QCoreApplication.translate("application_pages", u"Troco de Caixa :", None))
        self.label_37.setText(QCoreApplication.translate("application_pages", u"Estoque Troco de Caixa :", None))
        self.label_38.setText(QCoreApplication.translate("application_pages", u"Troco de Caixa anterior :", None))
        self.label_39.setText(QCoreApplication.translate("application_pages", u"Estoque Troco de Cx ant. :", None))
        self.label_40.setText(QCoreApplication.translate("application_pages", u"Resultado Troco de Caixa :", None))
        self.btn_repetir_troco_cx.setText(QCoreApplication.translate("application_pages", u"repetir", None))
        self.btn_repetir_estoque_troco_cx.setText(QCoreApplication.translate("application_pages", u"repetir", None))
        self.groupBox_entradas.setTitle(QCoreApplication.translate("application_pages", u"Entradas", None))
        self.label_31.setText(QCoreApplication.translate("application_pages", u"Total M\u00e1quina de Cart\u00f5es: :", None))
        self.label_35.setText(QCoreApplication.translate("application_pages", u"vendas_dinheiro:", None))
        self.label_36.setText(QCoreApplication.translate("application_pages", u"vendas PIX direto CNPJ:", None))
        self.label_69.setText(QCoreApplication.translate("application_pages", u"diferen\u00e7a:", None))
        self.label_73.setText(QCoreApplication.translate("application_pages", u"vendas PIX direto CPF:", None))
        self.btn_ver_entrada_n_operadora.setText(QCoreApplication.translate("application_pages", u"ver", None))
        self.groupBox_resultado_caixa.setTitle(QCoreApplication.translate("application_pages", u"Resultado Caixa", None))
        self.groupBox_trocas_devolucoes.setTitle(QCoreApplication.translate("application_pages", u"Trocas/Devolu\u00e7\u00f5es", None))
        self.label_48.setText(QCoreApplication.translate("application_pages", u"Trocas/Devolu\u00e7\u00f5es Produtos: ", None))
        self.label_49.setText(QCoreApplication.translate("application_pages", u"Trocas/Devolu\u00e7\u00f5es Dinheiro: ", None))
        self.label_50.setText(QCoreApplication.translate("application_pages", u"Trocas/Devolu\u00e7\u00f5es D\u00e9bito: ", None))
        self.label_51.setText(QCoreApplication.translate("application_pages", u"Trocas/Devolu\u00e7\u00f5es Cr\u00e9dito:", None))
        self.btn_ver_trocas_dev.setText(QCoreApplication.translate("application_pages", u"ver todas trocas e devolu\u00e7\u00f5es do caixa", None))
        self.btn_apurar_resultado_caixa.setText(QCoreApplication.translate("application_pages", u"Apurar o resultado do Caixa", None))
        self.btn_enviar_fechamento_caixa.setText(QCoreApplication.translate("application_pages", u"Enviar Fechamento de Caixa", None))
        self.btn_enviar_fechamento_parcial_caixa.setText(QCoreApplication.translate("application_pages", u"Enviar Fechamento Parcial de Caixa", None))
        self.btn_caixa_visto.setText(QCoreApplication.translate("application_pages", u"Caixa Visto", None))
        self.groupBox_fechamentos_parciais.setTitle(QCoreApplication.translate("application_pages", u"Fechamentos Parciais", None))
        self.btn_ver_fechamentos_parciais.setText(QCoreApplication.translate("application_pages", u"ver", None))
        self.label_fecham_parc_cx.setText(QCoreApplication.translate("application_pages", u"TextLabel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("application_pages", u"Usu\u00e1rio", None))
        self.groupBox_observacoes.setTitle(QCoreApplication.translate("application_pages", u"Observa\u00e7\u00f5es", None))
        self.btn_ver_observacoes.setText(QCoreApplication.translate("application_pages", u"ver", None))
        self.label_observacoes.setText("")
        self.btn_atualizar_vendas.setText(QCoreApplication.translate("application_pages", u"atualizar vendas", None))
        self.label_46.setText(QCoreApplication.translate("application_pages", u"Fechamentos parciais de caixa", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("application_pages", u"Dados do Caixa", None))
        self.label_53.setText(QCoreApplication.translate("application_pages", u"Data do Cx. :", None))
        self.label_54.setText(QCoreApplication.translate("application_pages", u"Vendas do dia lida:", None))
        self.groupBox_despesas_cx_parc.setTitle(QCoreApplication.translate("application_pages", u"Despesas", None))
        self.label_55.setText(QCoreApplication.translate("application_pages", u"Total das despesas de Caixa: ", None))
        self.groupBox_troco_parc.setTitle(QCoreApplication.translate("application_pages", u"Troco", None))
        self.label_56.setText(QCoreApplication.translate("application_pages", u"Troco de Caixa :", None))
        self.label_57.setText(QCoreApplication.translate("application_pages", u"Estoque Troco de Caixa :", None))
        self.label_58.setText(QCoreApplication.translate("application_pages", u"Troco de Caixa anterior :", None))
        self.label_59.setText(QCoreApplication.translate("application_pages", u"Estoque Troco de Cx ant. :", None))
        self.label_60.setText(QCoreApplication.translate("application_pages", u"Resultado Troco de Caixa :", None))
        self.groupBox_entradas_parc.setTitle(QCoreApplication.translate("application_pages", u"Entradas", None))
        self.label_61.setText(QCoreApplication.translate("application_pages", u"Total M\u00e1quina de Cart\u00f5es: :", None))
        self.label_62.setText(QCoreApplication.translate("application_pages", u"vendas_dinheiro:", None))
        self.label_63.setText(QCoreApplication.translate("application_pages", u"vendas PIX direto:", None))
        self.groupBox_resultado_caixa_2.setTitle(QCoreApplication.translate("application_pages", u"Resultado Caixa", None))
        self.label_64.setText(QCoreApplication.translate("application_pages", u"Resultado do Caixa :", None))
        self.groupBox_trocas_devolucoes_parc.setTitle(QCoreApplication.translate("application_pages", u"Trocas/Devolu\u00e7\u00f5es", None))
        self.label_65.setText(QCoreApplication.translate("application_pages", u"Trocas/Devolu\u00e7\u00f5es Produtos: ", None))
        self.label_66.setText(QCoreApplication.translate("application_pages", u"Trocas/Devolu\u00e7\u00f5es Dinheiro: ", None))
        self.label_67.setText(QCoreApplication.translate("application_pages", u"Trocas/Devolu\u00e7\u00f5es D\u00e9bito: ", None))
        self.label_68.setText(QCoreApplication.translate("application_pages", u"Trocas/Devolu\u00e7\u00f5es Cr\u00e9dito:", None))
        self.btn_caixa_visto_parc.setText(QCoreApplication.translate("application_pages", u"Caixa Parcial Visto", None))
        self.groupBox_usuario_parc.setTitle(QCoreApplication.translate("application_pages", u"Usu\u00e1rio", None))
        self.label_52.setText(QCoreApplication.translate("application_pages", u"Despesas de Caixa", None))
        self.btn_enviar_despesa_caixa.setText(QCoreApplication.translate("application_pages", u"Enviar Despesa do Caixa", None))
        self.label_22.setText(QCoreApplication.translate("application_pages", u"Valor da despesa :", None))
        self.label_20.setText(QCoreApplication.translate("application_pages", u"Descri\u00e7\u00e3o da despesa :", None))
        self.label_19.setText(QCoreApplication.translate("application_pages", u"Data do Caixa :", None))
        self.label_21.setText(QCoreApplication.translate("application_pages", u"Despesas ID :", None))
        self.label_login.setText(QCoreApplication.translate("application_pages", u"Login", None))
        self.input_user_code.setPlaceholderText(QCoreApplication.translate("application_pages", u"c\u00f3digo do usu\u00e1rio", None))
        self.btn_login.setText(QCoreApplication.translate("application_pages", u"Logue-se !", None))
        self.lbl_ola.setText(QCoreApplication.translate("application_pages", u"Seja bem-vindo(a):", None))
        self.nome_usuario_login.setText("")
        self.btn_selection_date.setText(QCoreApplication.translate("application_pages", u"Ir para sele\u00e7\u00e3o referencial de Data", None))
        self.label_32.setText(QCoreApplication.translate("application_pages", u"Trocas e/ou Devolu\u00e7\u00f5es", None))
        self.label_27.setText(QCoreApplication.translate("application_pages", u"Data do Cx. :", None))
        self.label_79.setText(QCoreApplication.translate("application_pages", u"Entradas:", None))
        self.label_77.setText(QCoreApplication.translate("application_pages", u"Tipo: ", None))
        self.label_41.setText(QCoreApplication.translate("application_pages", u"Valor: ", None))
        self.label_33.setText(QCoreApplication.translate("application_pages", u"C\u00f3d. Prod.:", None))
        self.btn_inserir_entrada_troca_dev.setText(QCoreApplication.translate("application_pages", u"Inserir Entrada", None))
        self.checkBox_relevancia_entrada_cx.setText(QCoreApplication.translate("application_pages", u"relev.", None))
        self.label_80.setText(QCoreApplication.translate("application_pages", u"Sa\u00eddas:", None))
        self.label_78.setText(QCoreApplication.translate("application_pages", u"Tipo: ", None))
        self.label_43.setText(QCoreApplication.translate("application_pages", u"Valor: ", None))
        self.label_42.setText(QCoreApplication.translate("application_pages", u"C\u00f3d Prod: ", None))
        self.btn_inserir_saida_troca_dev.setText(QCoreApplication.translate("application_pages", u"Inserir Sa\u00edda", None))
        self.checkBox_relevancia_saida_cx.setText(QCoreApplication.translate("application_pages", u"relev.", None))
        self.label_75.setText(QCoreApplication.translate("application_pages", u"Total diferen\u00e7a geral:", None))
        self.label_30.setText(QCoreApplication.translate("application_pages", u"Deletar ID: ", None))
        self.btn_deletar_id_troca_devol.setText(QCoreApplication.translate("application_pages", u"Deletar ID", None))
        self.label.setText(QCoreApplication.translate("application_pages", u"Facilitador de Troco de Caixa", None))
        self.groupBox_moedas.setTitle(QCoreApplication.translate("application_pages", u"Moedas", None))
        self.label_5.setText(QCoreApplication.translate("application_pages", u"Moedas de 0,05 :", None))
        self.label_6.setText(QCoreApplication.translate("application_pages", u"Moedas de 0,10 :", None))
        self.label_7.setText(QCoreApplication.translate("application_pages", u"Moedas de 0,25 :", None))
        self.label_8.setText(QCoreApplication.translate("application_pages", u"Moedas de 0,50 :", None))
        self.label_9.setText(QCoreApplication.translate("application_pages", u"Moedas de 1,00 :", None))
        self.groupBox_notas.setTitle(QCoreApplication.translate("application_pages", u"Notas", None))
        self.label_10.setText(QCoreApplication.translate("application_pages", u"Notas de 2,00 :", None))
        self.label_11.setText(QCoreApplication.translate("application_pages", u"Notas de 5,00 :", None))
        self.label_12.setText(QCoreApplication.translate("application_pages", u"Notas de 10,00 :", None))
        self.label_13.setText(QCoreApplication.translate("application_pages", u"Notas de 20,00 :", None))
        self.label_14.setText(QCoreApplication.translate("application_pages", u"Notas de 50,00 :", None))
        self.label_15.setText(QCoreApplication.translate("application_pages", u"Notas de 100,00 :", None))
        self.label_16.setText(QCoreApplication.translate("application_pages", u"Notas de 200,00 :", None))
        self.groupBox_total_troco.setTitle(QCoreApplication.translate("application_pages", u"Total", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"Total Moedas:", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"Total Dinheiro:", None))
        self.label_4.setText(QCoreApplication.translate("application_pages", u"Total troco:", None))
        self.btn_limpar_campos_facilitador_troco_cx.setText(QCoreApplication.translate("application_pages", u"Limpar Campos", None))
        self.opcao_troco_cx.setText(QCoreApplication.translate("application_pages", u"Troco de Caixa", None))
        self.opcao_estoque_troco_cx.setText(QCoreApplication.translate("application_pages", u"Estoque Troco de Caixa", None))
        self.btn_enviando_facilitador_troco_para_fechamento_caixa.setText(QCoreApplication.translate("application_pages", u"Enviar Troco p Fecham Caixa", None))
        self.label_45.setText(QCoreApplication.translate("application_pages", u"Logado", None))
        self.label_17.setText(QCoreApplication.translate("application_pages", u"Escolha da Data para o Caixa", None))
        self.opcao_cx_fechado.setText(QCoreApplication.translate("application_pages", u"Cx Fechado", None))
        self.opcao_cx_a_fechar.setText(QCoreApplication.translate("application_pages", u"Cx a fechar", None))
        self.opcao_cx_outros.setText(QCoreApplication.translate("application_pages", u"Outros", None))
        self.checkBox_loja_fechada.setText(QCoreApplication.translate("application_pages", u"Dia com a loja fechada", None))
        self.btn_data_escolhida.setText(QCoreApplication.translate("application_pages", u"Data Escolhida", None))
        self.label_72.setText(QCoreApplication.translate("application_pages", u"Entradas que n\u00e3o passaram pela M\u00e1quina Operadora", None))
        self.label_70.setText(QCoreApplication.translate("application_pages", u"Entradas n\u00e3o Operadora", None))
        self.label_74.setText(QCoreApplication.translate("application_pages", u"valor: ", None))
        self.btn_inserir_entradas_n_operadora.setText(QCoreApplication.translate("application_pages", u"Inserir Entrada", None))
        self.label_71.setText(QCoreApplication.translate("application_pages", u"Deletar o ID da Entrada:", None))
        self.btn_deletar_entradas_n_operadora.setText(QCoreApplication.translate("application_pages", u"Deletar Entrada", None))
    # retranslateUi

