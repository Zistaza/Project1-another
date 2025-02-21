import streamlit as st

# Corrected page config
st.set_page_config(page_title="Unstoppable Mindset", page_icon="🔥")

st.title("🔥 Unstoppable Mindset: Unlock Your Full Potential 🚀")

st.header("💡 Welcome to Your Journey of Growth!")
st.write("Every challenge you face is a stepping stone toward greatness. This AI-powered app empowers you to embrace struggles, reflect on progress, and celebrate victories. 🌟")

# Powerful Quote Section
st.header("📢 Today's Power Quote")
st.write("💭 _Doubt kills more dreams than failure ever will._ – Suzy Kassem")

# User Challenge Input
st.header("🛑 What’s Holding You Back Today?")
user_input = st.text_input("💭 Describe a challenge you're currently facing:")

if user_input:
    st.success(f"✅ You're confronting: **{user_input}**. Remember, challenges shape champions—keep pushing forward! 💪🔥")
else:
    st.warning("⚡ Growth starts with awareness. Share your challenge and take the first step! 🏆")

# Reflection Section
st.header("🔄 Turn Struggles into Strength")
reflection = st.text_area("📝 What have you learned from your experiences?")

if reflection:
    st.success(f"💡 Powerful insight! Your reflection: **{reflection}** 🎯 Keep learning and evolving!")
else:
    st.info("🔍 Self-reflection fuels progress. Write down your thoughts and own your growth. 🚀")

# Achievements Section
st.header("🏆 Claim Your Victory!")
achievement = st.text_input("🎉 Share a recent success, big or small:")

if achievement:
    st.success(f"🔥 Incredible! You accomplished: **{achievement}** 🎯 Every win counts!")
else:
    st.info("🌟 Success is a habit—celebrate your progress, no matter how small! 🚀")

# Footer with Encouragement
st.write("---")
st.write("💪 **Your journey to greatness begins now. Keep moving forward!** 🚀🔥")
st.write("✨ **Created by Zeenat Yameen** ✨")
