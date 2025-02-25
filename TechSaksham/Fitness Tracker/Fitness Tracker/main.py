# main.py
from user import User
from workout_manager import add_workout, view_workouts, save_data, load_data

name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))
user = User(name, age, weight)

while True:
    print("\n1. Add Workout")
    print("2. View Workouts")
    print("3. Save Data")
    print("4. Load Data")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_workout(user)
    elif choice == '2':
        view_workouts(user)
    elif choice == '3':
        save_data(user)
    elif choice == '4':
        load_data(user)
    elif choice == '5':
        print("Exited the program. GoodBye!!")
        break
    else:
        print("Invalid choice. Please try again.")
