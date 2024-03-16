import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# Get data from model excel
data = pd.read_excel("../Model/model_pesan.xlsx")
data['kategori'] = data['kategori'].map({'spam':1, 'ham':0})

# Convert chat to vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['pesan'])
y = data['kategori']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Predict and Test Model
fileName = 'KNN_model_train.sav'
model = pickle.load(open(fileName, 'rb'))
y_pred = model.predict(X_test)


print(classification_report(y_test,y_pred))

# Confusion Matrix visualization
cm =confusion_matrix(y_test,y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot()
plt.show()