import streamlit as st

# Header Section
st.title("AI/ML Project Portfolio")
st.subheader("Welcome to my portfolio!")

# Navigation Bar
nav_selection = st.sidebar.radio("Navigation", ["Home", "Projects", "About", "Contact"])

if nav_selection == "Home":
    st.write("This is the home page.")
    # Add content specific to the home page

elif nav_selection == "Projects":
    st.subheader("AI/ML Projects")

    # Project 1
    st.subheader("Project 1")
    st.image("project1_image.jpg", caption="Project 1", use_column_width=True)
    st.write("Project 1 description.")
    st.button("View Details")

    # Project 2
    st.subheader("Project 2")
    st.image("project2_image.jpg", caption="Project 2", use_column_width=True)
    st.write("Project 2 description.")
    st.button("View Details")

    # Add more projects as needed

elif nav_selection == "About":
    st.subheader("About Me")

    # Add information about yourself, your skills, and background

elif nav_selection == "Contact":
    st.subheader("Contact Me")

    # Add contact information such as email, social media links, etc.

# Footer Section
st.markdown("---")
st.write("© 2023 My Portfolio. All rights reserved.")
st.write("Connect with me on [GitHub](https://github.com/your_username) | [LinkedIn](https://linkedin.com/in/your_profile)")
