import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from Backend.text_utils import list_to_string, preprocessing

# Load data
df = pd.read_csv("FakeNewsNet.csv")

X = df["title"].astype(str)
y = df["real"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipeline = Pipeline([
    ("join_tokens", FunctionTransformer(list_to_string)),
    ("clean_text", FunctionTransformer(preprocessing)),
    ("tfidf", TfidfVectorizer(
        max_features=10000,
        ngram_range=(1, 2),
        min_df=2
    )),
    ("model", LogisticRegression(max_iter=1000,class_weight="balanced"))
])

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, "Backend/model/text_model_pipeline.pkl")

print("✅ Model trained and saved correctly")
