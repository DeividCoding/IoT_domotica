from PyQt5.QtWidgets import  QDialog,QApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from  CUERPO.DISENO.configVenti_dise import Ui_Dialog
###############################################################
#  MIS LIBRERIAS...
##############################################################


class Dialog_configVenti(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        Ui_Dialog.__init__(self)
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        self.setWindowTitle(" ")
        self.setWindowModality(Qt.ApplicationModal)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Dialog_configVenti()
    application.show()
    app.exec()
    #sys.exit(app.exec())
