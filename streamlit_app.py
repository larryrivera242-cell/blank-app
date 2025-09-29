import streamlit as st

st.title("Customer Scheduler")
st.text_input("Customer Name")
st.time_input("Job Time")
import streamlit as st

st.subheader("Pick a time (12-hour)")
hour = st.selectbox("Hour", list(range(1, 13)))
minute = st.selectbox("Minute", [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
ampm = st.radio("AM/PM", ["AM", "PM"], horizontal=True)

display_time = f"{hour:02d}:{minute:02d} {ampm}"  # 12-hour string like "07:30 PM"
st.write("Selected:", display_time)

