import streamlit as st
import pandas as pd
import os

st.title("Customer Scheduler")

# Input fields
customer = st.text_input("Customer Name")
date = st.date_input("Job Date")  # New date picker
hour = st.selectbox("Hour", list(range(1, 13)))
minute = st.selectbox("Minute", [0, 15, 30, 45])
ampm = st.radio("AM/PM", ["AM", "PM"], horizontal=True)

display_time = f"{hour:02d}:{minute:02d} {ampm}"

# Save button
if st.button("Save Job"):
    # Load existing data if file exists
    if os.path.exists("schedule.csv"):
        df = pd.read_csv("schedule.csv")
    else:
        df = pd.DataFrame(columns=["Customer", "Date", "Time"])

    # Add new row
    new_entry = {"Customer": customer, "Date": str(date), "Time": display_time}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)

    # Save back to CSV
    df.to_csv("schedule.csv", index=False)

    st.success(f"Job for {customer} scheduled on {date} at {display_time}")

# Show saved schedule
if os.path.exists("schedule.csv"):
    st.subheader("All Scheduled Jobs")
    df = pd.read_csv("schedule.csv")
    st.table(df)
