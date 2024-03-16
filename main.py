import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Get data from model excel
fileName = "Model/model_pesan.xlsx"
data = pd.read_excel(fileName)

# Vectorizer chat
vectorizer = TfidfVectorizer()
vectorizer.fit(data['pesan'])

# Load file model KNN
fileName = 'Model/KNN_model.sav'
model = pickle.load(open(fileName, 'rb'))

# Function to Check Chat call
def check_chat(chat):
    # Convert chat to vectorizer
    chat_vector = vectorizer.transform([chat])
    # Predict Chat
    chat_pred = model.predict(chat_vector)
    if chat_pred == 0:
        status = "Normal"
    else:
        status = "Spam"
    response = {
        'Chat' : chat,
        'Status' : status
    }
    return response