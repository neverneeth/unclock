import asyncio
import streamlit as st
from datetime import datetime, timedelta
import pytz
import random

st.title("UnClock App - The Useless Clock App")
st.sidebar.title("UnClock Features")

# Feature selection
feature = st.sidebar.radio("Choose a Feature", ("World Clock", "Stopwatch", "Timer", "Alarm"))

if feature == "World Clock":
    st.header("World Clock")
    # Code for World Clock will go here

elif feature == "Stopwatch":
    st.header("Stopwatch")
    # Code for Stopwatch will go here

elif feature == "Timer":
    st.header("Timer")
    # Code for Timer will go here

elif feature == "Alarm":
    st.header("Alarm")
    # Code for Alarm will go here
