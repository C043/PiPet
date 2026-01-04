from ui.Dashboard import Dashboard


def test_dashboard_updates_status(qtbot):
    widget = Dashboard()
    qtbot.addWidget(widget)

    widget.set_status(True)
    assert widget.status_pill.text() == "ONLINE"
    assert "online" in widget.status_pill.property("state")

    widget.set_status(False)
    assert widget.status_pill.text() == "OFFLINE"
    assert "offline" in widget.status_pill.property("state")
