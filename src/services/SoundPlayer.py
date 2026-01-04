from pathlib import Path
from PySide6.QtCore import QObject, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput


class SoundPlayer(QObject):
    def __init__(self, audio_path: Path):
        super().__init__()
        self._player = QMediaPlayer(self)
        self._audio = QAudioOutput(self)
        self._player.setAudioOutput(self._audio)
        self._player.setSource(QUrl.fromLocalFile(str(audio_path)))

    def play(self):
        self._player.setPosition(0)
        self._player.play()
