from mcstatus import JavaServer
from src.services.utils import make_tcp_pinger


def test_ping_success(monkeypatch):
    class DummyStatus:
        description = "pem!"

    class DummyServer:
        def status(self, timeout=None):
            return DummyStatus()

    def fake_lookup(addr):
        return DummyServer()

    monkeypatch.setattr(JavaServer, "lookup", fake_lookup)

    ping = make_tcp_pinger("example.com", 25565)
    assert ping() is True


def test_ping_failure(monkeypatch):
    def fake_lookup(addr):
        raise Exception("offline")

    monkeypatch.setattr(JavaServer, "lookup", fake_lookup)

    ping = make_tcp_pinger("example.com", 25565)
    assert ping() is False
