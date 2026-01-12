from mcstatus import JavaServer


def make_tcp_pinger(host, timeout=2.0):
    def _ping():
        try:
            server = JavaServer.lookup(f"{host}")
            status = server.status()

            desc = str(getattr(status, "description", "")).lower()
            if "pem!" in desc:
                return True

            return False
        except Exception as exc:
            print(f"mcstatus failed: {exc!r}")
            return False

    return _ping
