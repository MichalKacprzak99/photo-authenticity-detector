from PyQt5 import QtCore, QtWidgets
from intro_window import IntroWindow
from load_image import LoadImage


class UiStartWindow(object):
    def setupUi(self, start_window):
        self.start_window = start_window
        self.start_window.setObjectName("start_window")
        self.start_window.resize(644, 677)
        self.start_window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.start_window.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(start_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 180, 351, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_menu_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_menu_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.main_menu_layout.setContentsMargins(12, 0, 12, 0)
        self.main_menu_layout.setSpacing(10)
        self.main_menu_layout.setObjectName("main_menu_layout")
        self.image_load_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.image_load_button.setIconSize(QtCore.QSize(20, 19))
        self.image_load_button.setObjectName("image_load_button")
        self.main_menu_layout.addWidget(self.image_load_button)
        self.open_instruction_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_instruction_button.setObjectName("open_instruction_button")
        self.main_menu_layout.addWidget(self.open_instruction_button)
        self.open_description_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_description_button.setObjectName("open_description_button")
        self.main_menu_layout.addWidget(self.open_description_button)
        self.open_credits_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_credits_button.setObjectName("open_credits_button")
        self.main_menu_layout.addWidget(self.open_credits_button)
        self.start_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(start_window)
        QtCore.QMetaObject.connectSlotsByName(start_window)

    def retranslateUi(self, start_window):
        _translate = QtCore.QCoreApplication.translate
        self.start_window.setWindowTitle(_translate("start_window", "MainWindow"))
        self.image_load_button.setText(_translate("start_window", "CHECK IMAGE"))
        self.open_instruction_button.setText(_translate("start_window", "INSTRUCTIONS"))
        self.open_description_button.setText(_translate("start_window", "PROJECT DESCRIPTION"))
        self.open_credits_button.setText(_translate("start_window", "CREDITS"))


class StartWindow(UiStartWindow):
    def __init__(self, start_window):
        self.setupUi(start_window)
        window = QtWidgets.QMainWindow()
        self.intro_window = IntroWindow(window, start_window)
        self.image_load_button.clicked.connect(self.load_user_image)

    def load_user_image(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        imagePath, _ = QtWidgets.QFileDialog.getOpenFileName(self.start_window, "QFileDialog.getOpenFileName()", "",
                                                  "Image files (*.jpg *.png)", options=options)

        self.load_user_image = LoadImage(imagePath)
        self.load_user_image.show()

    def start(self):
        self.start_window.hide()
        self.intro_window.start()