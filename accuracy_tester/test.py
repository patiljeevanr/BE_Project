# headers
print("test started...")
from sklearn.externals import joblib
print("1st header loaded...")
##from train import tfidf_vectorizer
##print("2st header loaded...")

# test file
X_test = [' नाथन एस्टल ने शतक बनाया  कैदियों के हक में उठी आवाज़ ']
print("test created...")

### ifidf vectorizer for test file
##X_test_tfidf = tfidf_vectorizer(X_test)
##print("test vectorizer done...")

# loading model
rf = joblib.load('./randomForest/randomForest.pkl')
print("train model loaded...")

# prediction
predicted = rf.predict(X_test)
print("test prediction........................")

# printing
size = len(X_test)
for text, lang in zip(X_test, range(5)):
    print('%r => %s' % (text, predicted[lang]))

