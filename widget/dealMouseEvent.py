from PySide6.QtGui import QMouseEvent, Qt


# region 鼠标拖动窗体

def mousePressEvent(widget, event: QMouseEvent) -> None:
    if event.button() == Qt.LeftButton:
        widget.m_drag = True
        widget.xdl = event.globalPosition().toPoint() - widget.pos()
        widget.setCursor(Qt.OpenHandCursor)


def mouseMoveEvent(widget, event: QMouseEvent) -> None:
    if widget.m_drag:
        widget.move(event.globalPosition().toPoint() - widget.xdl)


def mouseReleaseEvent(widget, event: QMouseEvent) -> None:
    if widget.m_drag and event.button() == Qt.LeftButton:
        widget.m_drag = False
        widget.setCursor(Qt.CustomCursor)

# endregion
