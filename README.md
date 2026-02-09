# 🎓 Student Performance Analysis System

---

## 📌 Abstract

The **Student Performance Analysis System** is a Python-based mini project developed to manage, preprocess, analyze, and visualize student performance data.  

The system allows users to:
- Create and maintain student records in CSV format  
- Clean and preprocess the dataset  
- Generate insightful visualizations  
- Log application activities  

This project demonstrates practical implementation of:

- File Handling  
- Data Validation  
- Data Preprocessing  
- Data Visualization  
- Logging  
- Git Version Control  

---

## 🧠 Objectives

- Implement CSV file handling in Python  
- Perform data cleaning (handling missing values and duplicates)  
- Apply preprocessing techniques using Pandas  
- Generate visualizations using Matplotlib and Seaborn  
- Implement logging functionality  
- Use Git and GitHub for version control  

---

## 🏗️ Project Structure

```
Mini_project/
│
├── data/
│   ├── data_student.csv
│   └── Cleaned_data_student.csv
│
├── plots/
│   └── (Generated PNG files)
│
├── student-data.py
├── preprocessing.py
├── visualization.py
├── logger_config.py
├── main.py
└── README.md
```

---

## 📂 Module Description

### 1️⃣ main.py
- Entry point of the project  
- Provides a menu-driven interface  
- Integrates all modules  

---

### 2️⃣ student-data.py
Handles student CSV operations.

**Features:**
- Create CSV file if not exists  
- Write default 50 rows  
- Manual data entry with validation  
- Read student records  
- Append new student records  

**Validations Implemented:**
- Positive integer validation  
- Score range validation (0–100)  
- Name validation (no digits allowed)  
- Grade validation (A–F)  

---

### 3️⃣ preprocessing.py
Handles data cleaning using Pandas.

**Features:**
- Convert columns to numeric  
- Handle missing values  
  - Numerical → Mean  
  - Categorical → Mode  
- Remove duplicate rows  
- Remove duplicate Roll Numbers  
- Save cleaned dataset  

**Output File:**  
`Cleaned_data_student.csv`

---

### 4️⃣ visualization.py
Generates charts from cleaned dataset.

**Charts Included:**
- Average Total Score by Grade  
- Top 10 Students  
- Histogram of Total Scores  
- Boxplot of Total Score by Grade  
- Attendance vs Total Score  

All plots are automatically saved in the `plots/` folder.

---

### 5️⃣ logger_config.py
Implements logging functionality.

**Features:**
- Logs application activity  
- Tracks operations and errors  
- Stores logs in:

```
project_log.txt
```

---

## 🛠️ Technologies Used

- Python  
- CSV Module  
- Pandas  
- Matplotlib  
- Seaborn  
- Logging Module  
- Git & GitHub  

---

## ⚙️ Key Functionalities

- Menu-driven system  
- CSV database management  
- Data cleaning and preprocessing  
- Statistical aggregation (GroupBy, Mean)  
- Data visualization  
- Logging implementation  
- Git branching and merging  

---

## 🔄 Git Workflow Used

- Initialize repository  
- Add and commit files  
- Create feature branches  
- Merge branches into main  
- Push changes to GitHub  

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone <repository-link>
```

### 2️⃣ Navigate to project folder

```bash
cd Mini_project
```

### 3️⃣ Install required libraries

```bash
pip install pandas matplotlib seaborn
```

### 4️⃣ Run the program

```bash
python main.py
```

---

## 🎯 Learning Outcomes

- File Handling in Python  
- Data Cleaning Techniques  
- Data Visualization  
- Modular Programming  
- Logging Implementation  
- Version Control using Git  

---

## 👩‍💻 Developed By

**Sakshi Asati**  
Python & Data Analysis  

---
