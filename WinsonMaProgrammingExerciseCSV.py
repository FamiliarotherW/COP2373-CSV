import csv

def write_grades_to_csv():
    # Writes students grades
        num_students = int(input("Enter the number of students: "))
    
        with open('grades.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])
    
            for _ in range(num_students):
                first_name = input("First name: ")
                last_name = input("Last name: ")
                exam1 = int(input("Exam 1 grade: "))
                exam2 = int(input("Exam 2 grade: "))
                exam3 = int(input("Exam 3 grade: "))
                writer.writerow([first_name, last_name, exam1, exam2, exam3])
        print("Grades written to grades.csv")
        
def read_grades_from_csv():
    # Reads grades and then display
    try:
        with open('grades.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print("{:<15} {:<8} {:<8} {:<8}". format(*row))
    except FileNotFoundError:
        print("grades.csv not found. ")
        
def main():
    # Main function control program
    while True:
        print("\n. Write Grades")
        print("2. Read Grades")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            write_grades_to_csv()
        elif choice == '2':
            read_grades_from_csv()
        elif choice == '3':
            break
        else:
            print("Invalid choice. ")
            
if __name__ == "__main__":
    main()