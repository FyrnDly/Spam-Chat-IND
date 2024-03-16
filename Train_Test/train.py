import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

# Get data from model excel
data = pd.read_excel("../Model/model_pesan.xlsx")
data['kategori'] = data['kategori'].map({'spam':1, 'ham':0})

# Convert chat to vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['pesan'])
y = data['kategori']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Set K numbers and Array Scores
K = np.arange(1,25)
scores = []

# Loop test to find optimal K numbers for scores
for k in K:
    model_check = KNeighborsClassifier(n_neighbors=k)
    model_check.fit(X_train,y_train)
    score = model_check.score(X_test,y_test)
    scores.append(score)

# Get optimal K number
optimal_k = K[np.argmax(scores)]
max_accuracy = max(scores)

# Create Model Train
model = KNeighborsClassifier(n_neighbors=optimal_k)
model.fit(X_train,y_train)

# Save model
fileName = 'KNN_model_train.sav'
pickle.dump(model,open(fileName, 'wb'))

# Get report Train
print(f'Optimal K number: {optimal_k}\nMax score accuracy: {max_accuracy}')