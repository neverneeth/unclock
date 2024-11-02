import streamlit as st
from datetime import datetime, timedelta
import time
import random
import units

# CSS Styling for the time display
st.markdown(
    """
    <style>
    .time {
        font-size: 130px !important;
        font-weight: 700 !important;
        color: #ec5953 !important;
    }
    .unit {
        font-size: 40px !important;
        font-weight: 700 !important;
        color: #ec5953 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Functions for stopwatch controls
def start():
    if not st.session_state.running:
        st.session_state.start_time = datetime.now()
        st.session_state.running = True
        st.session_state.unit, st.session_state.unitname = pick_unit()

def stop():
    if st.session_state.running:
        st.session_state.elapsed_time += datetime.now() - st.session_state.start_time
        st.session_state.running = False

def reset():
    st.session_state.start_time = None
    st.session_state.elapsed_time = timedelta()
    st.session_state.running = False

def pick_unit():
    unit_name = random.choice(units.unit_list)
    unit_val = units.unit_dict.get(unit_name, 0.1)  
    return unit_val, unit_name


# Initialize session state variables for stopwatch
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'elapsed_time' not in st.session_state:
    st.session_state.elapsed_time = timedelta()
if 'running' not in st.session_state:
    st.session_state.running = False
if 'unit' not in st.session_state:
    st.session_state.unit, st.session_state.unitname = pick_unit()
    st.session_state.unitname = ""


# Stopwatch display
time_display = st.empty()
col1, col2, col3 = st.columns(3)
# Button controls
with col1:
    if st.button("Start"):
        start()
with col2:
    if st.button("Stop"):
        stop()
with col3:
    if st.button("Reset"):
        reset()



# Update the stopwatch display in real-time
while True:
    if st.session_state.running:
        # Calculate current elapsed time
        current_time = datetime.now() - st.session_state.start_time + st.session_state.elapsed_time
    else:
        current_time = st.session_state.elapsed_time
    displayed_time = int((current_time.total_seconds()) // st.session_state.unit)
    # Format and display elapsed time without microseconds
    time_str = str(displayed_time)
    time_display.markdown(
        f"""<p class='time'>
        {time_str} <span class='unit'>{st.session_state.unitname}</span>
    </p>
    """, unsafe_allow_html=True
    )

    # Refresh every 0.1 seconds
    time.sleep(0.5)
