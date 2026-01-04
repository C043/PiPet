from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from services.ServerMonitor import ServerMonitor
from ui.Dashboard import Dashboard
from src.services.utils import make_tcp_pinger

app = QApplication([])

pinger = make_tcp_pinger("PEMLAND.aternos.me")
monitor = ServerMonitor(pinger)

dashboard = Dashboard()
monitor.status_changed.connect(dashboard.set_status)

timer = QTimer()
timer.setInterval(5_000)
timer.timeout.connect(monitor.tick)
timer.start()


dashboard.showFullScreen()
app.exec()
