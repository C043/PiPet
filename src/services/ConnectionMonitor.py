from PySide6.QtCore import QObject, QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest


class ConnectionMonitor(QObject):
    def __init__(self):
        super().__init__()
        self.net = QNetworkAccessManager(self)

    def check_internet(self):
        req = QNetworkRequest(QUrl("https://client3.google.com/generate_204"))
        req.setHeader(QNetworkRequest.UserAgentHeader, "Dashboard/1.0")
        self.net.get(req)
