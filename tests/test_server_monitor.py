from src.services.ServerMonitor import ServerMonitor
from PySide6.QtTest import QSignalSpy


def test_online_transition_triggers_alert(mocker):
    monitor = ServerMonitor(pinger=lambda: False)
    monitor.tick()
    assert monitor.is_online is False

    monitor.pinger = lambda: True
    spy = QSignalSpy(monitor.became_online)
    monitor.tick()
    assert spy.count() == 1
