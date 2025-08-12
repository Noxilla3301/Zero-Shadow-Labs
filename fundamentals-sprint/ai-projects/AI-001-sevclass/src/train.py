# train.py — logistic regression baseline for severity classification
# pip install scikit-learn pandas joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib, os

df = pd.read_csv(os.path.join('data','labeled.csv'))  # columns: text,label
Xtr, Xte, ytr, yte = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42, stratify=df['label'])

pipe = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=4000)),
    ('lr', LogisticRegression(max_iter=300))
])
pipe.fit(Xtr, ytr)
pred = pipe.predict(Xte)

print(classification_report(yte, pred))
os.makedirs('models', exist_ok=True)
joblib.dump(pipe, os.path.join('models','model.joblib'))
print('[+] Saved models/model.joblib')
