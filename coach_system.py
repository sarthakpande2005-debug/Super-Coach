import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Dummy syllabus + weightage (Will be replaced later with real data)

exam_syllabi = {
    "JEE": {
        "Physics": 0.35,
        "Chemistry": 0.30,
        "Mathematics": 0.35
    },
    "NEET": {
        "Physics": 0.25,
        "Chemistry": 0.25,
        "Biology": 0.50
    },
    "CAT": {
        "Quantitative Aptitude": 0.40,
        "Verbal Ability": 0.30,
        "Logical Reasoning & DI": 0.30
    }
}


# App Layout

st.title("📘 Super Coach – Demo")
st.write("Your personalized AI exam coach prototype.")

# Input: Exam name
exam_name = st.selectbox("Select your Exam:", list(exam_syllabi.keys()))

# Input: Time left until exam
days_left = st.number_input("Days left until exam:", min_value=1, value=30)

# Input: Hours per day available
hours_per_day = st.slider("Study hours per day:", 1, 12, 4)

if st.button("Generate Study Plan"):
    syllabus = exam_syllabi[exam_name]
    total_hours = days_left * hours_per_day

    # Distribute hours based on weightage
    study_plan = {subject: round(weight * total_hours) for subject, weight in syllabus.items()}

    df = pd.DataFrame(list(study_plan.items()), columns=["Subject", "Allocated Hours"])

    st.subheader("📊 Suggested Study Plan")
    st.dataframe(df)

    # Plot chart
    fig, ax = plt.subplots()
    ax.pie(df["Allocated Hours"], labels=df["Subject"], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

    # Export option
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Plan (CSV)", csv, "study_plan.csv", "text/csv")


# Mini Coach Chat (Currently hardcoded, will soon power it by an API)

st.subheader("💬 Talk to Your Coach")
user_input = st.text_input("Ask something (e.g., 'How should I start Physics?')")
if user_input:
    # Simulated ChatGPT response (stub)
    st.write("🤖 Coach:", f"That's a great question! For {exam_name}, start with the basics of high-weightage subjects. Consistency matters more than long hours.")
