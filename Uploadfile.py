import speech_recognition as sr
import streamlit as st
import requests   
r = sr.Recognizer()
audio_file = st.file_uploader("Upload your audio file here")
if audio_file is not None: 
    st.audio(audio_file, format="audio")
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)  
    recognised_text= r.recognize_google(audio)
    st.write('The text recognized from the audio seems to be: ')
    st.write( recognised_text )
