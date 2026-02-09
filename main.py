import logging
import student_data
import preprocessed
import visualization
from logger_config import setup_logger

# Setup logger once
setup_logger()

def main_menu():
    logging.info("Entered Main Menu")

    while True:
        print("\n===== Mini Project Main Menu =====")
        print("1. Student CSV Operations (student_data)")
        print("2. Preprocessing Cleaned CSV (preprocessed)")
        print("3. Visualization of Cleaned CSV (visualization)")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")
        logging.info(f"User selected option: {choice}")

        if choice == "1":
            logging.info("Opening Student CSV Menu")
            student_data.menu()

        elif choice == "2":
            logging.info("Opening Preprocessing Menu")
            preprocessed.menu()

        elif choice == "3":
            logging.info("Opening Visualization Menu")
            visualization.menu()

        elif choice == "4":
            logging.info("Application exited by user")
            print("Exiting Mini Project. Goodbye!")
            break

        else:
            logging.warning("Invalid choice entered")
            print("❌ Invalid choice! Please enter 1-4.")


if __name__ == "__main__":
    main_menu()
