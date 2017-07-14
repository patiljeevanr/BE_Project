# Headers
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
##from sklearn.neural_network import MLPClassifier
import glob

# data loading function
def load_data(list_of_files):
    return [line.rstrip() for filename in list_of_files for line in open(filename, encoding = 'UTF-8', errors='ignore')]

# classifiers
def train_svm(X, y):
    """
    Create and train the Support Vector Machine.
    """
    svm = SVC(C=1000000.0, gamma=0.0, kernel='rbf')
    svm.fit(X, y)
    return svm
'''
def train_NB(X, y):
    """
    Create and train the Naive Bayes.
    """
    naive_bayes = MultinomialNB()
    naive_bayes.fit(X, y)
    return naive_bayes

def train_random_forest(x, y):
    """
    Create and train the Random Forest.
    """
    rf = RandomForestClassifier()
    rf.fit(X, y)
    return rf

def train_perceptron(X, y):
    """
    Create and train the Perceptron.
    """
    per = Perceptron()
    per.fit(X, y)
    return per

##def train_NN(x, y):
##    """
##    Create and train the NN
##    """
##    nn = MLPClassifier()
##    nn.fit(x, y)
##    return nn
'''
# accessing files marathi
marathi_files = glob.glob('/home/jeevan/29-2-16/data_new/Marathi/*.txt')
data_marathi = load_data(marathi_files)

# accessing files hindi
hindi_files = glob.glob('/home/jeevan/29-2-16/data_new/Hindi/*.txt')
data_hindi = load_data(hindi_files)

# accessing files bodo
#bodo_files = glob.glob('/home/jeevan/29-2-16/data_new/Bodo/*.txt')
#data_bodo = load_data(bodo_files)

# accessing files nepali
nepali_files = glob.glob('/home/jeevan/29-2-16/data_new/Nepali/*.txt')
data_nepali = load_data(nepali_files)

# accessing files konkani
konkani_files = glob.glob('/home/jeevan/29-2-16/data_new/Konkani/*.txt')
data_konkani = load_data(konkani_files)


# accessing files bangla
bangla_files = glob.glob('/home/jeevan/29-2-16/data_new/Bangla/*.txt')
data_bangla = load_data(bangla_files)

# accessing files Telugu
telugu_files = glob.glob('/home/jeevan/29-2-16/data_new/Telugu/*.txt')
data_telugu = load_data(telugu_files)


# whole data
X_train = data_marathi + data_hindi + data_nepali + data_konkani + data_bangla + data_telugu# + data_bodo

# marathi labels
marathi_labels = ['Marathi' for _ in data_marathi]

# hindi labels
hindi_labels = ['Hindi' for _ in data_hindi]

# bodo labels
#bodo_labels = ['Bodo' for _ in data_bodo]

# nepali labels
nepali_labels = ['Nepali' for _ in data_nepali]

# konkani labels
konkani_labels = ['Konkani' for _ in data_konkani]

# bangla labels
bangla_labels = ['Bangla' for _ in data_bangla]

# telugu_labels
telugu_labels = ['Telugu' for _ in data_telugu]

# whole labels
y = marathi_labels + hindi_labels + nepali_labels + konkani_labels + bangla_labels + telugu_labels# + bodo_labels
# tfidf vectorizer
tfidf_vectorizer = TfidfVectorizer(analyzer='word')
X = tfidf_vectorizer.fit_transform(X_train)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training
svm = train_svm(X_train, y_train)
'''multin_nb = train_NB(X_train, y_train)
rf = train_random_forest(X, y)
per = train_perceptron(X, y)
##nn = train_NN(X, y)
'''
# Testing
pred_svm = svm.predict(X_test)
'''pred_nb  = multin_nb.predict(X_test)
pred_rf = rf.predict(X_test)
pred_per = per.predict(X_test)
##pred_nn = nn.predict(X_test)
'''
# printing
print("SVM:")
print("Test accuracy: {}".format(svm.score(X_test, y_test)))
print("Confusion Matrix: \n{}".format(confusion_matrix(pred_svm, y_test)))
'''
print("\nNaive Bayes:")
print("Test accuracy: {}".format(accuracy_score(y_test, pred_nb)))
print("Confusion Matrix: \n{}".format(confusion_matrix(pred_nb, y_test)))

print("\nRandom Forest:")
print("Test accuracy: {}".format(accuracy_score(y_test, pred_rf)))
print("Confusion Matrix: \n{}".format(confusion_matrix(pred_rf, y_test)))

print("\nPerceptron:")
print("Test accuracy: {}".format(accuracy_score(y_test, pred_per)))
print("Confusion Matrix: \n{}".format(confusion_matrix(pred_per, y_test)))

##print("\nNN:")
##print("Test accuracy: {}".format(accuracy_score(y_test, pred_nn)))
##print("Confusion Matrix: \n{}".format(confusion_matrix(pred_nn, y_test)))'''
