
from playFairCipher import PlayFairCipher
from PyQt5 import QtWidgets, uic

ENCRYPT_OPTION = 'Encrypt'
DECRYPT_OPTION = 'Decrypt'

TEXT_OPTION = 'Text'
FILE_OPTION = 'File'

MAX_LINE_LEN = 30

class Gui(object):
    
    def __init__(self) -> None:
        self.app            = QtWidgets.QApplication([]) 
        self.window         = QtWidgets.QMainWindow()
        self.messageBox     = QtWidgets.QMessageBox()

        self.playFairCipher = PlayFairCipher()

        self.results: str = ''
        self.setup()

    def setup(self) -> None:
        self.app.aboutToQuit.connect(self.quit)
        uic.loadUi('mainWindow.ui', self.window)

        self.window.types.addItems([ENCRYPT_OPTION, DECRYPT_OPTION])
        self.window.inputTypes.addItems([TEXT_OPTION, FILE_OPTION])

        self.window.executeButton.clicked.connect(self.execute)
        self.window.saveToFileButton.clicked.connect(self.save)
        self.window.inputDataFormatInfo.triggered.connect(self.displayInfo)

        self.window.show()

    def displayInfo(self):
        self.messageBox.about(
            self.messageBox, 'Input Format',
            'Input text can contain letters from the English alphabet, spaces, dots, commas, '
            'semicolons, and colons.\n\n'
            'Password can contain only letters.'
        )

    def execute(self) -> None:
        text = ''
        if self.window.inputTypes.currentText() == FILE_OPTION:
            filePath = self.window.inputTextField.toPlainText()
            try:
                f = open(filePath, 'r')
                for line in f:
                    text += line.strip() + ' '
                text = text[:-1]
                f.close()
                self.window.inputTextField.setPlainText(text)
            except FileNotFoundError:
                self.messageBox.about(
                    self.messageBox, 'Error',
                    'File was not found.'
                )
                return
        else:
            text = self.window.inputTextField.toPlainText().split('\n')
            text = ' '.join(text)
        
        if not self.playFairCipher.validateText(text):
            self.messageBox.about(
                self.messageBox, 'Error',
                'Input text contains prohibited characters.\n'
                'See the \'Help\' section for more information.'
            )
            return
        
        password = self.window.inputPasswordField.text()
        if not self.playFairCipher.validatePassword(password):
            self.messageBox.about(
                self.messageBox, 'Error',
                'The password contains prohibited characters.\n'
                'See the \'Help\' section for more information.'
            )
            return

        if self.window.types.currentText() == ENCRYPT_OPTION:
            self.results = self.playFairCipher.encipher(text, password)
        else:
            self.results = self.playFairCipher.decipher(text, password)
        self.window.outputTextField.setPlainText(self.results)

    def save(self) -> None:
        filePath = self.window.saveToFileField.text()
        try:
            f = open(filePath, 'w')
            results = self.results.split()
            lineLen = 0
            for el in results:
                if lineLen + len(el) < MAX_LINE_LEN or len(el) > MAX_LINE_LEN:
                    f.write(el + ' ')
                    lineLen += len(el)
                else:
                    f.write('\n' + el + ' ')
                    lineLen = len(el)
            f.close()
            self.messageBox.about(
                self.messageBox, 'Success', 
                'Results saved successfully.'
            )
        except:
            self.messageBox.about(
                self.messageBox, 'Error',
                'Unable to open the result file.'
            )

    def quit(self) -> None:
        self.window.close()