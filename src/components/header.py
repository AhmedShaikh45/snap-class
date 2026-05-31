import streamlit as st

def home_screen():

    # Local image path
    logo_path = r"C:\Users\Ahmed\Downloads\download.webp"

    # Display logo
    st.image(logo_path, width=120)

    # Display title
    st.markdown(
        """
        <h1 style="text-align:center; color:#E0E3FF;">
            SNAP<br/>CLASS
        </h1>
        """,
        unsafe_allow_html=True
    )