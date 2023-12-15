from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

# Header Section
st.title("AI/ML Project Portfolio")
st.subheader("Welcome to my portfolio!")

# Hamburger Menu
menu_options = ["Home", "Projects", "About", "Contact"]
nav_selection = st.sidebar.selectbox("Menu", menu_options)

# Navigation Bar
navigation_html = """
    <style>
        .hamburger { display: none; }
        @media screen and (max-width: 600px) {
            .hamburger { display: block; position: absolute; top: 10px; right: 10px; }
            .menu { display: none; position: absolute; top: 50px; right: 10px; background-color: #f9f9f9; padding: 10px; }
        }
    </style>
    <div class="hamburger" onclick="toggleMenu()">&#9776;</div>
    <div class="menu" id="menu">
        <form>
            <select onchange="location = this.value;">
                <option value="" disabled selected hidden>Navigation</option>
                <option value="/">Home</option>
                <option value="/projects">Projects</option>
                <option value="/about">About</option>
                <option value="/contact">Contact</option>
            </select>
        </form>
    </div>

    <script>
        function toggleMenu() {
            var menu = document.getElementById("menu");
            menu.style.display = (menu.style.display === "block") ? "none" : "block";
        }
    </script>
"""

st.markdown(navigation_html, unsafe_allow_html=True)

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

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
