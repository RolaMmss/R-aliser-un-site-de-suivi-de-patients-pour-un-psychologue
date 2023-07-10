import pandas as pd
import texthero as hero
from texthero import stopwords, preprocessing
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Read the XLSX file
data= pd.read_csv("../data/Emotion_final.csv")



default_stopwords = set(stopwords.DEFAULT)
custom_stopwords = ['ive','something','feel','feeling','feelings','like','im','know','get','would','time','little','even','one','life','people','think','bit','things','much','dont','make','going']
# Get the default English stopwords from texthero and add the custom stopwords
all_stopwords = default_stopwords.union(custom_stopwords)

# Prétraitement des données
custom_pipeline = [preprocessing.fillna,
                   preprocessing.lowercase,
                   preprocessing.remove_whitespace,
                   preprocessing.remove_diacritics,
                   preprocessing.remove_punctuation,
                   preprocessing.remove_urls,
                   preprocessing.remove_digits,
                   preprocessing.remove_brackets,
                   preprocessing.remove_angle_brackets,
                   preprocessing.remove_curly_brackets,
                   preprocessing.remove_square_brackets,
                   preprocessing.remove_punctuation,
                   preprocessing.remove_round_brackets,
                   preprocessing.remove_html_tags,
                   preprocessing.remove_whitespace,
                   lambda x: preprocessing.remove_stopwords(x, stopwords=all_stopwords)  # Apply remove_stopwords to each element
]

data['clean_text'] = hero.clean(data['Text'], pipeline=custom_pipeline)
data.to_csv('../data/clean_data.csv', index=False)  # Saving the DataFrame to a CSV file


# Example usage
nlp_pipeline = Pipeline([
    # ('preprocessor', custom_pipeline()),
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])


X = data['clean_text']
y = data['Emotion']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

nlp_pipeline.fit(X_train, y_train)
y_pred = nlp_pipeline.predict(y_test)

# Calculate accuracy for TF-IDF model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy (TF-IDF):", accuracy)

# Mesure de confiance (ici, probabilité de la classe prédite)
confidence = nlp_pipeline.predict_proba(X_test).max(axis=1)

# print("Rapport de classification pour le modèle TF-IDF :")
# print(classification_report(y_test, y_pred))
# confidence

with open('nlp_pipeline.pkl', 'wb') as file:
    pickle.dump(nlp_pipeline, file)