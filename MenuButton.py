"""A big button that expands to fill all available space."""

from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QPushButton, QSizePolicy


class MenuButton(QPushButton):
    """A big button that expands to fill all available space."""

    def __init__(self: QPushButton, text: str, object_name: str = None) -> None:
        """Initialize a MenuButton.

        text: the button's label
        object_name: (optional) an object name
        """
        super(MenuButton, self).__init__(text)

        # shadow = QGraphicsDropShadowEffect()
        # shadow.setBlurRadius(15)
        # self.setGraphicsEffect(shadow)
        if object_name:
            self.setObjectName(object_name)
        self.setFlat(True)
        self.setAutoFillBackground(True)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
