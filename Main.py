#Main.py By Johnelaidi581

import os
import sys
import qrcode
from notify import notification
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton


class QRCodeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QR Code Generator')
        self.setGeometry(100, 100, 300, 200)

        main_layout = QVBoxLayout()

        self.input_label = QLabel('Enter text:')
        self.input_field = QLineEdit()
        self.generate_button = QPushButton('Generate QR Code')
        self.qr_label = QLabel()

        main_layout.addWidget(self.input_label)
        main_layout.addWidget(self.input_field)
        main_layout.addWidget(self.generate_button)
        main_layout.addWidget(self.qr_label)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.generate_button.clicked.connect(self.generate_qr_code)

    def generate_qr_code(self):
        text = self.input_field.text()
        if not text:
            return

        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(text)
        qr.make(fit=True)

        image = qr.make_image(fill_color='black', back_color='white')
        image.save('QrCode.png')
        os.system('mv QrCode.png ~/Desktop')
        notification('Qr Generator', message='Check your destop', app_name='myapp')

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QRCodeApp()
    window.show()
    sys.exit(app.exec_())

