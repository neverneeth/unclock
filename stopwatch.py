import asyncio
import streamlit as st
from datetime import datetime, timedelta


# CSS Styling for the time display
st.markdown(
    """
    <style>
    .time {
        font-size: 130px !important;
        font-weight: 700 !important;
        color: #ec5953 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state variables for stopwatch
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'elapsed_time' not in st.session_state:
    st.session_state.elapsed_time = timedelta()
if 'running' not in st.session_state:
    st.session_state.running = False

# Functions for stopwatch controls
def start():
    if not st.session_state.running:
        st.session_state.start_time = datetime.now()
        st.session_state.running = True

def stop():
    if st.session_state.running:
        st.session_state.elapsed_time += datetime.now() - st.session_state.start_time
        st.session_state.running = False

def reset():
    st.session_state.start_time = None
    st.session_state.elapsed_time = timedelta()
    st.session_state.running = False

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

# Async function to update the stopwatch display
async def update_display():
    while True:
        if st.session_state.running:
            current_time = datetime.now() - st.session_state.start_time + st.session_state.elapsed_time
        else:
            current_time = st.session_state.elapsed_time

        # Format and display elapsed time
        time_str = str(current_time).split(".")[0]  # Remove microseconds
        time_display.markdown(
            f"<p class='time'>{time_str}</p>", unsafe_allow_html=True
        )

        await asyncio.sleep(0.1)  # Update every 0.1 seconds

# Run the async update_display function
asyncio.run(update_display())
