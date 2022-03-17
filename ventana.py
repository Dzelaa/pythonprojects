from ventana_ui import *
import random



def generar_contrasena():
    mayusculas =    ['A', 'V', 'E', 'R', 'T', 'Y', 'N']
    minusculas =    ['a', 'v', 'e', 'r', 't', 'y', 'n']
    simbolos   =    ['¿', '?', '/', '&', '%', '$', '#']
    numeros    =    ['1', '2', '3', '4', '5', '6', '7']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena

def main():
    contrasena = generar_contrasena()
    print('Tu nueva contrasena es: ', contrasena)



global contrasena
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.setText("Generar contraseña")
        self.pushButton.clicked.connect(self.actualizar)

    def actualizar(self):
        self.pushButton.setText(generar_contrasena())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()



