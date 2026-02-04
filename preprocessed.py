# preprocessed.py
import os
import pandas as pd

# ===== Setup =====
DATA_FOLDER = "/home/sakshi-asati/Desktop/python/Mini_project/data"
os.makedirs(DATA_FOLDER, exist_ok=True)

RAW_FILE = os.path.join(DATA_FOLDER, "data_student.csv")
CLEAN_FILE = os.path.join(DATA_FOLDER, "Cleaned_data_student.csv")

# ===== Load CSV =====
if not os.path.exists(RAW_FILE):
    print(f"❌ {RAW_FILE} not found! Please run your student_data.py first to create it.")
    exit()

df = pd.read_csv(RAW_FILE)

# ===== Preprocessing Functions =====

def handle_missing_values():
    """
    Handles missing values:
    - Numerical columns: replace NaN with mean
    - Categorical columns: replace NaN with mode[0]
    """
    global df
    null_cols = df.columns[df.isnull().any()].tolist()
    if not null_cols:
        print("✔ No missing values found.")
        return

    print(f"⚠ Missing values found in columns: {null_cols}")

    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            if df[col].isnull().any():
                mean_val = df[col].mean()
                df[col].fillna(mean_val, inplace=True)
                print(f"  -> Filled missing numerical values in '{col}' with mean: {mean_val:.2f}")
        else:
            if df[col].isnull().any():
                mode_val = df[col].mode()[0]
                df[col].fillna(mode_val, inplace=True)
                print(f"  -> Filled missing categorical values in '{col}' with mode: {mode_val}")

    df.to_csv(CLEAN_FILE, index=False)
    print(f"✔ Missing values handled and saved to {CLEAN_FILE}\n")

def handle_duplicate_rows():
    """
    Removes fully duplicate rows and duplicate Roll_No.
    """
    global df
    initial_len = len(df)
    
    # Remove full duplicates
    df.drop_duplicates(inplace=True)
    
    # Remove duplicate Roll_No
    if 'Roll_No' in df.columns:
        df = df[df['Roll_No'].duplicated(keep='first') == False]

    removed = initial_len - len(df)
    if removed > 0:
        print(f"✔ Removed {removed} duplicate rows (including duplicate Roll_No).")
    else:
        print("✔ No duplicate rows or Roll_No duplicates found.")

    df.to_csv(CLEAN_FILE, index=False)
    print(f"✔ Updated cleaned CSV saved at {CLEAN_FILE}\n")

def convert_columns():
    """
    Ensures numeric columns are correct types and handles any non-numeric errors.
    """
    global df
    numeric_cols = ['Roll_No','Student_ID','Age','Attendance','Exam_Score',
                    'Assignment_Score','Project_Score','Study_Hours_per_Week']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df.to_csv(CLEAN_FILE, index=False)
    print(f"✔ Numeric conversion done and saved to {CLEAN_FILE}\n")

def handle_all():
    """
    Run all preprocessing steps in order.
    """
    convert_columns()       # Convert first to ensure numeric operations
    handle_missing_values()
    handle_duplicate_rows()
    print("✔ All preprocessing completed and saved.\n")

# ===== Menu =====
def menu():
    while True:
        print("\n===== Preprocessing Menu =====")
        print("1. Handle Missing Values")
        print("2. Handle Duplicate Rows / Roll_No Duplicates")
        print("3. Convert Columns to Numeric (if needed)")
        print("4. Run All Preprocessing")
        print("5. Read Cleaned CSV")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            handle_missing_values()
        elif choice == '2':
            handle_duplicate_rows()
        elif choice == '3':
            convert_columns()
        elif choice == '4':
            handle_all()
        elif choice == '5':
            if os.path.exists(CLEAN_FILE):
                print("\n===== Cleaned CSV =====")
                print(pd.read_csv(CLEAN_FILE))
            else:
                print("❌ Cleaned CSV not found. Run preprocessing first.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

# ===== Start Program Only if Directly Run =====
if __name__ == "__main__":
    menu()
