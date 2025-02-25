# workout_manager.py
from workout import Workout

def add_workout(user):
    date = input("Enter the date (YYYY-MM-DD): ")
    exercise_type = input("Enter the exercise type: ")
    duration = int(input("Enter the duration (minutes): "))
    calories_burned = int(input("Enter the calories burned: "))
    workout = Workout(date, exercise_type, duration, calories_burned)
    user.add_workout(workout)
    print("Workout added successfully!")

def view_workouts(user):
    print(f"{user.name}'s Workouts:")
    user.view_workouts()

def save_data(user):
    filename = input("Enter the filename to save data: ")
    user.save_data(filename)
    print("Data saved successfully!")

def load_data(user):
    filename = input("Enter the filename to load data: ")
    user.load_data(filename)
    print("Data loaded successfully!")
