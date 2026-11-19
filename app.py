from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

workouts = {
    "weight_loss": {
        "title": "Fat Loss Workout",
        "description": "A cardio and strength routine to improve fitness.",
        "days": [
            {"day": "Monday", "exercises": ["Jumping Jacks - 3 × 30", "Squats - 3 × 15", "Walking - 20 min"]},
            {"day": "Tuesday", "exercises": ["Push-ups - 3 × 10", "Mountain Climbers - 3 × 20", "Plank - 3 × 30 sec"]},
            {"day": "Wednesday", "exercises": ["Brisk Walk - 30 min", "Lunges - 3 × 12", "Crunches - 3 × 15"]},
            {"day": "Thursday", "exercises": ["Rest or light stretching"]},
            {"day": "Friday", "exercises": ["Squats - 3 × 15", "Burpees - 3 × 10", "Plank - 3 × 40 sec"]},
            {"day": "Saturday", "exercises": ["Cycling - 20 min", "Push-ups - 3 × 10", "Walking - 15 min"]},
            {"day": "Sunday", "exercises": ["Rest and recovery"]}
        ]
    },

    "muscle_gain": {
        "title": "Muscle Building Workout",
        "description": "A strength routine designed to build muscle gradually.",
        "days": [
            {"day": "Monday", "exercises": ["Push-ups - 4 × 12", "Dumbbell Shoulder Press - 3 × 10", "Triceps Dips - 3 × 10"]},
            {"day": "Tuesday", "exercises": ["Squats - 4 × 12", "Lunges - 3 × 12", "Calf Raises - 3 × 15"]},
            {"day": "Wednesday", "exercises": ["Pull-ups or Assisted Pull-ups - 3 sets", "Dumbbell Rows - 3 × 12", "Biceps Curls - 3 × 12"]},
            {"day": "Thursday", "exercises": ["Rest and recovery"]},
            {"day": "Friday", "exercises": ["Push-ups - 3 × 12", "Shoulder Press - 3 × 10", "Dumbbell Fly - 3 × 12"]},
            {"day": "Saturday", "exercises": ["Squats - 3 × 12", "Plank - 3 × 40 sec", "Light cardio - 15 min"]},
            {"day": "Sunday", "exercises": ["Rest"]}
        ]
    },

    "fitness": {
        "title": "General Fitness Workout",
        "description": "A balanced plan for general fitness and movement.",
        "days": [
            {"day": "Monday", "exercises": ["Walking - 20 min", "Squats - 3 × 12", "Push-ups - 3 × 8"]},
            {"day": "Tuesday", "exercises": ["Cycling - 20 min", "Plank - 3 × 30 sec"]},
            {"day": "Wednesday", "exercises": ["Stretching - 15 min", "Walking - 20 min"]},
            {"day": "Thursday", "exercises": ["Lunges - 3 × 10", "Push-ups - 3 × 10", "Crunches - 3 × 12"]},
            {"day": "Friday", "exercises": ["Jogging - 20 min", "Squats - 3 × 12"]},
            {"day": "Saturday", "exercises": ["Full body workout - 30 min"]},
            {"day": "Sunday", "exercises": ["Rest"]}
        ]
    }
}


@app.route("/")
def home():
    return render_template("index.html", workouts=workouts)


@app.route("/bmi", methods=["POST"])
def bmi():
    data = request.get_json()

    height = float(data.get("height", 0))
    weight = float(data.get("weight", 0))

    if height <= 0 or weight <= 0:
        return jsonify({"error": "Please enter valid height and weight."}), 400

    height_m = height / 100
    bmi_value = weight / (height_m * height_m)

    if bmi_value < 18.5:
        category = "Underweight"
    elif bmi_value < 25:
        category = "Normal range"
    elif bmi_value < 30:
        category = "Overweight"
    else:
        category = "Obesity range"

    return jsonify({
        "bmi": round(bmi_value, 1),
        "category": category
    })


@app.route("/generate-workout", methods=["POST"])
def generate_workout():
    data = request.get_json()
    goal = data.get("goal", "fitness")

    if goal not in workouts:
        goal = "fitness"

    return jsonify(workouts[goal])


@app.route("/diet")
def diet():
    diet_plan = {
        "Breakfast": [
            "Oats with milk and banana",
            "Eggs with whole wheat bread",
            "Poha with peanuts"
        ],
        "Lunch": [
            "Rice or roti",
            "Dal",
            "Seasonal vegetables",
            "Curd"
        ],
        "Snack": [
            "Fruit",
            "Roasted chana",
            "Peanuts"
        ],
        "Dinner": [
            "Roti",
            "Paneer or dal",
            "Vegetables",
            "Salad"
        ]
    }

    return jsonify(diet_plan)


if __name__ == "__main__":
    app.run(debug=True)