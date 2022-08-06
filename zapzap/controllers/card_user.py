from PyQt6.QtWidgets import QWidget, QApplication
from zapzap.model.user import UserDAO
from zapzap.theme.builder_icon import getImageQPixmap
from zapzap.theme.icons import IMAGE_DISABLE
from zapzap.view.card_user import Ui_CardUser

from gettext import gettext as _


class CardUser(QWidget, Ui_CardUser):
    def __init__(self, parent=None, user=None):
        super(CardUser, self).__init__()
        self.setupUi(self)
        self.user = user

        if self.user.id == 1:  # user default
            self.btnDisable.hide()
            self.btnDelete.hide()
        else:
            self.btnDisable.clicked.connect(self.buttonClick)
            self.btnDelete.clicked.connect(self.buttonClick)

        self.load()

    def load(self):
        self.id.setText('#'+str(self.user.id))
        self.name.setText(self.user.name)
        svg = self.user.icon
        if self.user.enable:
            self.btnDisable.setText(_("Disable"))
        else:
            self.btnDisable.setText(_("Enable"))
            svg = svg.format(IMAGE_DISABLE)
        self.icon.setPixmap(getImageQPixmap(svg))

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()
        mainWindow = QApplication.instance().getWindow()

        if btnName == 'btnDisable':
            self.user.enable = not self.user.enable
            UserDAO.update(self.user)
            mainWindow.emitDisableUser(self.user)
            self.load()
        if btnName == 'btnDelete':
            UserDAO.delete(self.user.id)
            mainWindow.emitDeleteUser(self.user)
            self.close()
