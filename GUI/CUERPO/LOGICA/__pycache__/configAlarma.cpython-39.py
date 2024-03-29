a
    �E`s)  �                   @   s�   d dl mZmZ d dlmZmZmZmZmZm	Z	 d dlm
Z
 d dlmZmZmZ d dl mZ d dlZd dlmZ d dlmZ G d	d
� d
e�ZG dd� deje�Zedkr�e�g �Ze� Ze��  e��  dS )�    )�	QtWidgets�Qt)�QWidget�QVBoxLayout�QPushButton�QGridLayout�	QCheckBox�	QTextEdit)�QMessageBox)r   �
pyqtSignal�QObject)�QtCoreN)�partial)�	Ui_Dialogc                   @   s$   e Zd Zee�Zdd� Zdd� ZdS )�itemRonianoc                 C   s6   t �| � || _|| _|| _|| _| jj�| j� d S �N)	r   �__init__�id�checkBox_estado�textEdit_texto�boton_muerte�clicked�connect�mandarSenalMuerto)�selfr   r   r   r   � r   �JC:\Users\ronal\Desktop\PROYECTO\IoT_domotica\CUERPO\LOGICA\configAlarma.pyr      s    
zitemRoniano.__init__c                 C   s   | j �| j� d S r   )�suHoraMorir�emitr   �r   r   r   r   r      s    zitemRoniano.mandarSenalMuertoN)�__name__�
__module__�__qualname__r   �intr   r   r   r   r   r   r   r      s   	r   c                   @   s`   e Zd Ze� Zdd� Zdd� Zddd�Zdd	� Zd
d� Z	dd� Z
ddd�Zdd� Zddd�ZdS )�Dialog_configAlarmac                 C   s�   t �| � tj�| � | �| � d| _t� | _t� | _	| j�
| j	� | j�tj� | j�tj� | j�d� | j�| j� d| _d| _d| _d| _d| _| jj�t| jdd�� g | _d| _g | _d S )	Nz-*^~^*-T�   r   z:/ICON/IMAGENES/tache_1.pngz:/ICON/IMAGENES/tache_2.png� F) r   r   r   �QDialog�setupUiZSEPARADOR_ITEMSr   �widgetr   �vboxZ	setLayoutZscroll_alarmsZsetVerticalScrollBarPolicyr   ZScrollBarAlwaysOnZsetHorizontalScrollBarPolicyZScrollBarAlwaysOff�setWidgetResizable�	setWidget�	MAX_ITEMS�punteroNoItems�contadorIdsVivosMuertos�IMAGEN_ELIMINAR�IMAGEN_ELIMINAR_2Zbtn_agregarItemr   r   r   �agregarCheckBox�listaItemsRonianosZtextPregunta�listIdsItemsVivos)r   �scroll_alarmar   r   r   r   (   s(    

zDialog_configAlarma.__init__c                 C   s   d S r   r   r   r   r   r   �preguntaBlancoS   s    z"Dialog_configAlarma.preguntaBlancoTc                 C   s   d S r   r   )r   ZtupleFormatr   r   r   �getDatos\   s    zDialog_configAlarma.getDatosc                 C   s   d S r   r   )r   �eventr   r   r   �
closeEventv   s    zDialog_configAlarma.closeEventc                 C   s   d S r   r   r   r   r   r   �datosDefaultx   s    z Dialog_configAlarma.datosDefaultc                 C   s   d S r   r   )r   ZdatosPreguntaZdatosRespuestar   r   r   �abrirPregunta�   s    z!Dialog_configAlarma.abrirPreguntar&   r   c                 C   s�  | j | jk �rnt� }|�d� |�d� t|�}t� }|�d� t� }|�d� t	� }d| j
 d }d| j d }	d| j
 d }
|�||	 |
 � |�dd� |�dd� |�|� |�|� t| j|||�}| j�| j� |j�| j� | j�|� |j|d	d	d
dtjjd� |�|d
d	d
d
� |�|d
d
dd� |�d	d	d	d	� | j�|� |  j d
7  _ |  jd
7  _nt�| dd| j� d�tj � d S )N�K   zgQCheckBox::indicator {width:30px; height:30px; }QCheckBox::indicator:pressed{background-color:#0C868C;}zborder: 1px solid black;zQPushButton{border-image:url(z);}z#QPushButton:hover{border-image:url(z%QPushButton:pressed{border-image:url(�   r   �   �����)Z	alignment�DelphiPreguntasz!El numero maximo de items es de:
z- items, y usted ya ha llegado
a dicho limite.)!r.   r-   r   ZsetMinimumHeightZsetMaximumHeightr   r   �setStyleSheetr	   r   r0   r1   �setMaximumSize�setMinimumSize�setTextZ
setCheckedr   r/   r4   �appendr   r   �
borrarItemr3   �	addWidgetr   r   Z
AlignRightZsetContentsMarginsr*   r
   �question�Ok)r   ZtextoZestador)   Z
gridLayoutZcheckBoxZtextEditZbotonCerrar�a�b�cZnewItemRonianor   r   r   r2   �   sF    





��z#Dialog_configAlarma.agregarCheckBoxc                 C   sH   t d| jd� t d| j� | j�� }t d|� |D ]}| �|d� q2d S )NzBORRAREMOS z	 items,,,zlista de posiciones...zCOPY...F)�printr.   r4   �copyrF   )r   ZcopyList�xr   r   r   �borrarTodosItems�   s    

z$Dialog_configAlarma.borrarTodosItemsc                 C   s�   | j �|�}tj}|r:t�| dd|d � d�tjtjB �}|tjkr�| j}|}|�|��� }|�	|� |�
d � | j�|� | j �|� |  jd8  _d S )Nr@   u2   ¿Esta seguro que quieres
eliminar el item numero r>   �?)r4   �indexr
   ZYesrH   ZNor*   ZitemAtr)   ZremoveWidget�	setParentr3   �popr.   )r   ZidItemAMatarZordenAutomaticaZposItemMatarZ	resultadoZlayoutZnoWidgetBorrarZwidgetToRemover   r   r   rF   �   s$    �
�


zDialog_configAlarma.borrarItemN)T)r&   r   )T)r    r!   r"   r   ZquierePreguntaImagenr   r6   r7   r9   r:   r;   r2   rP   rF   r   r   r   r   r$   &   s   +	
!
(r$   �__main__)�PyQt5r   r   �PyQt5.QtWidgetsr   r   r   r   r   r	   r
   ZPyQt5.QtCorer   r   r   �os�	functoolsr   ZCUERPO.DISENO.alarm_diser   r   r'   r$   r    �QApplication�app�application�show�execr   r   r   r   �<module>   s     W
