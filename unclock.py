import streamlit as st
from datetime import datetime
import pytz
import random

st.title("UnClock App - The Useless Clock App")

# Initialize a list in session_state to keep track of added world clocks
if "world_clocks" not in st.session_state:
    st.session_state["world_clocks"] = []

# Function to generate random geographic coordinates
def generate_random_coordinates():
    latitude = round(random.uniform(-90.0, 90.0), 4)  # Latitude range
    longitude = round(random.uniform(-180.0, 180.0), 4)  # Longitude range
    return latitude, longitude

# Button to add a new random timezone clock with geographic coordinates
if st.button("Add +"):
    # Limit the clocks to 5 entries; remove the oldest if the limit is reached
    if len(st.session_state["world_clocks"]) >= 5:
        st.session_state["world_clocks"].pop(0)

    # Get a random timezone for time calculation
    timezones = pytz.all_timezones
    random_timezone = random.choice(timezones)

    # Generate random geographic coordinates
    latitude, longitude = generate_random_coordinates()

    # Append the coordinates and timezone to session_state
    st.session_state["world_clocks"].append({
        "coordinates": f"Lat: {latitude}, Long: {longitude}",
        "timezone": random_timezone
    })

# Display each world clock in a separate tile
for clock in st.session_state["world_clocks"]:
    timezone = clock["timezone"]
    coordinates = clock["coordinates"]

    with st.container():
        st.markdown(f"""
        <div style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin: 5px 0;">
            <h4 style="color: #333;">{coordinates} ({timezone})</h4>
            <p style="color: #555;" id="time-{timezone}"></p>
        </div>
        """, unsafe_allow_html=True)

        # Function to update the clock display
        @st.cache_data
        def update_clock(timezone, element_id):
            current_time = datetime.now(pytz.timezone(timezone)).strftime('%Y-%m-%d %H:%M:%S')
            st.markdown(f"<p style='color: #555;' id='{element_id}'>{current_time}</p>", unsafe_allow_html=True)

        # Initial display
        update_clock(timezone, f"time-{timezone}")

        # Trigger a manual rerun after 1 second using a button
        if st.button("Refresh Clock", key=f"refresh-{timezone}"):
            pass  # Empty function to trigger a rerun