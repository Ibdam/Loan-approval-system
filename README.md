# 💳 Loan Approval Prediction System

A machine learning-based web application that predicts whether a loan application should be **Approved** or **Declined** based on key applicant features such as income, dependents, education, employment status, and asset value.  

This project demonstrates a complete data science workflow from **data preprocessing**, **model training**, **evaluation**, and **deployment** using **Flask** and **Render**.

---

## 🚀 Features

✅ Predict loan approval status using trained ML models (Logistic Regression / Random Forest / XGboost).  
✅ User-friendly web interface for entering applicant details.  
✅ Dynamic result card showing **Approved** or **Declined**.  
✅ Visualizations (confusion matrix, loan approval rates, correlation heatmap).  
✅ Deployable on **Render** or **Vercel** for free hosting.

---

## 🧠 Machine Learning Workflow

1. **Data Preprocessing**
   - Handled missing values.
   - Encoded categorical features (Education, Self Employed).
   - Feature scaling using `StandardScaler`.

2. **Feature Engineering**
   - Created additional features like:
     - `debt_to_income = loan_amount / income_annum`
     - `asset_coverage = Assets_value / loan_amount`

3. **Model Training**
   - Models used:
     - Logistic Regression
     - Random Forest Classifier
     - XGBoost (tested)
   - Balanced the dataset using **SMOTE** to handle class imbalance.
   - Achieved ~58% accuracy (after balancing).

4. **Evaluation Metrics**
   - Confusion Matrix
   - Precision, Recall, and F1-Score

---

## 🖥️ Web Application Overview

**Input Form Fields:**
- Number of Dependents  
- Education (Graduate / Not Graduate)  
- Self Employed (Yes / No)  
- Annual Income (₦)  
- Loan Amount (₦)  
- Loan Term (Months)  
- Asset Value (₦)

**Output:**
- A visually styled card showing:  
  🟢 “Approved” or 🔴 “Declined”

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|-----------------|
| **Backend** | Flask |
| **Frontend** | HTML5, CSS3 |
| **ML Libraries** | scikit-learn, pandas, numpy, matplotlib, seaborn |
| **Visualization** | Matplotlib, Seaborn |
| **Deployment** | Render (Free Tier) |

---

## 🛠️ Installation & Setup

## 1 Clone the repository
```bash
git clone https://github.com/Ibdam/Loan-approval-system.git
cd Loan-approval-system

## 2 Create Virtual Environment
python -m venv venv
source venv/Scripts/activate   # On Windows
# or
source venv/bin/activate       # On macOS/Linux

3 Install Dependencies
pip install -r requirements.txt

4 Run the Application
python app.py

5 Access Locally

Visit:
👉 http://127.0.0.1:5000/

🌐 Live Demo

🔗 Deployed on Render:
https://loan-approval-system-w7ep.onrender.com/

📊 Visualizations

📁 All project visualizations (confusion matrix, approval distribution, correlation heatmap) are stored in the
visualization/ folder and generated using Matplotlib and Seaborn.

🎥 Video Editing Works (For Reference)

Here are some of my professional video editing works related to tech storytelling and digital projects:
🎬 Video 1: 'https://drive.google.com/file/d/1W5qcx7O-iZFs0o3rnIAPfdI3paSVnBdU/view?usp=sharing'

🎬 Video 2: 'https://drive.google.com/file/d/1sw2lUwYSNG7HYZ-6KO7uWW7ISow48H_c/view?usp=sharing'

🎬 Video 3: 'https://drive.google.com/file/d/1PLmjGOlbgIyx-IK0OFgWS2m2bK2qvORT/view?usp=sharing'

🎬 Video 4: 'https://drive.google.com/file/d/17N58g1L-aa_IjQXGu7pF8m3xFyReRbni/view?usp=sharing'

🎬 Video 5: 'https://drive.google.com/file/d/1gg0mbtYjAtaJVkm9aPrt55aiC88KTJzq/view?usp=sharing'

🎬 Video 6: 'https://drive.google.com/file/d/1YYsfOaDQ_2-w9-ZbVX2LiMonxmBJjjaL/view?usp=sharing'

🧑‍💻 Author

👤 Olowomojuore Damilola Ibrahim
📧 Email: olowomojuoredamilola@gmail.com

🌍 Twine: https://www.twine.net/seaprime

💼 GitHub: https://github.com/Ibdam

🏁 Future Improvements

Integrate Nigerian-based financial dataset

Improve accuracy with feature selection or neural networks

Add database (SQLite/PostgreSQL) to track user submissions

Develop admin dashboard for loan statistics visualization

🪙 License

This project is licensed under the MIT License — you are free to use, modify, and distribute it with attribution.

⭐ If you like this project, please give it a star on GitHub!