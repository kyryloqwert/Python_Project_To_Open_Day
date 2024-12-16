import string
import random
from main import *

class FirstApp(MainApp):
    def __init__(self, window_title: str, size_w: int, size_h: int):
        super().__init__(window_title, size_w, size_h)

        # Встановлюю зовнішній вигляд вікна.
        self.setStyleSheet("""
                    QWidget {
                        background-color: #4B0082;  /* Колір фону */
                        border: 0px solid #800080;   /* Колір і товщина рамки */
                        border-radius: 25px;           /* Закруглення кутів рамки */
                    }
                    QLabel {
                        color: white;  /* Колір тексту для QLabel */
                        font-size: 16px; /* Розмір шрифту для мітки */
                    }
                    QLineEdit {
                        color: yellow;  /* Колір тексту в полі введення */
                        background-color: black;  /* Колір фону поля введення */
                        border-radius: 5px;  /* Закруглення кутів */
                        padding: 5px;  /* Відступи */
                    }
                    QPushButton {
                        background-color: #800080;  /* Колір фону кнопки */
                        color: white;  /* Колір тексту на кнопці */
                        border-radius: 5px;  /* Закруглення кутів кнопки */
                        padding: 5px 15px;  /* Відступи всередині кнопки */
                    }
                    QPushButton:hover {
                        background-color: #9932CC;  /* Колір кнопки при наведенні */
                    }
                """)

        # Створюю генератор пароля.

        # Створюю ще один горизонтальний layout для введення довжини пароля.
        self.h_layout2 = Qtw.QHBoxLayout()
        self.v_layout.addLayout(self.h_layout2)

        # Створюю напис для поля введення довжини пароля.
        label_len = Qtw.QLabel('Довжина пароля: ')
        self.h_layout2.addWidget(label_len)

        # Створюю текстове поле для введення довжини пароля.
        self.len_field = Qtw.QLineEdit()
        self.len_field.setText('0')
        self.h_layout2.addWidget(self.len_field)

        # Створюю напис для відображення згенерованого пароля.
        out_label = Qtw.QLabel('Ваш пароль: ')
        self.h_layout.addWidget(out_label)

        # Створюю поле для відображення згенерованого пароля.
        self.password_display = Qtw.QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setText('Your password')
        self.h_layout.addWidget(self.password_display)

        # Створюю кнопку для генерації пароля.
        botton_generation = Qtw.QPushButton('Generate')
        botton_generation.clicked.connect(self.generation_password)
        self.h_layout.addWidget(botton_generation)

    def generation_password(self):
        # Отримую довжину пароля з текстового поля.
        length = int(self.len_field.text())
        letter = string.ascii_uppercase
        digits = string.digits
        password_template = letter + digits
        password = ''

        # Перевірка довжини пароля і генерація.
        match length:
            case 0:
                self.password_display.setText('No length')
                return
            case _:
                for _ in range(0, length):
                    password += random.choice(password_template)

        # Встановлюю згенерований пароль в поле для відображення.
        self.password_display.setText(password)

if __name__ == '__main__':
    # Створюю і запускаю додаток.
    app = Qtw.QApplication([])
    window_one = FirstApp('Password Generation', 400, 50)
    app.exec_()