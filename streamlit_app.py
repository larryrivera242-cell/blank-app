import streamlit as st
import pandas as pd
import os
import datetime

st.title("Customer Scheduler")

# Input fields
customer = st.text_input("Customer Name")
date = st.date_input("Job Date")
hour = st.selectbox("Hour", list(range(1, 13)))
minute = st.selectbox("Minute", [0, 15, 30, 45])
ampm = st.radio("AM/PM", ["AM", "PM"], horizontal=True)

display_time = f"{hour:02d}:{minute:02d} {ampm}"

# Save job
if st.button("Save Job"):
    # Load existing schedule
    if os.path.exists("schedule.csv"):
        df = pd.read_csv("schedule.csv")
    else:
        df = pd.DataFrame(columns=["Customer", "Date", "Time"])

    # New entry
    new_entry = {"Customer": customer, "Date": str(date), "Time": display_time}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)

    # Save back to CSV
    df.to_csv("schedule.csv", index=False)
    st.success(f"✅ Job for {customer} scheduled on {date} at {display_time}")

# Load schedule
if os.path.exists("schedule.csv"):
    st.subheader("📅 View Scheduled Jobs")
    df = pd.read_csv("schedule.csv")
    df["Date"] = pd.to_datetime(df["Date"]).dt.date

    # Date filter dropdown
    unique_dates = sorted(df["Date"].unique())
    selected_date = st.selectbox("Select a date", unique_dates, index=len(unique_dates)-1)

    filtered_jobs = df[df["Date"] == selected_date]

    if not filtered_jobs.empty:
        st.table(filtered_jobs)
    else:
        st.info("No jobs scheduled for this date.")
