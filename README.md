# 📱 SMS Spam Detection

An NLP-based SMS and Email spam detection web application built with Machine Learning and deployed using Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sms-spam-detection.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Live Demo

👉 [Try the app on Streamlit Cloud](https://smsspamdetection-42raz4ncuvcayabxb5cagy.streamlit.app)

---

## 📌 Overview

This project detects whether a given SMS or email message is **Spam** or **Not Spam** using Natural Language Processing (NLP) techniques and a Stacking Classifier ensemble model.

---

## 🧠 How It Works

1. **Input** — User enters an SMS or email message
2. **Preprocessing** — Text is cleaned using NLP techniques:
   - Lowercasing
   - Tokenization
   - Removing special characters and stopwords
   - Stemming (Porter Stemmer)
3. **Vectorization** — Cleaned text is converted to numerical features using TF-IDF
4. **Prediction** — Stacking Classifier predicts Spam or Not Spam
5. **Output** — Result is displayed on the app

---

## 🗂️ Project Structure

```
sms_spam_detection/
├── data/
│   ├── raw/
│   │   └── spam.csv                  # Raw dataset
│   └── processed/
│       ├── cleaned_data.csv          # After cleaning
│       └── preprocessed_data.csv     # After NLP preprocessing
├── notebooks/
│   ├── 01_data_cleaning.ipynb        # Data cleaning steps
│   ├── 02_text_preprocessing.ipynb   # NLP preprocessing
│   └── 03_model.ipynb                # Model training & evaluation
├── src/                              # Source utilities
├── app.py                            # Streamlit web app
├── vectorizer.pkl                    # Saved TF-IDF vectorizer
├── stacking_classifier.pkl           # Saved stacking classifier model
├── requirements.txt                  # Python dependencies
└── README.md
```

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.11 |
| NLP | NLTK (tokenization, stopwords, stemming) |
| ML Models | Scikit-learn, CatBoost |
| Vectorization | TF-IDF (sklearn) |
| Web App | Streamlit |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |

---

## 📊 Models Used

Multiple classifiers were trained and evaluated. The final model is a **Stacking Classifier** ensemble chosen for its best overall balance of accuracy and precision.

### Base Model Comparison

| Model | Accuracy | Precision |
|---|---|---|
| AdaBoost (AB) | 92.81% | 85.15% |
| KNN | 92.09% | 100.00% |
| Decision Tree (DT) | 97.30% | 89.03% |
| XGBoost | 97.21% | 94.78% |
| Gradient Boosting (GB) | 95.69% | 95.58% |
| LightGBM | 98.02% | 95.10% |
| CatBoost | 97.12% | 96.85% |
| Naive Bayes (NB) | 97.75% | 99.22% |
| Logistic Regression (LR) | 95.60% | 99.04% |
| SVC | 98.29% | 98.53% |
| Extra Trees (ET) | 98.29% | 98.53% |
| Random Forest (RF) | 98.11% | 100.00% |

### Ensemble Models

| Model | Accuracy | Precision |
|---|---|---|
| Voting Classifier | 97.75% | 100.00% |
| ✅ **Stacking Classifier** | **99.10%** | **99.30%** |

> **Stacking Classifier** was chosen as the final model for its superior accuracy while maintaining very high precision.

---

## ⚙️ Installation & Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/kaushalkumarma2025/sms_spam_detection.git
cd sms_spam_detection
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
nltk
scikit-learn
catboost
```

---

## 📁 Dataset

The project uses the [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) which contains 5,574 SMS messages labeled as spam or ham (not spam).

---

## 👨‍💻 Author

**Kaushal Kumar**
- GitHub: [@kaushalkumarma2025](https://github.com/kaushalkumarma2025)

---

## 📄 License

This project is licensed under the MIT License.
