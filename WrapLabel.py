"""QLabel that wraps text."""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QLabel, QStyle, QStyleOption


class WrapLabel(QLabel):
    """QLabel that wraps text by default."""

    def __init__(self, text: str, *args, **kwargs):
        """Initialize WrapLabel."""
        super(WrapLabel, self).__init__(text, *args, **kwargs)

        self.textalignment = Qt.AlignLeft | Qt.TextWrapAnywhere
        self.isTextLabel = True
        self.align = None

    def paintEvent(self, event):
        """Paint."""
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)

        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

        self.style().drawItemText(painter, self.rect(),
                                  self.textalignment, self.palette(), True, self.text())
