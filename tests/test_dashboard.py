from ui.Dashboard import Dashboard


def test_dashboard_updates_status(qtbot):
    widget = Dashboard()
    qtbot.addWidget(widget)

    widget.set_minecraft_status(True)
    assert widget.minecraft_status_pill.text() == "ONLINE"
    assert "online" in widget.minecraft_status_pill.property("state")

    widget.set_minecraft_status(False)
    assert widget.minecraft_status_pill.text() == "OFFLINE"
    assert "offline" in widget.minecraft_status_pill.property("state")
