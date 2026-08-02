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

---


## Deployment
This app has been deploed to below streamlit url. Please have a check

https://your-streamlit-app-link-here

---

## Screenshots

Add your screenshots to the repository and reference them here. For example:

```markdown
![App Home Screen](screenshots/app_home.png)

![Model Metrics Screen](screenshots/model_metrics.png)
```

- Create a `screenshots/` folder in the repo.  
- Save your two Bits Virtual Lab screenshots as `app_home.png` and `model_metrics.png` (or update the filenames below).  
- Use relative paths so the images render on GitHub and in markdown viewers.

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
