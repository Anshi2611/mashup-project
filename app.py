import streamlit as st
import subprocess

st.title("🎵 Music Mashup Generator")

singer = st.text_input("Singer Name")
num_videos = st.number_input("Number of Videos", min_value=1, max_value=10, value=1)
duration = st.number_input("Duration (seconds)", min_value=1, max_value=60, value=10)

if st.button("Generate Mashup"):
    st.write("Processing... please wait ⏳")

    command = f'python 102303605.py "{singer}" {num_videos} {duration} output.mp3'
    subprocess.run(command, shell=True)

    st.success("Mashup created successfully! 🎉")
    st.audio("output.mp3")
