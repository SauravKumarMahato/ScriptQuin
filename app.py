import streamlit as st
from api_call import generate_code_with_gpt
import time

# Set the layout to a wide format
st.set_page_config(layout="wide", page_title="ScriptQuin")


# Set dark background color for the entire page
st.markdown(
    """
    <style>
        body {
            background-color: #262730;
            color: #ffffff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Left section
left_col = st.sidebar
left_col.title("Test Script generator in Selenium(Python)")

# Box for code explanation
code_explanation = left_col.text_area("Enter the html code of your testing page: (Used for testing static html page having form )", height=300, max_chars=100000)

# Set light background color for the left window
left_col.markdown(
    '<style>div.Widget.stTextArea {background-color: #333333;}</style>', 
    unsafe_allow_html=True
)

# Right section
right_col = st
right_col.title("Script generated")

# Button to generate code with dynamic styling
generate_button_clicked = left_col.button(label="Generate Script", key="generate_button", help="Click to generate code")

# Set light green background color for the right window
right_col.markdown(
    '<style>div.Widget.stText {background-color: #1f1f1f;}</style>', 
    unsafe_allow_html=True
)

# Variables for controlling the display speed
delay_between_words = 0.2

# Generate code using GPT API when the button is pressed
if code_explanation:
    generated_code = generate_code_with_gpt(code_explanation)

    if generate_button_clicked and generated_code:
        # Split the generated code into lines
        generated_lines = generated_code.split("\n")

        # Display each line with characters revealed one by one
        for line in generated_lines:
            st.text(line)
            time.sleep(delay_between_words)
