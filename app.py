import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, matthews_corrcoef, roc_auc_score,
    confusion_matrix, classification_report
)
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("ML Classification Demo App")

# File upload
uploaded_file = st.file_uploader("Upload your CSV dataset", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    # Show full dataset
    st.write("Dataset Preview (all rows):")
    st.dataframe(data)

    # Assume last column is target
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    st.write(f"Training samples: {len(X_train)}")
    st.write(f"Testing samples: {len(X_test)}")

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Model selection
    model_choice = st.selectbox(
        "Choose a model",
        ["Logistic Regression", "Decision Tree", "kNN", "Naive Bayes", "Random Forest"]
    )

    # Define models
    models = {
        "Logistic Regression": LogisticRegression(max_iter=2000, solver='lbfgs'),
        "Decision Tree": DecisionTreeClassifier(),
        "kNN": KNeighborsClassifier(),
        "Naive Bayes": GaussianNB(),
        "Random Forest": RandomForestClassifier()
    }

    model = models[model_choice]

    # Fit model (scaled for some)
    if model_choice in ["Logistic Regression", "kNN", "Naive Bayes"]:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        y_prob = model.predict_proba(X_test_scaled)[:,1] if hasattr(model, "predict_proba") else None
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:,1] if hasattr(model, "predict_proba") else None

    # Metrics
    st.subheader("Evaluation Metrics")
    st.write(f"Evaluation performed on {len(y_test)} test samples out of {len(data)} total rows.")
    st.write("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    st.write("Precision:", round(precision_score(y_test, y_pred, average='weighted'), 4))
    st.write("Recall:", round(recall_score(y_test, y_pred, average='weighted'), 4))
    st.write("F1 Score:", round(f1_score(y_test, y_pred, average='weighted'), 4))
    st.write("MCC:", round(matthews_corrcoef(y_test, y_pred), 4))
    if y_prob is not None and len(np.unique(y)) == 2:
        st.write("AUC:", round(roc_auc_score(y_test, y_prob), 4))
    else:
        st.write("AUC: N/A (binary classification required)")

    # Confusion Matrix
    st.subheader("Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    st.pyplot(fig)

    # Classification Report
    st.subheader("Classification Report")
    st.text(classification_report(y_test, y_pred))
