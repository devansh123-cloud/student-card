students = {}

while True:
    print("\n📘 Student Menu")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_number = input("Enter roll number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Student Marks: ")
        grade = input("Enter Student Grade: ")

        students[roll_number] = {
            "name": name,
            "marks": marks,
            "grade": grade
        }

        print("✅ Student added successfully!")

    elif choice == "2":
        search_roll = input("Enter Roll Number to search: ")

        if search_roll in students:
            print("👨‍🎓 Student Found:")
            print(f"Name: {students[search_roll]['name']}")
            print(f"Marks: {students[search_roll]['marks']}")
            print(f"Grade: {students[search_roll]['grade']}")
        else:
            print("❌ Student not found.")

    elif choice == "3":
        print("👋 Exiting...")
        break

    else:
        print("Invalid choice.")
