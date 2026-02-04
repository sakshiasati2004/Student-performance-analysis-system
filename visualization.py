import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===== Setup =====
PROJECT_FOLDER = "/home/sakshi-asati/Desktop/python/Mini_project"
PLOTS_FOLDER = os.path.join(PROJECT_FOLDER, "plots")
os.makedirs(PLOTS_FOLDER, exist_ok=True)  # Create folder if it doesn't exist

DATA_FOLDER = os.path.join(PROJECT_FOLDER, "data")
CLEANED_FILE = os.path.join(DATA_FOLDER, "Cleaned_data_student.csv")

# Check if file exists
if not os.path.exists(CLEANED_FILE):
    print(f"❌ Cleaned CSV file not found at {CLEANED_FILE}. Run preprocessing first.")
    exit()

# Read cleaned CSV
df = pd.read_csv(CLEANED_FILE)

# Add total score column for convenience
df['Total_Score'] = df[['Exam_Score', 'Assignment_Score', 'Project_Score']].sum(axis=1)

# Set Seaborn style
sns.set_style("whitegrid")

# ===== Functions for plots =====
def average_score_by_grade():
    avg_total = df.groupby('Grade')['Total_Score'].mean().sort_index()
    plt.figure(figsize=(8,5))
    sns.barplot(x=avg_total.index, y=avg_total.values, palette="viridis")
    plt.title("Average Total Score by Grade")
    plt.xlabel("Grade")
    plt.ylabel("Average Total Score")
    plt.tight_layout()
    save_path = os.path.join(PLOTS_FOLDER, "avg_total_score_by_grade.png")
    plt.savefig(save_path)
    try:
        plt.show()
    except:
        print(f"✔ Plot saved as {save_path}")

def top_10_students():
    top_df = df.sort_values('Total_Score', ascending=False).head(10)
    plt.figure(figsize=(10,5))
    sns.barplot(x='Name', y='Total_Score', data=top_df, palette="coolwarm")
    plt.title("Top 10 Students by Total Score")
    plt.xlabel("Student Name")
    plt.ylabel("Total Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_path = os.path.join(PLOTS_FOLDER, "top_10_students.png")
    plt.savefig(save_path)
    try:
        plt.show()
    except:
        print(f"✔ Plot saved as {save_path}")

def histogram_total_score():
    plt.figure(figsize=(8,5))
    sns.histplot(df['Total_Score'], bins=10, kde=True, color="skyblue")
    plt.title("Histogram of Total Scores")
    plt.xlabel("Total Score")
    plt.ylabel("Count")
    plt.tight_layout()
    save_path = os.path.join(PLOTS_FOLDER, "histogram_total_score.png")
    plt.savefig(save_path)
    try:
        plt.show()
    except:
        print(f"✔ Plot saved as {save_path}")

def boxplot_score_by_grade():
    plt.figure(figsize=(8,5))
    sns.boxplot(x='Grade', y='Total_Score', data=df, palette="Set2")
    plt.title("Boxplot of Total Score by Grade")
    plt.xlabel("Grade")
    plt.ylabel("Total Score")
    plt.tight_layout()
    save_path = os.path.join(PLOTS_FOLDER, "boxplot_total_score_by_grade.png")
    plt.savefig(save_path)
    try:
        plt.show()
    except:
        print(f"✔ Plot saved as {save_path}")

def attendance_vs_total_score():
    plt.figure(figsize=(8,5))
    sns.scatterplot(x='Attendance', y='Total_Score', data=df, hue='Grade', palette="Set1", s=100)
    plt.title("Attendance vs Total Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Total Score")
    plt.legend(title='Grade')
    plt.tight_layout()
    save_path = os.path.join(PLOTS_FOLDER, "attendance_vs_total_score.png")
    plt.savefig(save_path)
    try:
        plt.show()
    except:
        print(f"✔ Plot saved as {save_path}")

# ===== Menu =====
def menu():
    while True:
        print("\n===== Student Performance Visualization Menu =====")
        print("1. Average Total Score by Grade")
        print("2. Top 10 Students by Total Score")
        print("3. Histogram of Total Scores")
        print("4. Boxplot of Total Score by Grade")
        print("5. Attendance vs Total Score")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")

        if choice == '1':
            average_score_by_grade()
        elif choice == '2':
            top_10_students()
        elif choice == '3':
            histogram_total_score()
        elif choice == '4':
            boxplot_score_by_grade()
        elif choice == '5':
            attendance_vs_total_score()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    menu()
