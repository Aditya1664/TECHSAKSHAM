# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:44:32 2025

@author: doshi
"""

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)
        print(f"Workout '{workout}' added successfully.")

    def view_workouts(self):
        if not self.workouts:
            print("No workouts recorded yet.")
        else:
            print("\nYour Workouts:")
            for i, workout in enumerate(self.workouts, 1):
                print(f"{i}. {workout}")

    def save_data(self, filename="user_data.txt"):
        with open(filename, "w") as file:
            file.write(f"{self.name}\n{self.age}\n{self.weight}\n")
            for workout in self.workouts:
                file.write(f"{workout}\n")
        print("Data saved successfully.")

    def load_data(self, filename="user_data.txt"):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                self.name = lines[0].strip()
                self.age = int(lines[1].strip())
                self.weight = float(lines[2].strip())
                self.workouts = [line.strip() for line in lines[3:]]
                print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")


def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))

    user = User(name, age, weight)

    while True:
        print("\n1. Add Workout")
        print("2. View Workouts")
        print("3. Save Data")
        print("4. Load Data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            workout = input("Enter workout name: ")
            user.add_workout(workout)
        elif choice == "2":
            user.view_workouts()
        elif choice == "3":
            user.save_data()
        elif choice == "4":
            user.load_data()
        elif choice == "5":
            print("Exiting program. Have a great day!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
