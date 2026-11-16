import streamlit as st
st.title("Hello word")
st.header('This is a header')
# st.divider()
# st.subheader("This is a subheader")
# st.text('Normal size text')
# st.caption("This is a caption")
# st.markdown(r"$sqrt{2x+2}$")
# st.markdown("#Heading 1")
# st.markdown("##Heading 2")
# st.markdown("""
# 1. ML
# 2. DL""")
# st.latex(r"\sqrt{3x+3}")
agree = st.checkbox("I agree")
if agree:
    st.write("You agree")
else:
    st.write("You don't agree")

gender = st.radio(
    "Select your gender",
    ["Male", "Female", "Other"]
)
st.write(f"You selected {gender}")
options = st.selectbox(
    "Select your options",
    ('Option 1', 'Option 2', 'Option 3')
)
st.write(f'You selected {options}')

options = st.multiselect(
    "Select your options",
    ('Option 1', 'Option 2', 'Option 3')
)
st.write(f'You selected {options}')

color = st.select_slider(
    "your color",
    options = ["green","orange","red"]
)

st.write (f'You selected {color}')

age1 = st.number_input("enter your age", min_value = 0, max_value = 100, value = 25)
st. write (f"you are {age1} old")

age2 = st.slider(
    "your age", min_value = 0, max_value = 100, value = 100
)
st. write (f"you are {age2} old")

name = st.text_input("Enter your name")
st.write(f"Your name is {name}")

st.divider()
st.link_button(
    "About",
    url = "http://www.google.com"
)

file = st.file_uploader(
    "Upload your file",
    type= ["pdf", 'docx', "doc"],
    accept_multiple_files = False,
)

if file:
    st.write(f'You upload {file.name}')