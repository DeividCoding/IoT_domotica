from PyQt5 import QtWidgets,Qt
from PyQt5.QtWidgets import QWidget,QVBoxLayout
from PyQt5.QtWidgets import  QMessageBox,QMainWindow
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QMainWindow,QLabel,QWidget,QPushButton, QVBoxLayout,QScrollArea,QMessageBox
from PyQt5.QtGui import QIcon

from PyQt5.Qt import QSizePolicy,Qt
from PyQt5 import QtCore


###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################


###############################################################
#  MIS LIBRERIAS...
##############################################################
from CUERPO.LOGICA.ALARMA.ItemAlarmaVista import ItemAlarmaVista
from CUERPO.LOGICA.ALARMA.ItemAlarmaEdit import ItemAlarmaEdit
from CUERPO.LOGICA.ALARMA.baseDatos_alarma import BaseDatos_alarmas
from recursos import App_Alarmas,HuellaAplicacion
from CUERPO.LOGICA.ALARMA.reloj import Reloj
from CUERPO.LOGICA.ALARMA.notificadorAlarmas import NotificadorAlarmas
from CUERPO.LOGICA.ALARMA.checadorAlarma import ChecadorAlarma

###############################################################
#  MIS LIBRERIAS...
##############################################################
import IMAG_rc



class AdministradorAlarmas(QMainWindow,HuellaAplicacion):
    def __init__(self,noDia,hora,minuto,segundo):
        QMainWindow.__init__(self)
        self.initUI()
        HuellaAplicacion.__init__(self)

        self.baseDatosAlarmas=BaseDatos_alarmas(App_Alarmas.NOMBRE_BASE_DATOS_ALARMAS)
        self.baseDatosAlarmas.crearBaseDatos()
        self.ventanaCreadoraAlarmas=ItemAlarmaEdit()

        self.MAX_ITEMS=20
        self.punteroNoItems=0
        self.contadorIdsVivosMuertos = 0

        #self.btn_agregarItem.clicked.connect(partial(self.agregarAlarma,Alarma()))
        self.btnAgregarItem.clicked.connect(self.crearUnaAlarma)
        self.listaItemsRonianos=[]
        self.textPregunta=""
        self.listIdsItemsVivos=[]


        self.prepararSincronizaciones(noDia,hora,minuto,segundo)

        self.cargarAlarmas()
        self.ventanaCreadoraAlarmas.senal_alarmaCreada.connect(self.nuevaAlarmaCreada)

        self.show()


    def initUI(self):
        self.statusBar() 
        toolbar = self.addToolBar('Edicion')
        self.addToolBar(QtCore.Qt.BottomToolBarArea,toolbar)
        toolbar.setStyleSheet("QToolButton:checked {background-color:#94DCD3; border:none; } ")
        toolbar.setMovable(False)
        toolbar.setOrientation(QtCore.Qt.Horizontal)

        toolbar.addWidget(self.get_expansorWidget() )    
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

        self.setGeometry(300, 300, 350, 250)

        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.widget.setLayout(self.vbox)

        

        #Scroll Area Properties
        self.scroll_alarmas = QScrollArea()     # Scroll Area which contains the widgets, set as the centralWidget
        self.scroll_alarmas.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_alarmas.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_alarmas.setWidgetResizable(True)
        self.scroll_alarmas.setWidget(self.widget)
        self.scroll_alarmas.setStyleSheet("""
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
                        background:#F7E5E5;
                        }
                        QScrollBar::handle{
                        background :#979797;
                        }
                        QScrollBar::handle::pressed{
                        background :  #193b58;
                        }
                        """)
        self.setCentralWidget(self.scroll_alarmas)


    def get_separadorQAction(self):
        separadorQAction=QLabel()
        separadorQAction.setMinimumSize(10,2)
        return separadorQAction

    def get_expansorWidget(self):
        expansorWidget=QWidget()
        expansorWidget.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        return expansorWidget   


#######################################################################################################################3
# REVISANDO   LAS     ALARMAS
#######################################################################################################################3
    def prepararSincronizaciones(self,noDia,hora,minuto,segundo):

        self.checadorAlarma=ChecadorAlarma(noDia, hora, minuto )
        self.reloj=Reloj(noDia,hora,minuto,segundo)

        self.avisador=NotificadorAlarmas()    
        self.reloj.senal_minutoCambio.connect(self.consultarChecadorAlarmas)
        self.reloj.senal_diaCambio.connect(self.renovarAlarmas )


        self.checadorAlarma.senal_alarmaDetectada.connect( self.avisador.activarAlarmas )
        self.avisador.senal_alarmaSonando.connect( self.mostrarAvisadorAlarmas )

        
        self.contador=QTimer()
        self.contador.timeout.connect(self.clockContador)
        # Call start() method to modify the timer value
        self.contador.start(10)


    def mostrarAvisadorAlarmas(self):
        self.avisador.show()

    def renovarAlarmas(self,listaDatos):
        print("SOLCITANDO RENOVACION...")
        #listaDatos[0]=dia   listaDatos[1]=hora   listaDatos[2]=minutos
        self.checadorAlarma.actualizarAlarmasHoy( listaDatos[0],listaDatos[1],listaDatos[2] )

    def consultarChecadorAlarmas(self,listaDatos):
        #listaDatos[0]=dia   listaDatos[1]=hora   listaDatos[2]=minutos
        self.checadorAlarma.revisar(listaDatos[1],listaDatos[2])


    def clockContador(self):
         #self.hora=self.hora.addSecs(1)
         #self.timeEdit_tiempo.addSecs(1)
         #self.timeEdit_tiempo.setTime(self.hora)
         self.reloj.clock()


    def cargarAlarmas(self):
        listaAlarmas=self.baseDatosAlarmas.getTodas_alarmas()
        #(   ('Julian', 1, 9, 30, 1, 1, 1, 0, 0, 0, 0, 0), ....   )
        
        for alarma in listaAlarmas:
            self.agregarAlarma(alarma=alarma)


    def crearUnaAlarma(self):
        self.ventanaCreadoraAlarmas.modoTrabajo(modoEdicion=False)
        self.ventanaCreadoraAlarmas.show()

    def nuevaAlarmaCreada(self,alarma):
        #print(alarma[0])
        #print(type(alarma[0]))
        #self.senal_creoUnaAlarma.emit(alarma)
    
        alarma=alarma[0]

        self.checadorAlarma.actuarAnte_anexionAlarma(alarma)
        self.agregarAlarma(alarma)


    def notificarEdicionUnaAlarma(self,alarma):
        #self.senal_editoUnaAlarma.emit(alarma)
        self.checadorAlarma.actuarAnte_edicionUnaAlarma( alarma[0] )

    def agregarAlarma(self,alarma):
        if self.punteroNoItems<self.MAX_ITEMS:
            itemAlarma=ItemAlarmaVista(id=self.contadorIdsVivosMuertos)
            itemAlarma.cargarAlarma(alarma)
            itemAlarma.suHoraMorir.connect(self.borrarItem)
            itemAlarma.senal_alarmaEditada.connect(self.notificarEdicionUnaAlarma)
            self.listIdsItemsVivos.append(self.contadorIdsVivosMuertos)

            self.vbox.addWidget(itemAlarma)
            self.punteroNoItems+=1
            self.contadorIdsVivosMuertos+=1
        else:
            mensaje="El numero maximo de alarmas que\n"
            mensaje+=f"puedes registrar es de: {self.MAX_ITEMS} alarmas\n"  
            mensaje+=f"y usted ya ha creado {self.MAX_ITEMS} alarmas."
            
            ventanaDialogo = QMessageBox()
            ventanaDialogo.setWindowIcon(QIcon(self.ICONO_APLICACION)  )
            ventanaDialogo.setWindowTitle(self.NOMBRE_APLICACION)
            ventanaDialogo.setIcon(QMessageBox.Information)

            ventanaDialogo.setText(mensaje)
            ventanaDialogo.setStandardButtons(QMessageBox.Ok)
            btn_ok = ventanaDialogo.button(QMessageBox.Ok)
            btn_ok.setText('Entendido')
            ventanaDialogo.exec_()



    def borrarItem(self,listaIdIs_itemAMatar):
        print("BORRAR: ",listaIdIs_itemAMatar)
        idItemAMatar=listaIdIs_itemAMatar[0] #id en el orden las widget
        nombreAlarma=listaIdIs_itemAMatar[1] #id en la base de datos

        posItemMatar=self.listIdsItemsVivos.index(idItemAMatar)

        ventanaDialogo = QMessageBox()
        ventanaDialogo.setIcon(QMessageBox.Question)
        ventanaDialogo.setWindowIcon( QIcon(self.ICONO_APLICACION)  )
        ventanaDialogo.setWindowTitle(self.NOMBRE_APLICACION)

        mensaje="¿Esta seguro que quieres\n" 
        mensaje+=f"eliminar la alarma numero: {posItemMatar+1}\n"
        mensaje+=f" cuyo nombre es: {nombreAlarma}?"
        ventanaDialogo.setText(mensaje)
        ventanaDialogo.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        btn_yes = ventanaDialogo.button(QMessageBox.Yes)
        btn_yes.setText('Si')
        btn_no = ventanaDialogo.button(QMessageBox.No)
        btn_no.setText('No')
        ventanaDialogo.exec_()
        if ventanaDialogo.clickedButton()  ==  btn_yes:
            layout=self.vbox
            noWidgetBorrar=posItemMatar
            widgetToRemove = layout.itemAt(noWidgetBorrar).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

            #self.listaItemsRonianos.pop(posItemMatar)
            self.listIdsItemsVivos.pop(posItemMatar)
            self.punteroNoItems -= 1

            self.baseDatosAlarmas.eliminar(nombreAlarma=nombreAlarma)
            #self.senal_eliminoUnaAlarma.emit(nombreAlarma)
            self.checadorAlarma.actuarAnte_eliminacionUnaAlarma(nombreAlarma)
            
    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = AdministradorAlarmas(1,10,20,0)
    application.show()
    app.exec()

    ##sys.exit(app.exec())


