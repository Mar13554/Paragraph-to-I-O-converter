import sys, os, json
from Converter import convert_w
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit

new_file_name = ""

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #Overall layout of window
        self.setGeometry(800, 400, 450, 300)
        self.setWindowTitle("Converter V.0.1")
        layout = QVBoxLayout()

        #User input
        self.text_paragraph = QTextEdit()
        self.text_name = QLineEdit()
        self.text_name.setPlaceholderText("Enter here e.g.: File.json")
        layout.addWidget(self.text_paragraph)
        layout.addWidget(self.text_name)
        #Button
        button = QPushButton("Convert!")
        button.clicked.connect(self.run_main_function)
        layout.addWidget(button)

        self.setLayout(layout)
        self.show()

    def run_main_function(self):
        #Get input
        paragraph = self.text_paragraph.toPlainText()
        #Convert:
        main_dict = convert_w(paragraph)
        #Create file to store:
        new_file_name = self.text_name.text()
        file_path = os.path.join("JSON", new_file_name)
        print(file_path)
        try:
            with open(file_path, "x") as file:
                pass
        except FileExistsError:
            pass
        with open(file_path, "w") as file:
            json.dump(main_dict, file, indent=4)
        #Clear input:
        self.text_paragraph.clear()
        self.text_name.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())