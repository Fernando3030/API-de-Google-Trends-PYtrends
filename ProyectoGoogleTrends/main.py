from PyQt4 import QtGui
from interfaz import Ui_Form 
import sys

def main():
	app= QtGui.QApplication(sys.argv)
	widget=QtGui.QWidget()
	window=Ui_Form()
	window.setupUi(widget)
	widget.show()
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()
	