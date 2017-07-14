from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
import sys
from PyQt4 import QtGui, QtCore
import glob
import shutil
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline




class Admin(QtGui.QMainWindow):
	def __init__(self):
		super(Admin, self).__init__()
		self.setGeometry(50, 50, 699, 538)
		self.setWindowTitle("Admin page")
		self.setStyleSheet("QMainWindow{font-size : 400px; color : blue; background-image: url('/home/jeevan/29-2-16/silver4.jpg');}")
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
		self.lbl2.move(230, 90)
		self.lbl2.resize(231,41)

		
				
	
		btn = QtGui.QPushButton("Train Corpus", self)
		qf = QtGui.QFont("Verdana", 11, QtGui.QFont.Bold)
		btn.setFont(qf)
		btn.resize(131,41)
		btn.move(280,170)
		btn.clicked.connect(self.trainModule)
		

		btn_out = QtGui.QPushButton("Log Out",self)
		btn_out.setFont(qf)
		btn_out.resize(131,41)
		btn_out.move(520,170)
		btn_out.clicked.connect(self.logOut)
		
		
		btn_remove = QtGui.QPushButton("Delete old models",self)
		qf = QtGui.QFont("Verdana", 11, QtGui.QFont.Bold)
		btn_remove.setFont(qf)
		btn_remove.resize(161,41)
		btn_remove.move(20,170)
		btn_remove.clicked.connect(self.deleteModels)
		
		self.show()
	
	
	def deleteModels(self):
		shutil.rmtree("/home/jeevan/29-2-16/data_new/randomForest")
		#os.remove("/home/jeevan/29-2-16/data_new/randomForest")
		print("\nold Model deleted successfully..!")
	
	def logOut(self):
		self.lidWindow = Lid()
		self.lidWindow.show()
		self.close()
		print("log out successful..!")	



	# data loading functions
	def load_data(self, list_of_files):
		return [line.rstrip() for filename in list_of_files for line in open(filename, encoding = 'UTF-8', errors='ignore')]	
	

	def trainModule(self):
		if not os.path.exists("/home/jeevan/29-2-16/data_new/randomForest"):
			os.makedirs("/home/jeevan/29-2-16/data_new/randomForest")
		print("\n Training under process..!")
			#message box or dialogbox coding
	
		# accessing files marathi
		marathi_files = glob.glob('/home/jeevan/29-2-16/data_new/Marathi/*.txt')
		data_marathi = self.load_data(marathi_files)

		# accessing files hindi
		hindi_files = glob.glob('/home/jeevan/29-2-16/data_new/Hindi/*.txt')
		data_hindi = self.load_data(hindi_files)

		# accessing files bodo
#		bodo_files = glob.glob('/home/jeevan/29-2-16/data_new/Bodo/*.txt')
#		data_bodo = self.load_data(bodo_files)

		# accessing files nepali
		nepali_files = glob.glob('/home/jeevan/29-2-16/data_new/Nepali/*.txt')
		data_nepali = self.load_data(nepali_files)

		# accessing files konkani
		konkani_files = glob.glob('/home/jeevan/29-2-16/data_new/Konkani/*.txt')
		data_konkani = self.load_data(konkani_files)


		# accessing files bangla
		bangla_files = glob.glob('/home/jeevan/29-2-16/data_new/Bangla/*.txt')
		data_bangla = self.load_data(bangla_files)
	
		# accessing files Telugu
		telugu_files = glob.glob('/home/jeevan/29-2-16/data_new/Telugu/*.txt')
		data_telugu = self.load_data(telugu_files)


		# whole data
		X_train = data_marathi + data_hindi + data_nepali + data_konkani + data_bangla + data_telugu# + data_bodo

		# marathi labels
		marathi_labels = ['Marathi' for _ in data_marathi]

		# hindi labels
		hindi_labels = ['Hindi' for _ in data_hindi]

		# bodo labels
#		bodo_labels = ['Bodo' for _ in data_bodo]

		# nepali labels
		nepali_labels = ['Nepali' for _ in data_nepali]

		# konkani labels
		konkani_labels = ['Konkani' for _ in data_konkani]

		# bangla labels
		bangla_labels = ['Bangla' for _ in data_bangla]

		# telugu_labels
		telugu_labels = ['Telugu' for _ in data_telugu]

		# whole labels
		y_train = marathi_labels + hindi_labels + nepali_labels + konkani_labels + bangla_labels + telugu_labels# + bodo_labels
		
		# pipeline of random forest and tfidf vectorizer
		rf = Pipeline([('vect',TfidfVectorizer(analyzer='word')),('rft',RandomForestClassifier())])
		rf.fit(X_train, y_train)
		print("model trained successfully...")

		# saving the model
		joblib.dump(rf, './randomForest/randomForest.pkl')

		print("model trained & saved successfully...")

		
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
		self.setStyleSheet("QMainWindow{font-size : 400px; color : blue; background-image: url('/home/jeevan/29-2-16/silver4.jpg');}")

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
		lbl1.move(450, 30)
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

		#open testin form
		self.lidWindow = Lid()
		self.lidWindow.show()		
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
			QtGui.QMessageBox.warning(self, 'Error', 'Incorrect Username or Password.!!')






class Lid(QtGui.QMainWindow):
	def __init__(self):
		super(Lid, self).__init__()
		self.setGeometry(50, 50, 699, 538)
		self.setWindowTitle("Main Window")
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.setStyleSheet("QMainWindow{font-size : 400px; color : blue; background-image: url('/home/jeevan/29-2-16/silver4.jpg');}")
	
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
		self.close()	




	def Signal(self):
		
		

		# test file
		#X_test = X_test.join()
		X_test = []
		
		getData = str(self.qte.toPlainText())

		if(getData[:4] == "http" or getData[:3] == "www" ):
			print("pleas Wait ..Test data crawling from weblink")
			html = urlopen(getData).read()
			soup = BeautifulSoup(html, "html.parser")
			# kill all script and style elements
			for script in soup(["script", "style"]):
			    script.extract()    # rip it out
			# get text
			text = soup.get_text()
			# break into lines and remove leading and trailing space on each
			lines = (line.strip() for line in text.splitlines())
			# break multi-headlines into a line each
			chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
			# drop blank lines
			text = '\n'.join(chunk for chunk in chunks if chunk)
			#a = re.sub('[A-Za-z0-9]+',"",text)
			getData = re.sub('[^\u0900-\u097F\u002E\u002C\u003F\u0021]'," ",text)
			#print(re.sub('&:,+',"",a))
				#chnges rqrd	

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
		
	
		
	def clear_App(self):
		self.qte.clear()
		self.resultLabel.setText("")



		
		
		
def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Lid()
	sys.exit(app.exec_())
main()


