// ===================================
// FITNESS WORKOUT GENERATOR
// ===================================

async function generateWorkout(goal) {
    const resultBox = document.getElementById("workout-result");
    const title = document.getElementById("workout-title");
    const description = document.getElementById("workout-description");
    const daysContainer = document.getElementById("workout-days");

    try {
        const response = await fetch("/generate-workout", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ goal: goal })
        });

        const data = await response.json();

        title.textContent = data.title;
        description.textContent = data.description;
        daysContainer.innerHTML = "";

        data.days.forEach(day => {
            const card = document.createElement("div");
            card.className = "day-card";

            const heading = document.createElement("h3");
            heading.textContent = day.day;

            const list = document.createElement("ul");

            day.exercises.forEach(exercise => {
                const li = document.createElement("li");
                li.textContent = exercise;
                list.appendChild(li);
            });

            card.appendChild(heading);
            card.appendChild(list);
            daysContainer.appendChild(card);
        });

        resultBox.classList.remove("hidden");
        resultBox.scrollIntoView({ behavior: "smooth" });

    } catch (error) {
        alert("Unable to load workout. Please try again.");
        console.error(error);
    }
}


// ===================================
// BMI CALCULATOR
// ===================================

async function calculateBMI() {
    const height = document.getElementById("height").value;
    const weight = document.getElementById("weight").value;
    const result = document.getElementById("bmi-result");

    if (!height || !weight || height <= 0 || weight <= 0) {
        alert("Please enter valid height and weight.");
        return;
    }

    try {
        const response = await fetch("/bmi", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                height: height,
                weight: weight
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "BMI calculation failed.");
        }

        result.innerHTML = `
            <h2>${data.bmi}</h2>
            <p>Your BMI Category: <strong>${data.category}</strong></p>
        `;

        result.classList.remove("hidden");

    } catch (error) {
        alert(error.message);
    }
}


// ===================================
// WATER TRACKER
// ===================================

let water = Number(localStorage.getItem("fitzone_water")) || 0;

function updateWater() {
    document.getElementById("water-count").textContent = water;

    const percentage = Math.min((water / 8) * 100, 100);

    document.getElementById("water-progress").style.width =
        percentage + "%";

    localStorage.setItem("fitzone_water", water);
}

function addWater() {
    if (water < 8) {
        water++;
        updateWater();
    } else {
        alert("Great! You have reached your 8-glass tracker goal.");
    }
}

function resetWater() {
    water = 0;
    updateWater();
}

updateWater();


// ===================================
// WORKOUT TRACKER
// ===================================

let workoutCount =
    Number(localStorage.getItem("fitzone_workouts")) || 0;

function updateWorkoutCount() {
    document.getElementById("workout-count").textContent = workoutCount;

    localStorage.setItem("fitzone_workouts", workoutCount);
}

function completeWorkout() {
    workoutCount++;
    updateWorkoutCount();
    alert("Workout completed! Keep going 💪");
}

function resetWorkout() {
    workoutCount = 0;
    updateWorkoutCount();
}

updateWorkoutCount();