from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/home.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(986, 666)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Home)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menuUsers = QtWidgets.QFrame(parent=Home)
        self.menuUsers.setMinimumSize(QtCore.QSize(40, 0))
        self.menuUsers.setMaximumSize(QtCore.QSize(30, 16777215))
        self.menuUsers.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.menuUsers.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menuUsers.setObjectName("menuUsers")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menuUsers)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu = QtWidgets.QVBoxLayout()
        self.menu.setSpacing(8)
        self.menu.setObjectName("menu")
        self.verticalLayout.addLayout(self.menu)
        self.horizontalLayout.addWidget(self.menuUsers)
        self.userStacked = QtWidgets.QStackedWidget(parent=Home)
        self.userStacked.setObjectName("userStacked")
        self.horizontalLayout.addWidget(self.userStacked)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        
        Home.setWindowTitle(_("Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Home = QtWidgets.QWidget()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec())
