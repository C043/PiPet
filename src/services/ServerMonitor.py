from PySide6.QtCore import QObject, Signal


class ServerMonitor(QObject):
    status_changed = Signal(bool)
    became_online = Signal()
    became_offline = Signal()

    def __init__(self, pinger):
        super().__init__()
        self.pinger = pinger
        self.is_online = None

    def tick(self):
        current = self.pinger()

        if self.is_online is None:
            self.is_online = current
            self.status_changed.emit(current)
            return

        if current != self.is_online:
            if self.is_online is False and current is True:
                self.became_online.emit()
            elif self.is_online is True and current is False:
                self.became_offline.emit()
            self.is_online = current
            self.status_changed.emit(current)
