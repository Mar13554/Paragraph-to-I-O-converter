import sys, os, json
from Converter import convert_w, convert_s
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit

new_file_name = ""
string_options = ["Change to sentence-to-sentence", "Change to one-to-one"]
setting_value = 0 #Default one-to-one

def value_change():
if setting_value == 0:
    return 1
else:
    return 0

class MyApp(QWidget):
def __init__(self):
    super().__init__()
    self.initUI()

def initUI(self):
    #Overall layout of window
    self.setGeometry(800, 400, 450, 300)
    self.setWindowTitle("Converter V.0.2")
    layout = QVBoxLayout()

    #User input
    self.text_paragraph = QTextEdit()
    self.text_name = QLineEdit()
    self.text_name.setPlaceholderText("Enter here e.g.: File.json")
    layout.addWidget(self.text_paragraph)
    layout.addWidget(self.text_name)

    #Button for setting
    self.button_setting = QPushButton(string_options[setting_value])
    self.button_setting.clicked.connect(self.change_value)
    layout.addWidget(self.button_setting)

    #Button to convert
    button = QPushButton("Convert!")
    button.clicked.connect(self.run_main_function)
    layout.addWidget(button)

    self.setLayout(layout)
    self.show()

def change_value(self):
    global setting_value
    setting_value = value_change()
    self.button_setting.setText(string_options[setting_value])
    print(f"Changed setting {setting_value}")

def run_main_function(self):
    global new_file_name
    #Check file
    new_file_name = self.text_name.text()
    file_path = os.path.join("JSON", new_file_name)
    try:
        with open(file_path, "x") as file:
            current_paragraph_amount = 1
            file_exists = False
    except FileExistsError:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                current_paragraph_amount = len(data)+1
                file_exists = True
        except Exception:
            print("Error with handling null in file")
    #Get input
    paragraph = self.text_paragraph.toPlainText()
    #Convert:
    if setting_value == 0:
        main_dict = convert_w(paragraph, current_paragraph_amount)
    else:
        main_dict = convert_s(paragraph, current_paragraph_amount)

    #Create file to store or update:
    print(file_path)
    if file_exists:
        data.update(main_dict)
    else:
        data = main_dict
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    #Clear input:
    self.text_paragraph.clear()


if __name__ == '__main__':
app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())
