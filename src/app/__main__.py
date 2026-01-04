from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from src.services.ServerMonitor import ServerMonitor
from src.ui.Dashboard import Dashboard
from src.services.utils import make_tcp_pinger
from pathlib import Path
from src.services.SoundPlayer import SoundPlayer
from src.ui.OledEyes import OledEyes

app = QApplication([])

pinger = make_tcp_pinger("PEMLAND.aternos.me")
monitor = ServerMonitor(pinger)

audio_path = Path(__file__).resolve().parent.parent / "resources" / "aternos.wav"

sound = SoundPlayer(audio_path)
monitor.became_online.connect(sound.play)

dashboard = Dashboard()
monitor.status_changed.connect(dashboard.set_status)

oled_eyes = OledEyes(width=128, height=64, addr=0x3C)

eyes_timer = QTimer()
eyes_timer.setInterval(10)  # call often; RoboEyes throttles internally
eyes_timer.timeout.connect(oled_eyes.tick)
eyes_timer.start()

monitor.became_online.connect(oled_eyes.anim_laugh)
monitor.became_offline.connect(oled_eyes.anim_confused)

timer = QTimer()
timer.setInterval(5_000)
timer.timeout.connect(monitor.tick)
timer.start()

dashboard.showFullScreen()
app.exec()
