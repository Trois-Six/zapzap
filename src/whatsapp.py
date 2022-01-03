from PySide6.QtCore import QUrl
from PySide6.QtWebEngineCore import QWebEnginePage
from app_info import user_agent

# Classe para a página do webapp.
class WhatsApp(QWebEnginePage):
    def __init__(self, *args, **kwargs):
        QWebEnginePage.__init__(self, *args, **kwargs)
        self.featurePermissionRequested.connect(self.permission)

    def permission(self, frame, feature):
        """Permissões para o navegador."""
        self.setFeaturePermission(frame, feature, QWebEnginePage.PermissionGrantedByUser)
