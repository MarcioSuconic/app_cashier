from qt_core import *
from gui.pages.ui_pages import Ui_application_pages

from gui.widgets.py_push_button import PyPushButton

class UI_MainWindow(object):

    def setup_ui(self, parent):

        self.version = "v 1.0.1"

        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # SET INITIAL PARAMETERS
        parent.resize(900,640)
        parent.setMinimumSize(720,580)

        # CREATE CENTRAL WIDGET 
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #282a36")

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)

        # CREATE MAIN layout
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)

        # LEFT MENU TOP
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        # quando aplicamos a cor de fundo nos nossos frames os filhos herdam. se colocamos uma ID (abaixo) aí os filhos não herdam
        self.left_menu_top_frame.setObjectName("left_menu_top_frame") # sempre se usa o mesmo nome
        self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame {background-color: #44475a;}")


        # LEFT FRAME - ESPAÇADOR VERTICAL
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # LEFT MENU BOTTOM
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame") # como se fosse uma ID
        self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame {background-color: #44475a;}")

        # LABEL VERSION
        self.left_menu_label_version = QLabel(self.version)
        self.left_menu_label_version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("background-color: 'black'; color: 'white';")

        # LEFT MENU TOP LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)

        # LEFT MENU BOTTOM LAYOUT
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)

        # BOTTOM BUTTONS
        self.btn_bottom = QPushButton("Settings")

        # add ao layout
        self.left_menu_bottom_layout.addWidget(self.btn_bottom)

        # TOP BUTTONS 
        self.btn_toggle = PyPushButton(text="Ocultar menu", is_active=True, btn_hover='red', btn_pressed='blue')
        self.btn_data_cx = PyPushButton(text="Escolha Data Caixa", is_active=True, btn_hover='red', btn_pressed='blue')
        self.btn_troco_cx = PyPushButton(text="Facilitador Troco Cx", is_active=True, btn_hover='red', btn_pressed='blue')
        self.btn_despesas = PyPushButton(text="Despesas Caixa", is_active=True, btn_hover='red', btn_pressed='blue')
        self.btn_obs_cx = PyPushButton(text="Observações Caixa", is_active=True, btn_hover='red', btn_pressed='blue')
        self.btn_trocas_devolucoes = PyPushButton(text="Trocas e/ou Devol.", is_active=True, btn_hover='red', btn_pressed='blue')
        self.btn_entradas_n_operadora = PyPushButton(text="Ent. ñ Máq.", is_active=True, btn_hover='red', btn_pressed='blue')
        self.btn_fech_cx = PyPushButton(text="Fechamento Caixa", is_active=True, btn_hover='red', btn_pressed='blue')

        # add ao Layout
        self.left_menu_top_layout.addWidget(self.btn_toggle)
        self.left_menu_top_layout.addWidget(self.btn_data_cx)
        self.left_menu_top_layout.addWidget(self.btn_troco_cx)
        self.left_menu_top_layout.addWidget(self.btn_despesas)
        self.left_menu_top_layout.addWidget(self.btn_obs_cx)
        self.left_menu_top_layout.addWidget(self.btn_trocas_devolucoes)
        self.left_menu_top_layout.addWidget(self.btn_entradas_n_operadora)
        self.left_menu_top_layout.addWidget(self.btn_fech_cx)

        # add ao layout
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36;")

        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setStyleSheet("background-color: #6272a4;")

        # Layout TOP BAR
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)

        # TOP BAR LEFT LABEL
        self.top_bar_left_label = QLabel("MARSOFT")

        # TOP BAR CENTRAL LABEL
        self.top_bar_central_label = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # TOP BAR LABEL RIGHT
        self.top_bar_right_label = QLabel("| PÁGINA INICIAL")
        self.top_bar_right_label.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # add widgets ao layout
        self.top_bar_layout.addWidget(self.top_bar_left_label)
        self.top_bar_layout.addItem(self.top_bar_central_label)
        self.top_bar_layout.addWidget(self.top_bar_right_label)

        # Applications Pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.login)

        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)        
        self.content_layout.setSpacing(0)

        # BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #6272a4;")

        # layout BOTTOM BAR
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout

        # BOTTOM BAR LEFT LABEL
        self.bottom_bar_left_label = QLabel("Criado por Marcio Gonçalves Crancianinov Suconic")

        # BOTTOM BAR CENTRAL LABEL
        self.bottom_bar_central_label = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # BOTTOM BAR LABEL RIGHT
        self.bottom_bar_right_label = QLabel("© 2026")
        self.bottom_bar_right_label.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # add widgets ao layout
        self.bottom_bar_layout.addWidget(self.bottom_bar_left_label)
        self.bottom_bar_layout.addItem(self.bottom_bar_central_label)
        self.bottom_bar_layout.addWidget(self.bottom_bar_right_label)

        # ADD ao layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # ADD ao layout
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)    
