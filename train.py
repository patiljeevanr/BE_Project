# headres
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline

# loading of data function
def load_data(filename):
    return [line.rstrip() for line in open(filename, encoding = 'UTF-8', errors='ignore')]

def tfidf_vectorizer(data):
    return tfidf_vectorizer.transform(data)


# loading data
filename = '/home/pravin/29-2-16/data_new/train_data'
X_train = load_data(filename)

# loading labels
labels = '/home/pravin/29-2-16/data_new/train_labels'
y_train = load_data(labels)
print("loding done successfully...")

# pipeline
rf = Pipeline([('vect',TfidfVectorizer(analyzer='word')),('rft',RandomForestClassifier())])

### tfidf vectorizer
##tfidf_vectorizer = TfidfVectorizer(analyzer='word')
##X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
##
### randomForest code
##rf = RandomForestClassifier()
rf.fit(X_train, y_train[:-1])
print("model trained successfully...")

# saving the model
joblib.dump(rf, './randomForest/randomForest.pkl')

print("model trained & saved successfully...")
