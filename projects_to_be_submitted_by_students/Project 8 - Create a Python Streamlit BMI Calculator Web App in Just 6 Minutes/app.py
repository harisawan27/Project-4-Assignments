import streamlit as st

def compute_body_index(mass, stature):
    index = mass / (stature ** 2)
    return index

def assess_index(index):
    if index < 18.5:
        return "Your body mass is below the healthy range."
    elif 18.5 <= index < 24.9:
        return "You're in a healthy weight zone!"
    elif 25 <= index < 29.9:
        return "You're carrying a few extra pounds."
    else:
        return "Your BMI indicates obesity."

def app():
    st.title("Body Mass Index Checker 💡")

    mass = st.number_input("Input your weight in kilograms:", min_value=1.0, max_value=500.0, step=0.1)
    stature = st.number_input("Input your height in meters:", min_value=0.5, max_value=3.0, step=0.01)

    if st.button("Check My BMI"):
        index = compute_body_index(mass, stature)
        st.write(f"Calculated BMI: **{index:.2f}**")

        result = assess_index(index)
        st.write(result)

        if index < 18.5:
            st.info("You're underweight. A health consultation might help.")
        elif 18.5 <= index < 24.9:
            st.success("Nice! You're in great shape.")
        elif 25 <= index < 29.9:
            st.warning("Slightly above ideal weight. Consider reviewing your lifestyle.")
        else:
            st.error("BMI suggests obesity. Please talk to a healthcare professional.")

if __name__ == "__main__":
    app()
