import os
import csv

# ===== Setup =====
DATA_FOLDER = "/home/sakshi-asati/Desktop/python/Mini_project/data"
os.makedirs(DATA_FOLDER, exist_ok=True)
FILE_PATH = os.path.join(DATA_FOLDER, "data_student.csv")

# Create CSV with header if not present
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll_No","Student_ID","Name","Age","Attendance","Exam_Score",
                         "Assignment_Score","Project_Score","Study_Hours_per_Week",
                         "Grade","Performance_Level"])
    print(f"✔ CSV created at {FILE_PATH}\n")

# ===== Validation Functions =====
def get_positive_int(prompt, max_value=None):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            if value <= 0:
                print("❌ Must be positive!")
            elif max_value and value > max_value:
                print(f"❌ Cannot exceed {max_value}.")
            else:
                return value
        except ValueError:
            print("❌ Enter a numeric value.")

def get_positive_float(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
            if value < 0:
                print("❌ Must be positive!")
            else:
                return value
        except ValueError:
            print("❌ Enter a numeric value.")

def get_score(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
            if value < 0:
                print("❌ Must be positive!")
            elif value > 100:
                print("❌ Cannot exceed 100!")
            else:
                return value
        except ValueError:
            print("❌ Enter a numeric value.")

def get_name(prompt):
    while True:
        value = input(prompt)
        if any(char.isdigit() for char in value) or value.strip() == "":
            print("❌ Name cannot contain numbers or be empty.")
        else:
            return value.strip()

def get_grade(prompt):
    while True:
        value = input(prompt).upper()
        if value in ["A","B","C","D","E","F"]:
            return value
        else:
            print("❌ Grade must be between A and F.")

# ===== Core Functions =====
def write_student_data():
    print("\nWrite Options:")
    print("1. Default data (50 rows)")
    print("2. Enter manually")
    choice = input("Choice (1/2): ")

    if choice == "1":
        # ----- Full 50 rows with Roll_No and duplicates -----
        students = [
            ["Roll_No","Student_ID","Name","Age","Attendance","Exam_Score",
             "Assignment_Score","Project_Score","Study_Hours_per_Week",
             "Grade","Performance_Level"],

            [101,1,"Rahul",16,85,78,72,75,10,"B","Average"],
            [102,2,"Sakshi",15,90,88,90,92,14,"A","Good"],
            [103,3,"Aman",17,72,65,60,62,8,"C","Average"],
            [104,4,"Neha",16,80,75,70,72,9,"B","Average"],
            [105,5,"Rohit",18,95,92,94,96,16,"A","Good"],
            [106,6,"Pooja",17,60,55,50,48,6,"D","Poor"],
            [107,7,"Ankit",16,70,68,65,66,8,"C","Average"],
            [108,8,"Priya",15,88,84,86,88,13,"A","Good"],
            [109,9,"Karan",17,78,74,70,72,9,"B","Average"],
            [110,10,"Simran",16,82,79,76,78,11,"B","Average"],

            # Duplicate Roll Nos
            [101,11,"Rahul",16,85,78,72,75,10,"B","Average"],
            [103,12,"Aman",17,72,65,60,62,8,"C","Average"],

            # Some missing values
            [104,13,"Neha","",80,75,70,72,9,"B","Average"],
            [105,14,"Rohit",18,"",92,94,96,16,"A","Good"],
            [106,15,"Pooja",17,60,"",50,48,6,"D","Poor"],

            [107,16,"Ankit",16,70,68,65,66,8,"C","Average"],
            [108,17,"Priya",15,88,84,86,88,13,"A","Good"],
            [109,18,"Karan",17,78,74,70,72,9,"B","Average"],
            [110,19,"Simran",16,82,79,76,78,11,"B","Average"],
            [101,20,"Rahul",16,85,78,72,75,10,"B","Average"],

            [111,21,"Tina",16,90,89,87,88,12,"A","Good"],
            [112,22,"Vikram",17,77,73,70,74,9,"B","Average"],
            [113,23,"Meera",15,85,80,82,81,11,"B","Average"],
            [114,24,"Suresh",18,65,60,58,62,5,"D","Poor"],
            [115,25,"Anaya",16,92,90,91,94,15,"A","Good"],
            [116,26,"Kabir",17,70,68,65,66,8,"C","Average"],
            [117,27,"Riya",15,88,84,86,88,13,"A","Good"],
            [118,28,"Ishaan",16,78,74,70,72,9,"B","Average"],
            [119,29,"Sanya",17,82,79,76,78,11,"B","Average"],
            [120,30,"Arjun",16,85,78,72,75,10,"B","Average"],

            [101,31,"Rahul",16,85,78,72,75,10,"B","Average"],
            [104,32,"Neha",16,80,75,70,72,9,"B","Average"],
            [105,33,"Rohit",18,95,92,94,96,16,"A","Good"],
            [108,34,"Priya",15,88,84,86,88,13,"A","Good"],
            [109,35,"Karan",17,78,74,70,72,9,"B","Average"],
            [110,36,"Simran",16,82,79,76,78,11,"B","Average"],
            [111,37,"Tina",16,90,89,87,88,12,"A","Good"],
            [112,38,"Vikram",17,77,73,70,74,9,"B","Average"],
            [113,39,"Meera",15,85,80,82,81,11,"B","Average"],
            [114,40,"Suresh",18,65,60,58,62,5,"D","Poor"],
            [115,41,"Anaya",16,92,90,91,94,15,"A","Good"],
            [116,42,"Kabir",17,70,68,65,66,8,"C","Average"],
            [117,43,"Riya",15,88,84,86,88,13,"A","Good"],
            [118,44,"Ishaan",16,78,74,70,72,9,"B","Average"],
            [119,45,"Sanya",17,82,79,76,78,11,"B","Average"],
            [120,46,"Arjun",16,85,78,72,75,10,"B","Average"],
            [104,47,"Neha",16,80,75,70,72,9,"B","Average"],
            [105,48,"Rohit",18,95,92,94,96,16,"A","Good"],
            [108,49,"Priya",15,88,84,86,88,13,"A","Good"],
            [109,50,"Karan",17,78,74,70,72,9,"B","Average"],
        ]
        with open(FILE_PATH, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(students)
        print(f"✔ Default 50-row data written at {FILE_PATH}\n")

    elif choice == "2":
        rows = [["Roll_No","Student_ID","Name","Age","Attendance","Exam_Score",
                 "Assignment_Score","Project_Score","Study_Hours_per_Week",
                 "Grade","Performance_Level"]]
        n = get_positive_int("How many students? ")
        for i in range(n):
            print(f"\nStudent {i+1}:")
            roll_no = get_positive_int("Roll No: ")
            student_id = get_positive_int("Student ID: ")
            name = get_name("Name: ")
            age = get_positive_int("Age: ", max_value=100)
            attendance = get_score("Attendance (%): ")
            exam = get_score("Exam Score: ")
            assignment = get_score("Assignment Score: ")
            project = get_score("Project Score: ")
            study_hours = get_positive_float("Study Hours per Week: ")
            grade = get_grade("Grade (A-F): ")
            level = input("Performance Level: ")
            rows.append([roll_no, student_id, name, age, attendance, exam, assignment, project, study_hours, grade, level])
        with open(FILE_PATH, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"✔ Data saved manually at {FILE_PATH}\n")
    else:
        print("Invalid choice!\n")

def read_student_data():
    print("\nReading student data:\n")
    if not os.path.exists(FILE_PATH):
        print("File not found! Use Write option first.\n")
        return
    with open(FILE_PATH, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def append_student_data():
    print("\nAppend new student:")
    roll_no = get_positive_int("Roll No: ")
    student_id = get_positive_int("Student ID: ")
    name = get_name("Name: ")
    age = get_positive_int("Age: ", max_value=100)
    attendance = get_score("Attendance (%): ")
    exam = get_score("Exam Score: ")
    assignment = get_score("Assignment Score: ")
    project = get_score("Project Score: ")
    study_hours = get_positive_float("Study Hours per Week: ")
    grade = get_grade("Grade (A-F): ")
    level = input("Performance Level: ")
    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, student_id, name, age, attendance, exam, assignment, project, study_hours, grade, level])
    print("✔ Student appended successfully!\n")

def menu():
    while True:
        print("\n===== Student CSV Menu =====")
        print("1. Write")
        print("2. Read")
        print("3. Append")
        print("4. Exit")
        choice = input("Choice (1-4): ")
        if choice == "1":
            write_student_data()
        elif choice == "2":
            read_student_data()
        elif choice == "3":
            append_student_data()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    menu()
