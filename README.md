# 🚬 Smoking Health Dashboard (Streamlit App)

## 🚀 Overview
This project is an interactive **Data Analysis Dashboard** built with Streamlit to analyze the relationship between smoking habits and health indicators such as:

- Age
- Heart Rate
- Blood Pressure
- Cholesterol
- Smoking status (current smoker / non-smoker)
- Gender

The dashboard helps visualize health risks and patterns in smoking-related data.

---

## 📁 Dataset
The project uses a dataset from Kaggle:


---

## 🧠 Features

### 📊 Sidebar Controls
- Filter by:
  - Sex
  - Current Smoker
  - Age
  - Heart Rate

---

### 📈 Key Metrics (KPIs)
The dashboard displays:
- Maximum & Minimum Age
- Maximum & Minimum Heart Rate
- Maximum & Minimum Blood Pressure
- Maximum & Minimum Cholesterol

---

### 📊 Visualizations

#### 🔹 Scatter Plots
- Blood Pressure vs Heart Rate
- Cholesterol vs Heart Rate  
(with filtering by category and size variables)

---

#### 🔹 Bar Chart
- Sex vs Current Smoker relationship

---

#### 🔹 Pie Charts
- Current Smoker vs Age distribution  
- Current Smoker vs Cholesterol distribution (donut chart)

---

## 🛠️ Technologies Used
- Python 🐍  
- Streamlit 🌐  
- Pandas 📊  
- NumPy 🔢  
- Plotly Express 📈  

---

## 🎯 Insights
- Smoking status is strongly related to heart rate and blood pressure  
- Cholesterol levels vary between smokers and non-smokers  
- Age distribution helps identify high-risk groups  
- Visualization helps in understanding hidden health patterns  

---

## ▶️ How to Run

```bash
pip install streamlit pandas numpy plotly
streamlit run app.py
