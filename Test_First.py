from sklearn.externals import joblib
import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 699, 538)
		self.setWindowTitle("First..!")

		extractAction = QtGui.QAction("Exit..!!",self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Leave The App')
		extractAction.triggered.connect(self.close_application)
		self.statusBar()
	
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		
		self.home()
	def home(self):
		

		lbl_input = QtGui.QLabel('Enter Input :', self)
		qf = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
		lbl_input.setFont(qf)
		lbl_input.move(50, 180)

		lbl_result = QtGui.QLabel('Language Predicted :',self)
		qf = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
		lbl_result.setFont(qf)
		lbl_result.move(50,410)
		lbl_result.resize(161,31)
		
		lbl_lid = QtGui.QLabel('LANGUAGE IDENTIFICATION SYSTEM', self)
		qf = QtGui.QFont("Georgia", 16, QtGui.QFont.Bold)
		lbl_lid.setFont(qf)
		lbl_lid.move(150,20)
		lbl_lid.resize(451,41)


		
		'''resultLabel = QtGui.QLabel('--------???', self)
		qf = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
	        resultLabel.setFont(qf)
		resultLabel.move(240,410)'''
		
		#self.lbl_lid.resize(451,41)
		#review = QtGui.QLabel('Review')
		btn = QtGui.QPushButton("Identify", self)
		qf = QtGui.QFont("Verdana", 11, QtGui.QFont.Bold)
		btn.setFont(qf)
		#btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.clicked.connect(self.Signal)
		btn.resize(131,41)
		btn.move(170,300)
		
		btn_cancel = QtGui.QPushButton("Quit",self)
		btn_cancel.setFont(qf)
		btn_cancel.resize(131,41)
		btn_cancel.move(350,300)
		btn_cancel.clicked.connect(self.close_application)

		btn_admin = QtGui.QPushButton("Admin Login",self)
		btn_admin.setFont(qf)
		btn_admin.resize(131,41)
		btn_admin.move(560,60)

		qte = QtGui.QTextEdit(self)
		qtef = QtGui.QFont("Arial", 12, )
		qte.setFont(qtef)
		qte.setGeometry(170,120,511,151)
		qte.move(170,120)
		
		self.show()

	def Signal(self):
		
		# test file
		#X_test = X_test.join()
		X_test = [' नाथन एस्टल ने शतक बनाया  कैदियों के हक में उठी आवाज़ ']
		print("test created...")


		# loading model
		rf = joblib.load('./randomForest/randomForest.pkl')
		print("train model loaded...")
	


		# prediction
		predicted = rf.predict(X_test)
		print("test prediction........................")
		resultLabel = QtGui.QLabel(predicted[0], self)
		qf = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
		resultLabel.setFont(qf)
		resultLabel.move(240,410)
		resultLabel.resize(421,21)
		resultLabel.show()
	

		'''resultLabel = QtGui.QLabel('Marathi..?? Hondi..??..Konkani..??', self)
		qf = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
	        resultLabel.setFont(qf)
		resultLabel.move(240,410)
		resultLabel.resize(421,21)
		resultLabel.show()
		#resultLabel.setText('Identified Language is :::- ????')
		#self.resultLabel.move(150,50)
		#self.resultLabel.adjustSize()	
		print("\n dialog msg")'''
	'''def dialog(self):

		lbl_lang = QtGui.QLabel('--------???', self)
		qf = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
	        lbl_lang.setFont(qf)
		lbl_lang.move(240,410)

	'''
		#lbl_lang1 = QtGui.QLabel('--------???', self)
		#self.lbl_lang.setText('Identified Language is :::- ????')
		#self.lbl_lang.setText("Lang...")
	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Close!',
							"Are You sure?",
							QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
		if choice == QtGui.QMessageBox.Yes:
			print("closed..!!")
			sys.exit()
		else:
			pass
		
		
		
def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())
main()
