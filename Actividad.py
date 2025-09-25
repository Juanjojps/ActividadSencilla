import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from ui_actividad import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        self.setupUi(self)
        self.Cambiar.clicked.connect(self.on_cambiar)

        print("Funcionando")


    def on_cambiar(self):
        self.label_principal.setText("Texto cambiado")
        print("Se ha cambiado el texto")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    app.exec()