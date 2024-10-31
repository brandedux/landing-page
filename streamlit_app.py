import streamlit as st
import pandas as pd
from validate_email import validate_email

st.title("OilyRAGs")
st.header("AI Assistant for Mechanics")

st.write("""OilyRAGs provides instant access to mechanical knowledge and real-time diagnostic help for mechanics using artificial intelligence and natural language processing.""")

st.write("""**Key Features:**""")
st.markdown("- Vast database of repair procedures and technical documents")  
st.markdown("- Step-by-step repair guides")
st.markdown("- Real-time help through conversation")
st.markdown("- Parts lookup and sourcing")

email = st.text_input("Enter your email")
submit = st.button("Get Updates")
if submit:
    valid = validate_email(email)
    if valid:
        st.success("Thanks for signing up!")
    else:
        st.error("Please enter a valid email")
