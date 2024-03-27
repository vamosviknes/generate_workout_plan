import streamlit as st

# Function to calculate BMI based on user's height and weight
def calculate_bmi(height, weight):
    # Convert height from cm to meters
    height_meters = height / 100
    # Calculate BMI
    bmi = weight / (height_meters ** 2)
    return bmi

# Function to determine BMI level or obesity status
def determine_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Function to generate workout plans for weight loss
def generate_workout_plan_weight_loss(days_per_week):
    workout_plan = {
        "Day 1": "Cardio (e.g., running)",
        "Day 2": "Strength (e.g., squats)",
        "Day 3": "HIIT (e.g., jumping jacks)",
        "Day 4": "Active Recovery (e.g., walking)",
        "Day 5": "Cardio (e.g., cycling)",
        "Day 6": "Circuit (e.g., mountain climbers)",
        "Day 7": "Rest"
    }
    return {day: workout_plan[day] for day in list(workout_plan.keys())[:days_per_week]}

# Function to generate workout plans for muscle gain
def generate_workout_plan_muscle_gain(days_per_week):
    workout_plan = {
        "Day 1": "Chest and Triceps\n- Bench Press\n- Dumbbell Flyes\n- Tricep Dips\n- Tricep Pushdowns",
        "Day 2": "Back and Biceps\n- Pull-Ups/Chin-Ups\n- Bent Over Rows\n- Barbell Curls\n- Hammer Curls",
        "Day 3": "Legs\n- Squats\n- Lunges\n- Leg Press\n- Leg Curls",
        "Day 4": "Shoulders and Abs\n- Shoulder Press\n- Lateral Raises\n- Front Raises\n- Planks\n- Russian Twists",
        "Day 5": "Rest or Active Recovery (Light Cardio, Stretching)",
        "Day 6": "Full Body Workout\n- Deadlifts\n- Push-Ups\n- Pull-Ups\n- Dumbbell Shoulder Press\n- Dumbbell Lunges",
        "Day 7": "Rest"
    }
    return {day: workout_plan[day] for day in list(workout_plan.keys())[:days_per_week]}

# Function to generate meal suggestions for weight loss
def generate_meal_suggestions_weight_loss():
    return {
        "Breakfast": "Oatmeal with berries, Avocado toast with poached egg",
        "Lunch": "Grilled chicken salad, Quinoa with roasted vegetables",
        "Dinner": "Salmon with steamed broccoli, Turkey chili with beans"
    }

# Function to generate meal suggestions for muscle gain
def generate_meal_suggestions_muscle_gain():
    return {
        "Breakfast": "Scrambled eggs with spinach and whole grain toast, Greek yogurt with fruit and nuts",
        "Lunch": "Grilled steak with sweet potatoes, Brown rice with black beans and grilled chicken",
        "Dinner": "Lean beef stir-fry with vegetables, Baked salmon with quinoa and roasted vegetables"
    }

# Function to generate dietary plan for weight loss
def generate_dietary_plan_weight_loss():
    return {
        "Protein": "Lean meats, fish, tofu",
        "Carbohydrates": "Whole grains, fruits, vegetables",
        "Healthy Fats": "Nuts, seeds, avocados",
        "Limit": "Sugary snacks, processed foods"
    }

# Function to generate dietary plan for muscle gain
def generate_dietary_plan_muscle_gain():
    return {
        "Protein": "Chicken breast, lean beef, eggs",
        "Carbohydrates": "Brown rice, quinoa, sweet potatoes",
        "Healthy Fats": "Nuts, olive oil, avocados",
        "Limit": "Added sugars, refined carbs"
    }

# Streamlit UI
def main():
    st.title("AI EmPower Fit")

    # User inputs for name, height, weight, and age
    name = st.text_input("Enter your name:")
    height = st.number_input("Enter your height (in centimeters):", min_value=50, max_value=300)
    weight = st.number_input("Enter your weight (in kilograms):", min_value=1, max_value=300)
    age = st.number_input("Enter your age:", min_value=1, max_value=150)

   
    # Calculate BMI and determine status
    if height and weight:
        bmi = calculate_bmi(height, weight)
        bmi_status = determine_bmi_status(bmi)
        st.write(f"Your BMI: {bmi:.2f} - {bmi_status}")

    # User inputs for workout goal and days per week
    workout_goal = st.selectbox("Select your workout goal:", ["Weight Loss", "Muscle Gain"])
    days_per_week = st.number_input("Enter number of days per week you can do exercise:", min_value=1, max_value=7, step=1)

    # Generate workout plan button
    if st.button("Generate Workout Plan"):
        # Call the appropriate function based on the selected workout goal
        if workout_goal == "Weight Loss":
            workout_plan = generate_workout_plan_weight_loss(days_per_week)
            meal_suggestions = generate_meal_suggestions_weight_loss()
            dietary_plan = generate_dietary_plan_weight_loss()
        elif workout_goal == "Muscle Gain":
            workout_plan = generate_workout_plan_muscle_gain(days_per_week)
            meal_suggestions = generate_meal_suggestions_muscle_gain()
            dietary_plan = generate_dietary_plan_muscle_gain()

        st.success("Generated Workout Plan:")
        
        # Create a table to display the workout plan
        st.write("Day", "Exercise")
        for day, exercise in workout_plan.items():
            st.write(day, exercise)

        # Add a gap line
        st.write("---")

        # Display meal suggestions
        st.header("Meal Suggestions:")
        for meal, suggestion in meal_suggestions.items():
            st.write(f"{meal}: {suggestion}")

        # Add a gap line
        st.write("---")

        # Display dietary plan
        st.header("Dietary Plan:")
        for nutrient, foods in dietary_plan.items():
            st.write(f"{nutrient}: {foods}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
