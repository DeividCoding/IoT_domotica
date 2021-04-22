from PyQt5.QtWidgets import  QDialog,QApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from functools import partial
from PyQt5.QtCore import Qt, pyqtSignal,QObject
###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from  CUERPO.DISENO.SISTEMA_CONTROL.configLed_dise import Ui_Dialog
###############################################################
#  MIS LIBRERIAS...
##############################################################


class Dialog_configLed(QtWidgets.QDialog, Ui_Dialog):
    senal_colorElegido= pyqtSignal(list)

    COLORES_RGB=( 
    "(255,255,255)",#blanco
    "(255,0,0)",#rojo
    "(0,255,0)",#verde
    "(0,0,255)",#azul
    "(255,255,0)",#amarillo
    "(255,0,255)",#magenta
    "(0,255,255)"#cian
    )

    def __init__(self):
        Ui_Dialog.__init__(self)
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        self.setWindowTitle(" ")
        self.setWindowModality(Qt.ApplicationModal)

        self.tuplaBotones=(self.btn_0,self.btn_1,self.btn_2,self.btn_3,self.btn_4,self.btn_5,self.btn_6)
        for n in range(len(self.tuplaBotones)):
            self.tuplaBotones[n].clicked.connect(partial(self.eligioColor,n))
        
    
    def eligioColor(self,idColor):
        #CONVENCIO DE COLORES USADAS EN ARDUINO...
        # 0-blanco
        # 1-rojo
        # 2-verde
        # 3-azul
        # 4-amarillo
        # 5-magenta
        # 6-cian

        listDatos=[idColor,self.COLORES_RGB[idColor]]
        self.senal_colorElegido.emit(listDatos)
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Dialog_configLed()
    application.show()
    app.exec()
    #sys.exit(app.exec())