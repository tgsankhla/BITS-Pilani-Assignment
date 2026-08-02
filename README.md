# ML Assignment 2 — Classification Models

## Overview
This project implements several supervised classification models, evaluates them using multiple metrics, and provides an interactive Streamlit app for running experiments and visualizing results.

Key features:
- Notebook experiments and model comparisons
- A Streamlit app to upload data, choose a model, and view metrics and plots
- Sample dataset included for quick testing

---

## Quickstart
1. Install dependencies (see Requirements).  
2. Run the Streamlit app locally:

```bash
streamlit run app.py
```

3. Open the app in the browser, upload a CSV, select a model, and inspect metrics.

---

## Installation
1. Create a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Streamlit app
- Upload your dataset (CSV). The app assumes the last column is the target.  
- Choose one of the implemented models.  
- View evaluation metrics, confusion matrix, and classification report.

Notebook
- `ML_Assignment_2.ipynb` contains experiments and code used to train and evaluate models offline.


## Screenshots from BITS Virtual lab

![Virtual Screen 1](screenshots/Lab1.png)

![Virtual Screen 2](screenshots/Lab2.png)

---

## Dataset
- Sample dataset: `test_data.csv` (500 rows, 12 features + target) — included for testing.  
- Notebook uses the Breast Cancer dataset from `sklearn.datasets` for demonstration.  
- You may upload your own CSV or XLSX file in the Streamlit app. The app expects the target to be the last column.

---

## Models Implemented
- Logistic Regression
- Decision Tree Classifier
- k-Nearest Neighbors (kNN)
- Naive Bayes (GaussianNB)
- Random Forest

---

## Evaluation Metrics
- Accuracy
- Precision (weighted for multiclass)
- Recall (weighted for multiclass)
- F1 Score (weighted for multiclass)
- Matthews Correlation Coefficient (MCC)
- Area Under the ROC Curve (AUC) — for binary classification where probability estimates are available

---

## Results / Observations (summary)
- Logistic Regression often achieved the best overall trade-off (accuracy and AUC) on the demo dataset.  
- Naive Bayes and Random Forest performed competitively for recall in some runs.  
- Decision Tree was less consistent on AUC for the demo dataset.  

Notes: results depend on the dataset and preprocessing; consult the notebook for detailed experiments.

---

## Repository Structure

ML_Assignment_2/
- ML_Assignment_2.ipynb    # Jupyter Notebook with experiments
- app.py                   # Streamlit application
- requirements.txt         # Python dependencies
- test_data.csv            # Sample dataset for quick testing
- README.md                # This document

---

## Requirements
- Python 3.9+
- See `requirements.txt` for exact package versions. Typical packages used:
  - pandas
  - scikit-learn
  - streamlit
  - matplotlib
  - seaborn

---

## App Preview
Below are screenshots of the Streamlit app running locally (`localhost:8501`):

### Dataset Upload and Model Selection
![App Screenshot 1](<screenshots\App_Local1.png>)

### Evaluation Metrics and Confusion Matrix
![App Screenshot 2](<screenshots\App_Local2.png>)

### Classification Report
![App Screenshot 3](<screenshots\App_Local3.png>)

These screenshots demonstrate successful dataset upload, model selection (kNN), evaluation metrics display, confusion matrix visualization, and classification report generation.

---

## Conclusion
This project successfully implements multiple machine learning classification models and provides an interactive Streamlit interface for evaluation.  
- The app supports both `.csv` datasets.  
- Evaluation metrics and visualizations are automatically generated for each model.  
- **Logistic Regression** achieved the best overall performance, followed closely by **Naive Bayes** and **Random Forest**.  

The repository is complete, reproducible, and ready for evaluation.  
It includes the notebook, Streamlit app, requirements, and a sample dataset (`test_data.csv`) that meets the assignment specifications.

---

## Streamlit App (Live)
👉 [Live Streamlit App](https://tusharsankhla-ml-assignment2.streamlit.app/)
