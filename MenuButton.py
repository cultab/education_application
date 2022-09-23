
from PyQt5.QtWidgets import QPushButton, QSizePolicy

class MenuButton(QPushButton):

    def __init__(self: QPushButton, text: str, object_name: str = None) -> None:
        super(MenuButton, self).__init__(text)
        if object_name:
            self.setObjectName(object_name)
        self.setFlat(True)
        self.setAutoFillBackground(True)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
