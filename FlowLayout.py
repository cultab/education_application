"""Port of the qt6 cpp FlowLayout example."""

from PyQt5.QtCore import QMargins, QPoint, QRect, QSize, Qt
from PyQt5.QtWidgets import (QLayout, QLayoutItem, QSizePolicy, QSpacerItem,
                             QStyle)


class FlowLayout(QLayout):
    """Layout that let's widgets rearrange themselves to fill the available space."""

    def __init__(self, margin=-1, hSpacing=-1, vSpacing=-1, *args, **kwargs):
        """Initialize FlowLayout."""
        super(FlowLayout, self).__init__(*args, **kwargs)

        self.itemList = []
        self.m_hSpace = hSpacing
        self.m_vSpace = vSpacing

        self.setContentsMargins(margin, margin, margin, margin)

    def addItem(self, item: QLayoutItem) -> None:
        """Add an item to the layout."""
        self.itemList.append(item)

    def horizontalSpacing(self):
        """Return horizontal spacing."""
        if self.m_hSpace >= 0:
            return self.m_hSpace
        else:
            return self.smartSpacing(QStyle.PM_LayoutHorizontalSpacing)

    def verticalSpacing(self):
        """Return vertical spacing."""
        if self.m_vSpace >= 0:
            return self.m_vSpace
        else:
            return self.smartSpacing(QStyle.PM_LayoutVerticalSpacing)

    def count(self):
        """Return item count in layout."""
        return len(self.itemList)

    def itemAt(self, index: int) -> QLayoutItem:
        """Return item at index."""
        if self.itemList and index < self.count():
            return self.itemList[index]
        else:
            pass

    def takeAt(self, index: int) -> QLayoutItem:
        """Return and remove item from layout at index."""
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)
        return None

    def expandingDirections(self):
        """Return Qt.Orientations."""
        return Qt.Orientations()

    def hasHeightForWidth(self) -> bool:
        """Has heightForWidth() function."""
        return True

    def heightForWidth(self, width: int) -> int:
        """Get height given width."""
        return self.doLayout(QRect(0, 0, width, 0), True)

    def setGeometry(self, rect: QRect) -> None:
        """Set geometry."""
        super().setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self) -> QSize:
        """Return prefered size of the layout."""
        return self.minimumSize()

    def minimumSize(self) -> QSize:
        """Return minimum size of the layout."""
        size = QSize()
        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        margins = self.contentsMargins()
        size += QSize(margins.left() + margins.right(), margins.top() + margins.bottom())
        return size

    def doLayout(self, rect: QRect, testOnly: bool) -> int:
        """Lay items out."""
        left, top, right, bottom = self.getContentsMargins()
        effectiveRect = rect.adjusted(left, top, -right, -bottom)
        x = effectiveRect.x()
        y = effectiveRect.y()
        lineHeight = 0

        for i, item in enumerate(self.itemList):
            wid = item.widget()
            spaceX = self.horizontalSpacing()
            if spaceX == -1:
                spaceX = wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Horizontal)
            spaceY = self.verticalSpacing()
            if spaceY == -1:
                spaceY = wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Vertical)

            match item:
                case QSpacerItem():
                    # item.setGeometry(QRect(x, y, effectiveRect.x() - x, effectiveRect.y() - y))
                    x = effectiveRect.x()
                    y = y + lineHeight
                    lineHeight = 0
                    continue

            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > effectiveRect.right() and lineHeight > 0:
                x = effectiveRect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                rect = QRect(QPoint(x, y), item.sizeHint())
                item.setGeometry(rect)

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y() + bottom

    def smartSpacing(self, pm: QStyle.PixelMetric) -> int:
        """Calculate spacing?."""
        parent = self.parent()
        if not parent:
            return -1
        elif parent.isWidgetType():
            return parent.style().pixelMetric(pm, None, parent)
        else:
            return parent.spacing()

    def newRow(self):
        """Add a horizontal spacer forcing following widgets to a new row."""
        self.itemList.append(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
