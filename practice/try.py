nimport sys
from PyQt4 import QtGui, QtCore
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline


class Admin(QtGui.QMainWindow):
	def __init__(self):
		super(Admin, self).__init__()
		self.setGeometry(50, 50, 699, 538)
		self.setWindowTitle("Admin page")

		extractAction = QtGui.QAction("Exit",self)
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

		self.lbl2 = QtGui.QLabel('', self)
		qf = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
		self.lbl2.setFont(qf)
		self.lbl2.move(160, 240)
		self.lbl2.resize(231,41)

		btn = QtGui.QPushButton("Train Corpus", self)
		qf = QtGui.QFont("Verdana", 11, QtGui.QFont.Bold)
		btn.setFont(qf)
		btn.resize(131,41)
		btn.move(160,170)
		btn.clicked.connect(self.trainModule)
		#self.btn.clicked.connect(self.progressM)
		
		'''btn_cancel = QtGui.QPushButton("Quit",self)
		btn_cancel.resize(131,41)
		btn_cancel.move(140,380)
		btn_cancel.clicked.connect(self.close_application)'''


		btn_out = QtGui.QPushButton("Log Out",self)
		btn_out.setFont(qf)
		btn_out.resize(131,41)
		btn_out.move(350,170)
		btn_out.clicked.connect(self.logOut)
		
		

		'''btnAddLang = QtGui.QPushButton("Add Languages",self)
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
		checkBox3 = QtGui.QCheckBox('Bengali',self)
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

	def logOut(self):
		self.close()
		print("log out successful..!")	

	'''def enlarged_Window(self, state):

		if state == QtCore.Qt.Checked:
			print("success..")

			#QtGui.QMessageBox("successfull")

	'''



	# data loading functions
	def load_data(self, list_of_files):
		return [line.rstrip() for filename in list_of_files for line in open(filename, encoding = 'UTF-8', errors='ignore')]	
	

	def trainModule(self):
		print("\n Training under process..!")
			#message box or dialogbox coding	
		# accessing files marathi
		marathi_files = glob.glob('/home/jeevan/29-2-16/data_new/Marathi/*.txt')
		data_marathi = self.load_data(marathi_files)

		# accessing files hindi
		hindi_files = glob.glob('/home/jeevan/29-2-16/data_new/Hindi/*.txt')
		data_hindi = self.load_data(hindi_files)

		# whole data
		X_train = data_marathi + data_hindi

		# marathi labels
		marathi_labels = ['Marathi' for _ in data_marathi]

		# hindi labels
		hindi_labels = ['Hindi' for _ in data_hindi]

		# whole labels
		y_train = marathi_labels + hindi_labels
		
		# pipeline
		rf = Pipeline([('vect',TfidfVectorizer(analyzer='word')),('rft',RandomForestClassifier())])

		rf.fit(X_train, y_train)
		print("model trained successfully...")

		# saving the model
		joblib.dump(rf, './randomForest/randomForest.pkl')

		print("model trained & saved successfully...")

		#msg = QMessageBox()
		#msg.setIcon(QMessageBox.Information)
		#msg.setText("model trained & saved successfully...")
		#msg.setInformativeText("This is additional information")
		#msg.setWindowTitle("MessageBox demo")
			
		#QtGui.QMessageBox.Information(self,"")
		
		self.lbl2.setText("model trained successfully..!")
	

	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Close!',
							"Are You sure?",
							QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
		if choice == QtGui.QMessageBox.Yes:
			print("closed..!!")
			sys.exit()
		else:
			pass
		
	



class Login(QtGui.QMainWindow):
	def __init__(self):
		super(Login, self).__init__()
		self.setGeometry(50, 50, 699, 538)
		self.setWindowTitle("Login Page")

		extractAction = QtGui.QAction("Exit",self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Leave The App')
		extractAction.triggered.connect(self.close_application)
		self.statusBar()
	
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		
		#self.home()
	#def home(self):

		lbl1 = QtGui.QLabel('ADMIN LOGIN', self)
		qf = QtGui.QFont("Georgia", 14, QtGui.QFont.Bold)
		lbl1.setFont(qf)
		lbl1.move(460, 20)
		lbl1.resize(161,21)

		lbl2 = QtGui.QLabel('Username :', self)
		qf = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
		lbl2.setFont(qf)
		lbl2.move(260, 80)
		lbl2.resize(101,21)


		lbl2 = QtGui.QLabel('Password :', self)
		qf = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
		lbl2.setFont(qf)
		lbl2.move(260, 130)
		lbl2.resize(101,21)

		btn = QtGui.QPushButton("Login", self)
		qf = QtGui.QFont("Verdana", 11, QtGui.QFont.Bold)
		btn.setFont(qf)
		#btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		#btn.clicked.connect(self.trainModule)
		btn.resize(131,41)
		btn.move(370,200)
		btn.clicked.connect(self.lmethod)
		
		
		btn_cancel = QtGui.QPushButton("Cancel",self)
		btn_cancel.resize(131,41)
		btn_cancel.setFont(qf)
		btn_cancel.move(530,200)
		btn_cancel.clicked.connect(self.loginClose)


		self.textName = QtGui.QLineEdit(self)
		qlef = QtGui.QFont("Arial", 12, )
		self.textName.setFont(qlef)
		self.textName.setGeometry(370,80,321,31)
		#qle.move(370,21)


		self.textPass = QtGui.QLineEdit(self)
		qlef = QtGui.QFont("Arial", 12, )
		self.textPass.setFont(qlef)
		self.textPass.setEchoMode(QtGui.QLineEdit.Password)
		self.textPass.setGeometry(370,130,321,31)

		self.show()
	

	def loginClose(self):
		self.close()

	def adminWindow(self):
				self.myOtherWindow = Admin()
				self.myOtherWindow.show()
				self.close()

	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Close!',
							"Are You sure?",
							QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
		if choice == QtGui.QMessageBox.Yes:
			print("closed..!!")
			sys.exit()
		else:
			pass
	
	def lmethod(self):

		if (self.textName.text() == 'admin' and self.textPass.text() == 'admin'):
			print("login success")
			self.adminWindow()
			
		else:
			QtGui.QMessageBox.warning(self, 'Error', 'Bad user or password')






class Lid(QtGui.QMainWindow):
	def __init__(self):
		super(Lid, self).__init__()
		self.setGeometry(50, 50, 699, 538)
		self.setWindowTitle("Main Window")
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		extractAction = QtGui.QAction("Exit",self)
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


		
		self.resultLabel = QtGui.QLabel('', self)
		qf = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
		self.resultLabel.setFont(qf)
		self.resultLabel.move(240,410)
		
		#self.lbl_lid.resize(451,41)
		#review = QtGui.QLabel('Review')
		btn = QtGui.QPushButton("Identify", self)
		qf = QtGui.QFont("Verdana", 11, QtGui.QFont.Bold)
		btn.setFont(qf)
		#btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.clicked.connect(self.Signal)
		btn.resize(131,41)
		btn.move(170,300)
		
		btn_clear = QtGui.QPushButton("Clear",self)
		btn_clear.setFont(qf)
		btn_clear.resize(131,41)
		btn_clear.move(350,300)
		btn_clear.clicked.connect(self.clear_App)

		btn_admin = QtGui.QPushButton("Admin Login",self)
		btn_admin.setFont(qf)
		btn_admin.resize(131,41)
		btn_admin.move(560,60)
		btn_admin.clicked.connect(self.newWindow)
		#self.connect(button, SIGNAL('clicked()'), self.newWindow)
	



		self.qte = QtGui.QTextEdit(self)
		qtef = QtGui.QFont("Arial", 12, )
		self.qte.setFont(qtef)
		self.qte.setGeometry(170,120,511,151)
		self.qte.move(170,120)
		
		self.show()



	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Close!',
							"Are You sure?",
							QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
		if choice == QtGui.QMessageBox.Yes:
			print("closed..!!")
			sys.exit()
		else:
			pass


	def newWindow(self):
		self.myOtherWindow = Login()
		self.myOtherWindow.show()
		




	def Signal(self):
		
		

		# test file
		#X_test = X_test.join()
		X_test = []
		
		getData = str(self.qte.toPlainText())
		#print(getData)
		X_test.append(getData)
		#print(X_test[0])
		print("test created...!")


		# loading model
		rf = joblib.load('./randomForest/randomForest.pkl')
		print("train model loaded...!")
	


		# prediction
		predicted = rf.predict(X_test)
		print("test prediction done..!")
		self.resultLabel.setText(predicted[0])
		
	
		#lbl_lang1 = QtGui.QLabel('--------???', self)
		#self.lbl_lang.setText('Identified Language is :::- ????')
		#self.lbl_lang.setText("Lang...")
	def clear_App(self):
		self.qte.clear()
		self.resultLabel.setText("")



'''class TrainModule(QtGui.QMainWindow):
	def __init__(self):
		super(TrainModule, self).__init__()
		self.setGeometry(50, 50, 699, 538)
		self.setWindowTitle("Training Module!")

		extractAction = QtGui.QAction("Exit.",self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Leave The App')
		extractAction.triggered.connect(self.close_application)
		self.statusBar()
	
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		
		
	

		lbl1 = QtGui.QLabel('ADMIN MODULE', self)
		qf = QtGui.QFont("Georgia", 14, QtGui.QFont.Bold)
		lbl1.setFont(qf)
		lbl1.move(270, 40)
		lbl1.resize(171,31)

		
	
		btn = QtGui.QPushButton("Train Corpus", self)
		qf = QtGui.QFont("Verdana", 11, QtGui.QFont.Bold)
		btn.setFont(qf)
		#btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.clicked.connect(self.trainModule)
		btn.resize(131,41)
		btn.move(110,410)
		#self.btn.clicked.connect(self.progressM)
		
		

		btn_out = QtGui.QPushButton("Log Out",self)
		btn_out.setFont(qf)
		btn_out.resize(131,41)
		btn_out.move(300,410)
		
		
		self.show()
	
	# data loading functions
	def load_data(self, list_of_files):
		return [line.rstrip() for filename in list_of_files for line in open(filename, encoding = 'UTF-8', errors='ignore')]


	def trainModule(self):
		print("\n Welcome to LID system")
		
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
		
		self.QtGui.QMessageBox("Trained Successfully..!")



	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Close!',
							"Are You sure?",
							QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
		if choice == QtGui.QMessageBox.Yes:
			print("closed..!!")
			sys.exit()
		else:
			pass
		
	
'''
