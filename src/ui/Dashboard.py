from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTime, Qt
from PySide6.QtNetwork import QNetworkReply


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("dashboard")

        self.title_icon = QLabel()
        pixmap = QPixmap("./src/resources/raspLogo.png")
        self.title_icon.setPixmap(pixmap.scaledToWidth(40, Qt.SmoothTransformation))

        self.title_text = QLabel("Pet Dashboard")
        self.title_text.setObjectName("title")

        self.connection_status_pill = QLabel()
        self.connection_status_pill.setFixedSize(14, 14)
        self.connection_status_pill.setObjectName("connectionStatusPill")
        self.connection_status_pill.setAlignment(Qt.AlignCenter)

        self.current_time = QLabel()
        self.current_time.setWindowTitle("Current Time")
        self.current_time.setObjectName("currentTime")
        self.current_time.show()

        title_row = QHBoxLayout()
        title_row.setSpacing(8)
        title_row.addWidget(self.title_icon, alignment=Qt.AlignVCenter)
        title_row.addWidget(self.title_text, alignment=Qt.AlignVCenter)
        title_row.addWidget(self.connection_status_pill, alignment=Qt.AlignVCenter)

        title_row.addStretch(1)
        title_row.addWidget(
            self.current_time, alignment=Qt.AlignVCenter | Qt.AlignRight
        )

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

    def set_connection_status(self, reply):
        is_online = reply.error() == QNetworkReply.NoError
        reply.deleteLater()

        if is_online:
            self.connection_status_pill.setProperty("state", "online")
        else:
            self.connection_status_pill.setProperty("state", "offline")

        # Re-apply style so QSS updates state
        self.connection_status_pill.style().unpolish(self.connection_status_pill)
        self.connection_status_pill.style().polish(self.connection_status_pill)

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

    def update_time(self):
        self.current_time.setText(QTime.currentTime().toString("HH:mm:ss"))

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
          #currentTime {
              color: #e8f1f2;
              font-size: 36px;
              font-weight: 600;
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
