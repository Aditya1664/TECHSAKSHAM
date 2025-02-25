# workout.py
class Workout:
    def __init__(self, date, exercise_type, duration, calories_burned):
        self.date = date
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date}: {self.exercise_type} for {self.duration} minutes, {self.calories_burned} calories burned"
