
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication,QSpinBox,QActionGroup,QLabel,QWidget,QPushButton, QVBoxLayout,QScrollArea,QMessageBox
from PyQt5.QtGui import QIcon,QFont

from PyQt5.Qt import QSizePolicy,Qt
from PyQt5 import QtCore




###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################


###############################################################
#  MIS LIBRERIAS...
##############################################################
from CUERPO.LOGICA.DEBERES.itemDeber import ItemDeber
from recursos import App_Notas,HuellaAplicacion
import IMAG_rc



class SeccionNotas(QMainWindow,HuellaAplicacion):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

        HuellaAplicacion.__init__(self)


    def initUI(self):

        self.ESTADO_ALINEO=0   #0=IZQUIERDA, 1=CENTRO, 2=DERECHA
        self.TAMANO_LETRA=12

        self.MAX_ITEMS=20
        self.punteroNoItems=0
        self.contadorIdsVivosMuertos = 0



        #self.btn_agregarItem.clicked.connect(partial(self.agregarAlarma,Alarma()))
        self.listaItemsRonianos=[]
        self.textPregunta=""
        self.listIdsItemsVivos=[]
        self.listPunterosItems=[]
        self.siguienteItemEliminar=None
        


        #Creando las accciones que ayudaran a alinear el texto
        #border-image: url();
        self.alineacion_izquierda = QAction(QIcon(":/DEBERES/IMAGENES/DEBERES/izquierda.png"), 'Izquierda', self)
        self.alineacion_centro= QAction(QIcon(":/DEBERES/IMAGENES/DEBERES/centrado.png"), 'Centrado', self)
        self.alineacion_derecha= QAction(QIcon(":/DEBERES/IMAGENES/DEBERES/derecha.png"), 'Derecha', self)

        #habilitandolos para que puedan ser seleccionados
        self.alineacion_izquierda.setCheckable(True)
        self.alineacion_centro.setCheckable(True)
        self.alineacion_derecha.setCheckable(True)

        #Agrupando ciertas acciones para unicamente permitir la seleccion de una de ellas
        self.grupo_alineadores = QActionGroup(self)
        self.grupo_alineadores.addAction(self.alineacion_izquierda)
        self.grupo_alineadores.addAction(self.alineacion_centro)
        self.grupo_alineadores.addAction(self.alineacion_derecha)
  

        #exitAct.setShortcut('Ctrl+Q')
        #exitAct.setStatusTip('Exit application')
        #exitAct.triggered.connect(self.close)
        #QtCore.Qt.LeftToolBarArea
        self.statusBar() 
        toolbar = self.addToolBar('Edicion')
        self.addToolBar(QtCore.Qt.BottomToolBarArea,toolbar)
        toolbar.setStyleSheet("QToolButton:checked {background-color:#94DCD3; border:none; } ")
        toolbar.setMovable(False)
        toolbar.setOrientation(QtCore.Qt.Horizontal)

        toolbar.addWidget(self.get_expansorWidget() )    
        toolbar.addAction(self.alineacion_izquierda)
        toolbar.addSeparator()
        toolbar.addWidget( self.get_separadorQAction() )

        toolbar.addAction(self.alineacion_centro)
        toolbar.addSeparator()
        toolbar.addWidget( self.get_separadorQAction() )

        toolbar.addAction(self.alineacion_derecha)
        toolbar.addSeparator()
        toolbar.addWidget( self.get_separadorQAction() )

        self.spinBox_tam= QSpinBox()
        toolbar.addWidget(self.spinBox_tam)
        self.spinBox_tam.setMinimumSize(60,30)
        self.spinBox_tam.setFont(QFont('Arial', 12))
        toolbar.addWidget( self.get_separadorQAction() )


        #toolbar.addWidget(self.get_expansorWidget() )  
        self.btnAgregarItem=QPushButton()
        self.btnAgregarItem.setStyleSheet("""
            QPushButton {
               	border-image: url(:/ALARMA/IMAGENES/ALARMA/plus_off.png);
            }
            QPushButton:hover {
               	border-image: url(:/ALARMA/IMAGENES/ALARMA/plus_on.png);
            }
            QPushButton:pressed {
                border-image: url(:/ALARMA/IMAGENES/ALARMA/plus_off.png);
            }   
        """)
        self.btnAgregarItem.setMinimumSize(30,30)
        toolbar.addWidget(self.btnAgregarItem)
        toolbar.addWidget( self.get_separadorQAction() )



        #toolbar.addWidget(self.get_expansorWidget() )  

        self.setGeometry(300, 300, 350, 250)
        #self.setWindowTitle('Main window')
        self.show()



        

        # adding triggered action to the first action
        self.alineacion_derecha.triggered.connect( lambda x : self.alinear(2) )
        self.alineacion_centro.triggered.connect( lambda x : self.alinear(1)  )
        self.alineacion_izquierda.triggered.connect(lambda x : self.alinear(0)  )


        self.btnAgregarItem.clicked.connect(lambda : self.agregarNuevoItem("") )

        self.spinBox_tam.valueChanged.connect(self.cambiarTamano_letra)


        self.scroll = QScrollArea()     # Scroll Area which contains the widgets, set as the centralWidget
        self.scroll.setStyleSheet("""
                            *{
                            border:none;
                            background:#FFFFFF;
                            }
                            QScrollArea{
                                border-radius:20%;
                                padding:10px;
                                margin-bottom:15px;
                            }
                            QScrollBar{
                            background : rgb(170, 255, 255);
                            }
                            QScrollBar::handle{
                            background :#979797;
                            }
                            QScrollBar::handle::pressed{
                            background :  #193b58;
                            }
        """) #sin borde
        self.widget = QWidget()         # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()       # The Vertical Box that contains the Horizontal Boxes of  labels and buttons


        #self.vbox.addWidget(object)
        
        
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)


        self.spinBox_tam.setValue(self.TAMANO_LETRA)
        self.spinBox_tam.setMinimum(10)
        self.spinBox_tam.setMaximum(25)
        toolbar.setContentsMargins(0,5,0,0) #arriba,abajo,izquierda,derecha

        self.cargarDeberes()

        
    

    def alinear(self,idAlineo):
        self.ESTADO_ALINEO=idAlineo
        layout=self.vbox
        for noItem in range( self.punteroNoItems ):        
            widget = layout.itemAt(noItem).widget()
            widget.alinear(self.ESTADO_ALINEO)        
                
    def cargarDeberes(self):
        datos=""
        try:
            with open(App_Notas.ARCHIVO_DEBERES,'r') as archivoDeberes:
                datos=archivoDeberes.read()
        except FileNotFoundError:
            pass
        listaDeberes=datos.split(App_Notas.SEPARADOR_DEBERES)
        confiConArchivo_exitosa=False
        if len(listaDeberes)>1 and type(listaDeberes)==list:
            try:
                self.ESTADO_ALINEO,self.TAMANO_LETRA=[ int(x) for x in listaDeberes[0].split(",")  ]
                if self.ESTADO_ALINEO==0: 
                    self.alineacion_izquierda.trigger()
                elif self.ESTADO_ALINEO==1:
                    self.alineacion_centro.trigger()
                elif self.ESTADO_ALINEO==2:
                    self.alineacion_derecha.trigger()

                for textoDeber in listaDeberes[1:]:
                    self.agregarNuevoItem(textoDeber)
                confiConArchivo_exitosa=True
            except:
                pass
        if not(confiConArchivo_exitosa):
            self.alineacion_izquierda.trigger()            
            self.ESTADO_ALINEO=0   #0=IZQUIERDA, 1=CENTRO, 2=DERECHA
            self.TAMANO_LETRA=12



    def respaldarDeberes(self):
        listaDeberes=[]
        listaDeberes.append( str(self.ESTADO_ALINEO)+","+str(self.TAMANO_LETRA)  )
        layout=self.vbox
        for noItem in range( self.punteroNoItems ):        
            widget = layout.itemAt(noItem).widget()
            listaDeberes.append( widget.lineEdit_deber.text() )        
                
        contenidoArchivo=App_Notas.SEPARADOR_DEBERES.join(listaDeberes)

        with open(App_Notas.ARCHIVO_DEBERES,'w') as archivoDeberes:
            archivoDeberes.write(contenidoArchivo)

    def agregarNuevoItem(self,textoDeber):
        if self.punteroNoItems<self.MAX_ITEMS:
            itemDeber=ItemDeber(id=self.contadorIdsVivosMuertos,texto=textoDeber,idAlineacion=self.ESTADO_ALINEO,
            tamanoLetra=self.TAMANO_LETRA)
            itemDeber.senal_deberCumplido.connect(self.borrarItem)

            self.listIdsItemsVivos.append(self.contadorIdsVivosMuertos)
            self.vbox.addWidget(itemDeber)
            self.listPunterosItems.append(itemDeber)
            self.punteroNoItems+=1
            self.contadorIdsVivosMuertos+=1

        else:
            mensaje="El numero maximo numero de notas que\n"
            mensaje+=f"puedes registrar es de: {self.MAX_ITEMS} notas\n"  
            mensaje+=f"y usted ya ha creado {self.MAX_ITEMS} notas."
            ventanaDialogo = QMessageBox()
            ventanaDialogo.setIcon(QMessageBox.Information)
            ventanaDialogo.setWindowIcon( QIcon(self.ICONO_APLICACION)  )
            ventanaDialogo.setWindowTitle(self.NOMBRE_APLICACION)


            ventanaDialogo.setText(mensaje)
            ventanaDialogo.setStandardButtons(QMessageBox.Ok)
            btn_ok = ventanaDialogo.button(QMessageBox.Ok)
            btn_ok.setText('Entendido')
            ventanaDialogo.exec_()

    def borrarItem(self,id):
        idItemAMatar=id

        posItemMatar=self.listIdsItemsVivos.index(idItemAMatar)
        layout=self.vbox
        noWidgetBorrar=posItemMatar
        widgetToRemove = layout.itemAt(noWidgetBorrar).widget()
        # remove it from the layout list
        layout.removeWidget(widgetToRemove)
        # remove it from the gui
        widgetToRemove.setParent(None)
        self.listIdsItemsVivos.pop(posItemMatar)

        if self.siguienteItemEliminar!=None:
            print("Muerte ha*************************************************************",self.siguienteItemEliminar)
            print("Sentencia para********************************************************",posItemMatar)
            self.listPunterosItems.pop(self.siguienteItemEliminar)
            self.siguienteItemEliminar=posItemMatar
        else:
            print("Setencia para**************************************************************",posItemMatar)
            self.siguienteItemEliminar=posItemMatar

        self.punteroNoItems -= 1

    def get_separadorQAction(self):
        separadorQAction=QLabel()
        separadorQAction.setMinimumSize(10,2)
        return separadorQAction

    def get_expansorWidget(self):
        expansorWidget=QWidget()
        expansorWidget.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        return expansorWidget

    def cambiarTamano_letra(self,nuevoValor):
        self.TAMANO_LETRA=nuevoValor
        layout=self.vbox
        for noItem in range( self.punteroNoItems ):        
            widget = layout.itemAt(noItem).widget()
            widget.cambiarTamano(nuevoValor)   


def main():
    app = QApplication(sys.argv)
    ex = SeccionNotas()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()