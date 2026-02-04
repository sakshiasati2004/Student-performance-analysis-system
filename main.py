# main.py
import student_data   # Module for raw student CSV operations
import preprocessed    # Module for cleaning CSV
import visualization   # Module for visualizing cleaned CSV

def main_menu():
    while True:
        print("\n===== Mini Project Main Menu =====")
        print("1. Student CSV Operations (student_data)")
        print("2. Preprocessing Cleaned CSV (preprocessed)")
        print("3. Visualization of Cleaned CSV (visualization)")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            # Call student_data menu only when user selects this
            student_data.menu()
        elif choice == "2":
            # Call preprocessed menu only when user selects this
            preprocessed.menu()
        elif choice == "3":
            # Call visualization menu only when user selects this
            visualization.menu()
        elif choice == "4":
            print("Exiting Mini Project. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-4.")

# ===== Start Program Only if Directly Run =====
if __name__ == "__main__":
    main_menu()
