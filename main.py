import PyQt5.QtWidgets as Qtw

class MainApp(Qtw.QWidget):
    def __init__(self, window_title: str, size_w: int, size_h: int):
        """
        Початковий клас. Його ви наслідуєте та доповнюєте.
        :param window_title: Назва нашого вікна.
        :param size_w: Вертикальний розмір вікна.
        :param size_h: Горизонтальний розмір вікна.
        Всередині є два layout.
        v_layout: Це вертикальний.
        h_layout: Це горизонтальний.
        Горизонтальний прикріплений до вертикального.

        .show вже прописано.
        """
        super().__init__()
        # Встановлюємо характеристики нашого вікна.
        self.setWindowTitle(window_title)
        # Створюємо лінії.
        self.v_layout = Qtw.QVBoxLayout()
        self.h_layout = Qtw.QHBoxLayout()
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        # Встановлюємо розмір.
        self.resize(size_w, size_h)

        # Відображаємо вікно.
        self.show()