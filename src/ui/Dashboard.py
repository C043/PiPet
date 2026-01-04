from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame
from PySide6.QtCore import Qt


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("dashboard")

        self.title = QLabel("Desk Pet Dashboard")
        self.title.setObjectName("title")

        self.status_pill = QLabel("UNKNOWN")
        self.status_pill.setObjectName("statusPill")
        self.status_pill.setAlignment(Qt.AlignCenter)

        self.status_text = QLabel("Server status not checked yet.")
        self.status_text.setObjectName("statusText")
        self.status_text.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(24)

        layout.addWidget(self.title)
        layout.addWidget(self.status_pill)
        layout.addWidget(self.status_text)
        layout.addStretch()

        self.setLayout(layout)
        self._apply_style()

    def set_status(self, is_online: bool):
        if is_online:
            self.status_pill.setText("ONLINE")
            self.status_pill.setProperty("state", "online")
            self.status_text.setText("Minecraft server is online.")
        else:
            self.status_pill.setText("OFFLINE")
            self.status_pill.setProperty("state", "offline")
            self.status_text.setText("Minecraft server is offline.")

        # Re-apply style so QSS updates state
        self.status_pill.style().unpolish(self.status_pill)
        self.status_pill.style().polish(self.status_pill)

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
          #statusPill {
              color: white;
              font-size: 48px;
              font-weight: 700;
              padding: 20px 40px;
              border-radius: 16px;
              background: #555;
          }
          #statusPill[state="online"] {
              background: #2ecc71;
          }
          #statusPill[state="offline"] {
              background: #e74c3c;
          }
          #statusText {
              color: #e8f1f2;
              font-size: 24px;
          }
          """
        )
