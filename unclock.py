import streamlit as st
from datetime import datetime
import pytz
import random

st.title("UnClock App - The Useless Clock App")
st.sidebar.title("UnClock Features")

# Feature selection
feature = st.sidebar.radio("Choose a Feature", ("World Clock", "Stopwatch", "Timer", "Alarm"))

if feature == "World Clock":
    st.header("World Clock")

    # Initialize a list in session_state to keep track of added world clocks
    if "world_clocks" not in st.session_state:
        st.session_state["world_clocks"] = []

    # Function to generate random geographic coordinates
    def random_coordinates():
        latitude = round(random.uniform(-90.0, 90.0), 4)  # Latitude range
        longitude = round(random.uniform(-180.0, 180.0), 4)  # Longitude range
        return latitude, longitude

    # Button to add a new random timezone clock with geographic coordinates
    if st.button("Add +"):  # Renamed button
        # Limit the clocks to 5 entries; remove the oldest if the limit is reached
        if len(st.session_state["world_clocks"]) >= 5:
            st.session_state["world_clocks"].pop(0)

        # Get a random timezone for time calculation
        timezones = pytz.all_timezones
        random_timezone = random.choice(timezones)
        
        # Generate random geographic coordinates
        latitude, longitude = random_coordinates()
        
        # Append the coordinates and timezone to session_state
        st.session_state["world_clocks"].append({
            "coordinates": f"Lat: {latitude}, Long: {longitude}",
            "timezone": random_timezone
        })

    # Display each world clock in a separate tile
    for clock in st.session_state["world_clocks"]:
        with st.container():
            # Get the current time for the specific timezone
            now = datetime.now(pytz.timezone(clock["timezone"]))
            formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
            
            st.markdown(f"""
            <div style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin: 5px 0;">
                <h4 style="color: #333;">{clock['coordinates']} </h4>
                <p style="color: #555;">
                    {formatted_time}
                </p>
            </div>
            """, unsafe_allow_html=True)

elif feature == "Timer":
    st.header("Timer")
    # Code for Timer will go here

elif feature == "Alarm":
    st.header("Alarm")
    # Code for Alarm will go here
