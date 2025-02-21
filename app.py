#streamlit
import streamlit as st

st.set_page_config(page_title = "growth mindset project", project_icon="")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements!")

#qoute section
st.header("Today's Growth Mindset Qoute")
st.write("Success is not final,failure is not fatal:it is the courage to continue that counts._Winston Churchill")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
    st.success(f"you are facing: {user_input}. Keep pushing forward towards your goal!")
    else:
        st.warning("Tell us about your challenge to get started!")

        #reflecting
        st.header("Reflect on Your Learning")
        reflection = st.text_area("Reflect on Your Learning")
        reflection = st.text_area("Write your reflections here:")

        if reflection:
            st.success(f"Great Insight! Your reflection: {reflection}")
            else:
                st.info("Reflecting on past experience help you grow! Share your Share your difficulties")

                #acheviments
                st.header("Celebrates Your Win!")
                acheivment = st.text_input("Share something you've recently accomplished:")

                if acheivment:
                    st.success(f"Amazing! You achieved: {acheivment}")
                    else:
                        st.info("Big or small , every acheivements counts! Share one now!")

                        #footer
                        st.write("- - -")
                        st.write("Keep believing in yourself. Growth is a journey, not a destination! ")
                        st.write("Created By Zeenat Yameen")