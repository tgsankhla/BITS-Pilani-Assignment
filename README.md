# ML Assignment 2 – Classification Models

## Problem Statement
Implement multiple machine learning classification models on a dataset, evaluate them using six metrics, and compare their performance.  
Additionally, build a Streamlit app to allow interactive model selection and evaluation.

---

## Dataset
- **Source**: Breast Cancer dataset (from `sklearn.datasets`)
- **Features**: 30 numeric features describing cell nuclei
- **Target**: Binary classification (Malignant = 0, Benign = 1)

---

## Models Implemented
1. Logistic Regression  
2. Decision Tree Classifier  
3. k-Nearest Neighbors (kNN)  
4. Naive Bayes (GaussianNB)  
5. Random Forest (Ensemble)

---

## Evaluation Metrics
Each model was evaluated using the following six metrics:
- Accuracy  
- Precision  
- Recall  
- F1 Score  
- Matthews Correlation Coefficient (MCC)  
- Area Under Curve (AUC)

---

## Results

| Model               | Accuracy | Precision | Recall | F1    | MCC   | AUC   |
|----------------------|----------|-----------|--------|-------|-------|-------|
| Logistic Regression | 0.9737   | 0.9722    | 0.9859 | 0.9790| 0.9439| 0.9974|
| Decision Tree       | 0.9386   | 0.9444    | 0.9577 | 0.9510| 0.8689| 0.9324|
| kNN                 | 0.9474   | 0.9577    | 0.9577 | 0.9577| 0.8880| 0.9820|
| Naive Bayes         | 0.9649   | 0.9589    | 0.9859 | 0.9722| 0.9253| 0.9974|
| Random Forest       | 0.9649   | 0.9589    | 0.9859 | 0.9722| 0.9253| 0.9967|

---

## Observations
- **Logistic Regression** achieved the highest accuracy and AUC.  
- **Naive Bayes** and **Random Forest** also performed very strongly, with excellent recall.  
- **Decision Tree** was slightly weaker, especially in AUC.  
- **Overall, Logistic Regression can be considered the best performer, closely followed by Naive Bayes and Random Forest.**

---

## Streamlit App
An interactive app was built using **Streamlit** to:
- Upload a dataset (CSV format)
- Select a model
- Display evaluation metrics
- Show confusion matrix and classification report

 [Live Streamlit App Link](https://your-streamlit-app-link-here)

---

## Virtual Lab Screenshot
A screenshot of the notebook (`ML_Assignment_2.ipynb`) running successfully in the BITS Virtual Lab is included in the final PDF submission.

![Virtual Lab Screenshot 1](<Screenshot (1663).png>)
![Virtual Lab Screenshot 2](<Screenshot (1664).png>)

---

## Repository Structure
ML_Assignment_2/
│── ML_Assignment_2.ipynb   # Jupyter Notebook with experiments
│── app.py                  # Streamlit app
│── requirements.txt        # Dependencies
│── README.md               # Documentation

## How to Run Notebook and Streamlit App
```bash
jupyter notebook ML_Assignment_2.ipynb
streamlit run app.py

---