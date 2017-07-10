import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
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

		lbl1 = QtGui.QLabel('ADMIN MODULE', self)
		qf = QtGui.QFont("Georgia", 14, QtGui.QFont.Bold)
		lbl1.setFont(qf)
		lbl1.move(270, 40)
		lbl1.resize(171,31)

		lbl2 = QtGui.QLabel('Choose the Languages :', self)
		qf = QtGui.QFont("Arial", 13, QtGui.QFont.Bold)
		lbl2.setFont(qf)
		lbl2.move(90, 120)
		lbl2.resize(201,31)

		'''lbl_module = QtGui.QLabel("ADMIN MODULE",self)
		self.lbl_module.move(270,60)'''
	
		btn = QtGui.QPushButton("Train Corpus", self)
		qf = QtGui.QFont("Verdana", 11, QtGui.QFont.Bold)
		btn.setFont(qf)
		#btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.clicked.connect(self.trainModule)
		btn.resize(131,41)
		btn.move(110,410)
		#self.btn.clicked.connect(self.progressM)
		
		'''btn_cancel = QtGui.QPushButton("Quit",self)
		btn_cancel.resize(131,41)
		btn_cancel.move(140,380)
		btn_cancel.clicked.connect(self.close_application)'''


		btn_out = QtGui.QPushButton("Log Out",self)
		btn_out.setFont(qf)
		btn_out.resize(131,41)
		btn_out.move(300,410)
		

		btnAddLang = QtGui.QPushButton("Add Languages",self)
		btnAddLang.setFont(qf)
		btnAddLang.resize(131,31)
		btnAddLang.move(110,310)
		#btnAddLang.clicked.connect(self.isCheck)
		
		checkBox1 = QtGui.QCheckBox('Marathi',self)
		ch1 = QtGui.QFont("Droid Sans", 12 )
		checkBox1.setFont(ch1)
		checkBox1.move(121,170)
		checkBox1.stateChanged.connect(self.enlarged_Window)
		#checkBox.resize(101,20)
		checkBox2 = QtGui.QCheckBox('Hindi', self)
		ch1 = QtGui.QFont("Droid Sans", 12 )
		checkBox2.setFont(ch1)
		checkBox2.move(121,200)
		'''checkBox3 = QtGui.QCheckBox('Bengali',self)
		checkBox3.setFont(ch1)
		checkBox3.move(121,230)
		checkBox4 = QtGui.QCheckBox('Konkani',self)
		checkBox4.setFont(ch1)
		checkBox4.move(121,260)'''

		self.show()
	
	'''def isCheck(self):
		if self.checkBox1.isChecked:
			print("suc..?")
		else:
			print("faill")'''

	def enlarged_Window(self, state):

		if state == QtCore.Qt.Checked:
			print("success..")

			#QtGui.QMessageBox("successfull")





	# data loading functions
	def load_data(self, list_of_files):
		return [line.rstrip() for filename in list_of_files for line in open(filename, encoding = 'UTF-8', errors='ignore')]	
	

	def trainModule(self):
		print("\n dialog msg")
			#message box or dialogbox coding	
		# accessing files marathi
		marathi_files = glob.glob('/home/pravin/29-2-16/data_new/Marathi/*.txt')
		data_marathi = self.load_data(marathi_files)

		# accessing files hindi
		hindi_files = glob.glob('/home/pravin/29-2-16/data_new/Hindi/*.txt')
		data_hindi = self.load_data(hindi_files)
		
		
		# whole data
		X_train = data_marathi + data_hindi

		# marathi labels
		marathi_labels = ['Marathi' for _ in data_marathi]

		# hindi labels
		hindi_labels = ['Hindi' for _ in data_hindi]

		# whole labels
		y_train = marathi_labels + hindi_labels

		print("\ndata loaded successfully..!")

		# pipeline
		rf = Pipeline([('vect',TfidfVectorizer(analyzer='word')),('rft',RandomForestClassifier())])

		rf.fit(X_train, y_train)
		print("model trained successfully...")

		# saving the model
		joblib.dump(rf, './randomForest/randomForest.pkl')

		print("model trained & saved successfully...")			
		
		QtGui.QMessageBox("Trained Successfully..!")
	

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
