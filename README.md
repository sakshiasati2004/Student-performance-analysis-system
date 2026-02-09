🎓 Student Performance Analysis System (Mini Project)
📌 Project Overview

The Student Performance Analysis System is a Python-based mini project designed to manage, preprocess, analyze, and visualize student performance data using CSV handling, Pandas, and data visualization libraries.

This project demonstrates concepts of:

File Handling

Data Validation

Data Cleaning

Data Analysis

Data Visualization

Logging

Git & Version Control

📂 Project Structure
Mini_project/
│
├── data/
│   ├── data_student.csv
│   └── Cleaned_data_student.csv
│
├── plots/
│   └── (Generated PNG charts)
│
├── student-data.py
├── preprocessing.py
├── visualization.py
├── logger_config.py
├── main.py
├── project_log.txt
└── README.md

🧩 Modules Description
1️⃣ student-data.py

Creates and manages student CSV dataset

Provides input validation

Supports:

Write (default 50 rows or manual entry)

Read

Append

Ensures proper data integrity

2️⃣ preprocessing.py

Cleans dataset

Handles:

Duplicate values

Missing values

Data formatting

Generates cleaned dataset for analysis

3️⃣ visualization.py

Generates multiple charts using Matplotlib & Seaborn:

📊 Average Total Score by Grade

🏆 Top 10 Students

📈 Histogram of Total Scores

📦 Boxplot by Grade

📉 Attendance vs Total Score

All plots are saved as .png files in the plots/ folder.

4️⃣ logger_config.py

Implements logging system

Stores application activity logs in:

project_log.txt


Logs important operations and events

5️⃣ main.py

Acts as entry point

Integrates:

Data handling

Preprocessing

Visualization

Logging

🛠 Technologies Used

Python

CSV Module

Pandas

Matplotlib

Seaborn

OS Module

Logging Module

Git & GitHub

🚀 Features

✔ CSV file creation and management
✔ Manual and default data entry
✔ Input validation system
✔ Duplicate and missing value handling
✔ Data preprocessing
✔ Data visualization
✔ Logging system
✔ Menu-driven interface
✔ Git version control with branches

📊 Key Functionalities

Total Score Calculation

Performance Level Classification

Grade-wise Analysis

Attendance vs Performance Analysis

Automatic Plot Saving

🔁 Git Workflow Used

Repository Initialization

Branch Creation for Features

Merging into Main Branch

Version Control using GitHub

🎯 Learning Outcomes

Through this project, the following concepts were implemented:

File Handling

Data Cleaning Techniques

GroupBy & Aggregation

Data Visualization

Logging Implementation

Git Branching & Merging

Modular Programming

▶️ How to Run

Clone the repository:

git clone <repository-link>


Navigate to project folder:

cd Mini_project


Run main file:

python main.py

👩‍💻 Developed By

Sakshi Asati
Mini Project – Python & Data Analysis