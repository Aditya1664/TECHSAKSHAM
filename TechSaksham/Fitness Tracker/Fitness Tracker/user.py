# user.py
from workout import Workout

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_workouts(self):
        for workout in self.workouts:
            print(workout)

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for workout in self.workouts:
                # Save workout to file
                file.write(f"{workout.date},{workout.exercise_type},{workout.duration},{workout.calories_burned}\n")
                # Print the workout details after saving
                print(f"Saved workout: Date: {workout.date}, Exercise: {workout.exercise_type}, Time: {workout.duration} minutes, Calories burned: {workout.calories_burned}")
