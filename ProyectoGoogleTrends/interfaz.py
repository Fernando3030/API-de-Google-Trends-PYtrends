# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import ui_resources
from pytrends.pyGTrends import pyGTrends
import time
from random import randint
from PyQt4.QtCore import SIGNAL

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def button_click(self):
        paises=self.cbPaises.currentText()
        categoria=self.cbCategoria.currentText()
        fechita=self.cbFecha.currentText()
        busquedas= self.cbBusquedas.currentText()
        if paises == "Ecuador":
             pais = 'EC'
        else:
             if paises=="Argentina":
                 pais='AR'
             else:
                  if paises=="EEUU":
                      pais='US'
                  else:
                       if paises=="España":
					       pais='ES'
                       else: 
                            pais=''
		
	
        if categoria == "AficionesYTiempoLibre":
             cat = "65"
        else:
             if categoria=="Deportes":
                 cat="20"
             else:
                  if categoria=="Finanzas":
                      cat="7"
                  else:
                       if categoria=="Juegos":
					       cat="8"
                       else: 
                            cat=''
		
        if fechita == "Ultimos12Meses":
             fech = "today 12-m"
        else:
             if fechita=="Ultimos30Dias":
                 fech="today 1-m"
             else:
                  if fechita=="Ultimos7Dias":
                      fech="now 7-d"
                  else:
                       if fechita=="2004HastaHoy":
					       fech=''
                       else: 
                            fech=''
		
        if busquedas == "BusquedaImagenes":
             busq = "images"
        else:
             if busquedas=="BusquedaNoticias":
                 busq="news"
             else:
                  if busquedas=="GoogleShopping":
                      busq="froogle"
                  else:
                       if busquedas=="BusquedaYoutube":
					       busq="youtube"
                       else: 
                            busq=''
        google_username = self.txtCorreo.text()
        google_password = self.txtPass.text()
        tendencia = str(self.txtTendencia.text())
        path = "."
        # connect to Google
        connector = pyGTrends(google_username, google_password)
        # make request
        connector.request_report(tendencia,'en-US', cat, pais, fech, '', busq)
        # wait a random amount of time between requests to avoid bot detection
        time.sleep(randint(5, 10))
        # download file
        connector.save_csv(path, tendencia)
        # get suggestions for keywords
        keyword = "milk substitute"
        data = connector.get_suggestions(keyword)
        #self.textEdit.append(data)
        print(data)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(663, 347)
        self.btnBuscar = QtGui.QPushButton(Form)
        self.btnBuscar.setGeometry(QtCore.QRect(240, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnBuscar.setFont(font)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.btnBuscar.clicked.connect(self.button_click)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 121, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtPass = QtGui.QLineEdit(Form)
        self.txtPass.setGeometry(QtCore.QRect(160, 161, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPass.setFont(font)
        self.txtPass.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPass.setObjectName(_fromUtf8("txtPass"))
        self.txtCorreo = QtGui.QLineEdit(Form)
        self.txtCorreo.setGeometry(QtCore.QRect(160, 120, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtCorreo.setFont(font)
        self.txtCorreo.setObjectName(_fromUtf8("txtCorreo"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 201, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 161, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtTendencia = QtGui.QLineEdit(Form)
        self.txtTendencia.setGeometry(QtCore.QRect(160, 200, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtTendencia.setFont(font)
        self.txtTendencia.setObjectName(_fromUtf8("txtTendencia"))
        self.btnLimpiar = QtGui.QPushButton(Form)
        self.btnLimpiar.setGeometry(QtCore.QRect(370, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnLimpiar.setFont(font)
        self.btnLimpiar.setObjectName(_fromUtf8("btnLimpiar"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, -10, 661, 371))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/imagenes/fondo.jpg")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cbPaises = QtGui.QComboBox(Form)
        self.cbPaises.setGeometry(QtCore.QRect(380, 130, 111, 31))
        self.cbPaises.setObjectName(_fromUtf8("cbPaises"))
        self.cbPaises.addItem(_fromUtf8(""))
        self.cbPaises.addItem(_fromUtf8(""))
        self.cbPaises.addItem(_fromUtf8(""))
        self.cbPaises.addItem(_fromUtf8(""))
        self.cbPaises.addItem(_fromUtf8(""))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(380, 100, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(460, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(380, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.cbFecha = QtGui.QComboBox(Form)
        self.cbFecha.setGeometry(QtCore.QRect(380, 200, 111, 31))
        self.cbFecha.setObjectName(_fromUtf8("cbFecha"))
        self.cbFecha.addItem(_fromUtf8(""))
        self.cbFecha.addItem(_fromUtf8(""))
        self.cbFecha.addItem(_fromUtf8(""))
        self.cbFecha.addItem(_fromUtf8(""))
        self.cbFecha.addItem(_fromUtf8(""))
        self.cbCategoria = QtGui.QComboBox(Form)
        self.cbCategoria.setGeometry(QtCore.QRect(500, 130, 151, 31))
        self.cbCategoria.setObjectName(_fromUtf8("cbCategoria"))
        self.cbCategoria.addItem(_fromUtf8(""))
        self.cbCategoria.addItem(_fromUtf8(""))
        self.cbCategoria.addItem(_fromUtf8(""))
        self.cbCategoria.addItem(_fromUtf8(""))
        self.cbCategoria.addItem(_fromUtf8(""))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(500, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(500, 170, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.cbBusquedas = QtGui.QComboBox(Form)
        self.cbBusquedas.setGeometry(QtCore.QRect(500, 200, 151, 31))
        self.cbBusquedas.setObjectName(_fromUtf8("cbBusquedas"))
        self.cbBusquedas.addItem(_fromUtf8(""))
        self.cbBusquedas.addItem(_fromUtf8(""))
        self.cbBusquedas.addItem(_fromUtf8(""))
        self.cbBusquedas.addItem(_fromUtf8(""))
        self.cbBusquedas.addItem(_fromUtf8(""))
        self.label_5.raise_()
        self.btnBuscar.raise_()
        self.label_2.raise_()
        self.txtPass.raise_()
        self.txtCorreo.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.txtTendencia.raise_()
        self.btnLimpiar.raise_()
        self.cbPaises.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.cbFecha.raise_()
        self.cbCategoria.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.cbBusquedas.raise_()

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btnLimpiar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtCorreo.clear)
        QtCore.QObject.connect(self.btnLimpiar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtPass.clear)
        QtCore.QObject.connect(self.btnLimpiar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtTendencia.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Google Trends", None))
        self.btnBuscar.setText(_translate("Form", "Buscar", None))
        self.label_2.setText(_translate("Form", "Correo Gmail:", None))
        self.txtPass.setToolTip(_translate("Form", "Ingrese su contraseña", None))
        self.txtCorreo.setToolTip(_translate("Form", "Ingrese su correo electronico", None))
        self.label_4.setText(_translate("Form", "Tendencia a buscar:", None))
        self.label_3.setText(_translate("Form", "Contraseña:", None))
        self.txtTendencia.setToolTip(_translate("Form", "Ingrese la palabra a buscar", None))
        self.btnLimpiar.setText(_translate("Form", "Limpiar", None))
        self.cbPaises.setItemText(0, _translate("Form", "Ninguno", None))
        self.cbPaises.setItemText(1, _translate("Form", "Ecuador", None))
        self.cbPaises.setItemText(2, _translate("Form", "Argentina", None))
        self.cbPaises.setItemText(3, _translate("Form", "EEUU", None))
        self.cbPaises.setItemText(4, _translate("Form", "España", None))
        self.label_6.setText(_translate("Form", "Paises:", None))
        self.label_7.setText(_translate("Form", "FILTROS", None))
        self.label_8.setText(_translate("Form", "Fecha:", None))
        self.cbFecha.setItemText(0, _translate("Form", "Ninguno", None))
        self.cbFecha.setItemText(1, _translate("Form", "Ultimos12Meses", None))
        self.cbFecha.setItemText(2, _translate("Form", "Ultimos30Dias", None))
        self.cbFecha.setItemText(3, _translate("Form", "Ultimos7Dias", None))
        self.cbFecha.setItemText(4, _translate("Form", "2004HastaHoy", None))
        self.cbCategoria.setItemText(0, _translate("Form", "Ninguno", None))
        self.cbCategoria.setItemText(1, _translate("Form", "AficionesYTiempoLibre", None))
        self.cbCategoria.setItemText(2, _translate("Form", "Deportes", None))
        self.cbCategoria.setItemText(3, _translate("Form", "Finanzas", None))
        self.cbCategoria.setItemText(4, _translate("Form", "Juegos", None))
        self.label_9.setText(_translate("Form", "Categoria:", None))
        self.label_10.setText(_translate("Form", "Busquedas Web:", None))
        self.cbBusquedas.setItemText(0, _translate("Form", "Ninguno", None))
        self.cbBusquedas.setItemText(1, _translate("Form", "BusquedaImagenes", None))
        self.cbBusquedas.setItemText(2, _translate("Form", "BusquedaNoticias", None))
        self.cbBusquedas.setItemText(3, _translate("Form", "GoogleShopping", None))
        self.cbBusquedas.setItemText(4, _translate("Form", "BusquedaYoutube", None))


