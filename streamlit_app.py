import streamlit as st

st.title("Customer Scheduler")

# Customer Name
customer = st.text_input("Customer Name")

# Pick time in 12-hour format
hour = st.selectbox("Hour", list(range(1, 13)))
minute = st.selectbox("Minute", [0, 15, 30, 45])
ampm = st.radio("AM/PM", ["AM", "PM"], horizontal=True)

display_time = f"{hour:02d}:{minute:02d} {ampm}"

st.write("Selected Time:", display_time)

# Show summary
if customer:
    st.success(f"Job for {customer} scheduled at {display_time}")
