import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Initialize session state for dark mode if not set
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = True  # Default to dark mode

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Quiz", "Progress", "Dashboard"])

# Dark Mode Toggle
dark_mode_toggle = st.sidebar.checkbox("☀️ Light Mode", value=not st.session_state.dark_mode)
if dark_mode_toggle:
    st.session_state.dark_mode = False
    st.markdown("""
        <style>
            body {
                background-color: white;
                color: black;
            }
            .stApp {
                background-color:rgb(208, 183, 250);
                color: black;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.session_state.dark_mode = True
    st.markdown("""
        <style>
            body {
                background-color: #1e1e1e;
                color: white;
            }
            .stApp {
                background-color: #1e1e1e;
            }
        </style>
    """, unsafe_allow_html=True)
# Home Page
if page == "Home":
    st.title("🌱 Growth Mindset Challenge")
    st.subheader("Believe in Growth, Learn from Challenges!")
    
    st.write("""
    A **Growth Mindset** means believing that your abilities can be improved through learning and persistence. 
    Every challenge is an opportunity to grow! 🌟
    """)
    
    motivation_messages = [
        "Mistakes help us learn. Keep going! 💪",
        "Challenges make you stronger! 🚀",
        "Effort leads to success. Stay persistent! 🔥",
        "Learning never stops! Keep exploring. 📚",
        "Believe in yourself and keep growing! 🌱"
    ]
    
    if st.button("💡 Get a Motivation Boost!"):
        st.success(random.choice(motivation_messages))
    
    # User Input for Learning Goals
    st.subheader("📌 Set Your Learning Goal")
    goal = st.text_input("What new skill or habit do you want to develop?")
    if goal:
        st.write(f"Awesome! Keep working on `{goal}` and stay consistent! 🎯")
    
    # Habit Tracker
    st.subheader("📆 Track Your Progress")
    tracker = st.checkbox("Mark today's learning as complete")
    if tracker:
        st.success("Great job! Keep the streak going! 🔥")

# Quiz Page
elif page == "Quiz":
    st.title("🧠 Growth Mindset Quiz")
    
    questions = {
        "Failure is:": ["The end of the road", "A learning opportunity"],
        "Challenges are:": ["Something to avoid", "Opportunities to grow"],
        "Effort is:": ["Pointless", "Essential for improvement"]
    }
    
    score = 0
    responses = []
    
    for q, options in questions.items():
        answer = st.radio(q, options)
        responses.append(1 if answer == options[1] else 0)
    
    if st.button("📊 See My Growth Mindset Score"):
        score = sum(responses)
        st.success(f"Your Growth Mindset Score: {score} / {len(questions)} 🎉")
        
        st.session_state["quiz_score"] = score
        st.session_state["responses"] = responses
        st.session_state["last_attempt"] = datetime.date.today()
        
        if score == len(questions):
            st.write("You have a strong growth mindset! Keep it up! 🚀")
        else:
            st.write("Keep practicing a growth mindset! Every step matters. 🌱")

# Progress Page (Visualization)
elif page == "Progress":
    st.title("📈 Your Growth Mindset Progress")
    
    questions = {
        "Failure is:": ["The end of the road", "A learning opportunity"],
        "Challenges are:": ["Something to avoid", "Opportunities to grow"],
        "Effort is:": ["Pointless", "Essential for improvement"]
    }
    
    if "quiz_score" in st.session_state:
        df = pd.DataFrame({
            "Questions": list(questions.keys()),
            "Score": st.session_state["responses"]
        })
        
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(df["Questions"], df["Score"], color=["#4caf50" if x else "#f44336" for x in df["Score"]])
        ax.set_ylabel("Correct Answers")
        ax.set_title("Growth Mindset Quiz Results")
        ax.set_ylim(0, 1)
        
        st.pyplot(fig)
    else:
        st.warning("Take the quiz first to see your progress!")
    
    # Achievement Badges
    if "quiz_score" in st.session_state:
        st.subheader("🏆 Achievements")
        if st.session_state["quiz_score"] == len(questions):
            st.success("Congratulations! You've achieved a perfect score! 🏆")
# Dashboard Page (Personalized)
elif page == "Dashboard":
    st.title("📊 My Personalized Dashboard")
    
    questions = {
        "Failure is:": ["The end of the road", "A learning opportunity"],
        "Challenges are:": ["Something to avoid", "Opportunities to grow"],
        "Effort is:": ["Pointless", "Essential for improvement"]
    }
    
    if "quiz_score" in st.session_state:
        st.metric("📊 Last Quiz Score", f"{st.session_state['quiz_score']} / {len(questions)}")
        st.metric("📅 Last Quiz Attempt", f"{st.session_state['last_attempt']}")
    
    # Learning Streak Tracker
    if "learning_streak" not in st.session_state:
        st.session_state["learning_streak"] = 0
    
    streak_update = st.button("🔥 Keep My Streak Going!")
    if streak_update:
        st.session_state["learning_streak"] += 1
        st.success(f"Streak Updated! Current Streak: {st.session_state['learning_streak']} days! 🔥")
    
    st.metric("🔥 Learning Streak", f"{st.session_state['learning_streak']} days")
    
    # Social Sharing
    st.subheader("📢 Share Your Progress")
    st.write("Copy the link below to share your progress with friends!")
    st.code("https://yourapp.com/share")
    st.metric("🔥 Learning Streak", f"{st.session_state['learning_streak']} days")
    
    # Social Sharing
    st.subheader("📢 Share Your Progress")
    st.write("Copy the link below to share your progress with friends!")
    st.code("https://yourapp.com/share")
    
# Footer
st.write("---")
st.write("*Keep pushing forward, learning, and improving every day!* 💡🚀")



