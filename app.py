import streamlit as st
from datetime import datetime, timedelta, date

st.title("BloodDonorNetwork - Register")

role = st.radio("I am a...", ["Donor", "Need Blood"])
name = st.text_input("Full Name")
email = st.text_input("Email")
mobile = st.text_input("Mobile Number")
#password = st.text_input("Create Password", type="password")
#confirm = st.text_input("Confirm Password", type="password")
# DOB range logic
today = date.today()
min_dob = date(1950, 1, 1)
max_dob = date(today.year - 18, today.month, today.day)

dob = st.date_input(
    "Date of Birth",
    min_value=min_dob,
    max_value=max_dob,
    value=date(2000, 1, 1)
)

blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
last_donation = st.date_input("Last Blood Donation Date")

health_check = st.multiselect("Health Check (select all that apply)",
    ["No recent fever", "No chronic illnesses", "No infectious diseases"])

address = st.text_input("Address or Pincode")
city = st.selectbox("City", ["Mumbai", "Delhi", "Bangalore", "Chennai"])  # Add more

if role == "Need Blood":
    hospital = st.text_input("Hospital Name")
    urgency = st.radio("Urgency", ["Standard", "Urgent"])

consent = st.checkbox("I agree to share my info for donation matching")

if st.button("Submit & Go to Map"):
    # Age check using updated dob
    if dob > max_dob:
        st.error("Must be 18 or older to donate or request blood")
    elif datetime.now().date() - last_donation < timedelta(days=56) and role == "Donor":
        st.warning("Not eligible to donate until 56 days from last donation")
    elif not consent:
        st.warning("You must agree to proceed")
    else:
        # Write data to backend
        st.success("Submitted successfully! Go to map ➡")
        st.session_state['user'] = name
        st.switch_page("pages/map.py")  # or redirect logic
