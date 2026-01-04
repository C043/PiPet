from src.services.ServerMonitor import ServerMonitor


def test_sound_triggers_on_online(qtbot, mocker):
    pinger = lambda: False
    monitor = ServerMonitor(pinger)

    sound = mocker.Mock()

    monitor.became_online.connect(sound.play)

    monitor.tick()
    monitor.pinger = lambda: True
    monitor.tick()

    sound.play.assert_called_once()
