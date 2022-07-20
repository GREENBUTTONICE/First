import streamlit as st

st.title('This is a title')
st.write('Hello WOrld!!!')
st.text('This is some text.')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
     st.image(picture)


import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )