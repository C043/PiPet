from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame
from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("dashboard")

        self.title = QLabel()
        self.title.setTextFormat(Qt.RichText)
        self.title.setText(
            '<img src="./src/resources/raspLogo.png" width="40" style="vertical-align:middle;"> <span style="vertical-align:biddle;">Pet Dashboard</span>'
        )
        self.title.setObjectName("title")

        self.connection_status_pill = QLabel()
        self.connection_status_pill.setFixedSize(14, 14)
        self.connection_status_pill.setObjectName("connectionStatusPill")
        self.connection_status_pill.setAlignment(Qt.AlignCenter)

        title_row = QHBoxLayout()
        title_row.setSpacing(12)
        title_row.addWidget(self.title, alignment=Qt.AlignVCenter)
        title_row.addWidget(self.connection_status_pill, alignment=Qt.AlignVCenter)
        title_row.addStretch()

        self.minecraft_status_pill = QLabel("UNKNOWN")
        self.minecraft_status_pill.setObjectName("minecraftStatusPill")
        self.minecraft_status_pill.setAlignment(Qt.AlignCenter)

        self.minecraft_status_text = QLabel("Server status not checked yet.")
        self.minecraft_status_text.setObjectName("statusText")
        self.minecraft_status_text.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(24)

        layout.addLayout(title_row)
        layout.addWidget(self.minecraft_status_pill)
        layout.addWidget(self.minecraft_status_text)
        layout.addStretch()

        self.setLayout(layout)
        self._apply_style()

        self.net = QNetworkAccessManager(self)
        self.net.finished.connect(self._on_net_check)
        self.net_timer = QTimer(self)
        self.net_timer.setInterval(10000)
        self.net_timer.timeout.connect(self.check_internet)
        self.net_timer.start()

        self.check_internet()

    def check_internet(self):
        req = QNetworkRequest(QUrl("https://client3.google.com/generate_204"))
        req.setHeader(QNetworkRequest.UserAgentHeader, "Dashboard/1.0")
        self.net.get(req)

    def _on_net_check(self, reply):
        online = reply.error() == QNetworkReply.NoError
        reply.deleteLater()

        self.set_connection_status(online)

    def set_minecraft_status(self, is_online: bool):
        if is_online:
            self.minecraft_status_pill.setText("ONLINE")
            self.minecraft_status_pill.setProperty("state", "online")
            self.minecraft_status_text.setText("Minecraft server is online.")
        else:
            self.minecraft_status_pill.setText("OFFLINE")
            self.minecraft_status_pill.setProperty("state", "offline")
            self.minecraft_status_text.setText("Minecraft server is offline.")

        # Re-apply style so QSS updates state
        self.minecraft_status_pill.style().unpolish(self.minecraft_status_pill)
        self.minecraft_status_pill.style().polish(self.minecraft_status_pill)

    def set_connection_status(self, is_online: bool):
        if is_online:
            self.connection_status_pill.setProperty("state", "online")
        else:
            self.connection_status_pill.setProperty("state", "offline")

        # Re-apply style so QSS updates state
        self.connection_status_pill.style().unpolish(self.connection_status_pill)
        self.connection_status_pill.style().polish(self.connection_status_pill)

    def _apply_style(self):
        self.setStyleSheet(
            """
          #dashboard {
              background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                  stop:0 #0f2027, stop:0.5 #203a43, stop:1 #2c5364);
          }
          #title {
              color: #e8f1f2;
              font-size: 36px;
              font-weight: 600;
          }
          #connectionStatusPill {
            border-radius: 7px;
            background: #555;
          }
          #connectionStatusPill[state="online"] {
              background: #2ecc71;
          }
          #connectionStatusPill[state="offline"] {
              background: #e74c3c;
          }
          #minecraftStatusPill {
              color: white;
              font-size: 48px;
              font-weight: 700;
              padding: 20px 40px;
              border-radius: 16px;
              background: #555;
          }
          #minecraftStatusPill[state="online"] {
              background: #2ecc71;
          }
          #minecraftStatusPill[state="offline"] {
              background: #e74c3c;
          }
          #statusText {
              color: #e8f1f2;
              font-size: 24px;
          }
          """
        )
