import string
import random
from main import *  # Assuming MainApp is imported from your main module

class FirstApp(MainApp):
    def __init__(self, window_title: str, size_w: int, size_h: int):
        super().__init__(window_title, size_w, size_h)

        # Set the window style with a pink background
        self.setStyleSheet("""
                    QWidget {
                        background-color: #FFC0CB;  /* Set background color to pink */
                        border: 0px solid #800080;
                        border-radius: 25px;
                    }
                    QLabel {
                        color: white;
                        font-size: 16px;
                    }
                    QLineEdit {
                        color: yellow;
                        background-color: black;
                        border-radius: 5px;
                        padding: 5px;
                    }
                    QPushButton {
                        background-color: #800080;
                        color: white;
                        border-radius: 5px;
                        padding: 5px 15px;
                    }
                    QPushButton:hover {
                        background-color: #9932CC;
                    }
             """)

        # Create layout for password generation UI
        self.h_layout2 = Qtw.QHBoxLayout()
        self.v_layout.addLayout(self.h_layout2)

        # Label for password length input
        label_len = Qtw.QLabel('Довжина пароля: ')
        self.h_layout2.addWidget(label_len)

        # Field for password length
        self.len_field = Qtw.QLineEdit()
        self.len_field.setText('0')
        self.h_layout2.addWidget(self.len_field)

        # Checkbox to include digits
        self.include_digits_checkbox = Qtw.QCheckBox('Include digits')
        self.h_layout2.addWidget(self.include_digits_checkbox)

        # Adjust spacing between elements in the layout to bring them closer together
        self.h_layout2.setSpacing(5)  # Set smaller spacing between widgets
        self.h_layout2.setContentsMargins(10, 10, 10, 10)  # Adjust margins for tighter layout

        # Create a new horizontal layout for the output section
        self.h_layout = Qtw.QHBoxLayout()
        self.v_layout.addLayout(self.h_layout)

        # Label for generated password
        out_label = Qtw.QLabel('Ваш пароль: ')
        self.h_layout.addWidget(out_label)

        # Field for displaying generated password
        self.password_display = Qtw.QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setText('Your password')
        self.h_layout.addWidget(self.password_display)

        # Button to generate password
        button_generation = Qtw.QPushButton('Generate')
        button_generation.clicked.connect(self.generation_password)
        self.h_layout.addWidget(button_generation)

    def generation_password(self):
        # Get password length from the text field
        length = int(self.len_field.text())

        # Default character set: uppercase letters
        letter = string.ascii_uppercase

        # If the checkbox is checked, include digits in the password
        if self.include_digits_checkbox.isChecked():
            password_template = letter + string.digits
        else:
            password_template = letter

        password = ''

        # Check password length and generate password
        if length == 0:
            self.password_display.setText('No length')
            return

        for _ in range(length):
            password += random.choice(password_template)

        # Set the generated password in the display field
        self.password_display.setText(password)


if __name__ == '__main__':
    # Create and run the app
    app = Qtw.QApplication([])
    window_one = FirstApp('Password Generation', 400, 50)
    app.exec_()
