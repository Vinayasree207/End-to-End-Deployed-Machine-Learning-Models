
import streamlit as st
st.set_page_config(page_title="Home Page")
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

st.title("Introduction")
st.markdown('''
            
Welcome to the platform!

Here, you'll find a few Prediction and Recommendation based Machine Learning models. 

Think of it as a sneak peek into the world of end-to-end model deployments. I've curated data from Kaggle, ensuring your privacy is always protected—no real user info involved!

My aim is to showcase these operational Machine Learning Models in action deployed on an AWS EC2 instance. Each model comes packed with a unique approach and algorithm, ready to tackle different problem statements head-on.

Here's a glimpse of the tech used behind the scenes:

    🔹 AWS EC2: Powering our platform with reliable infrastructure.
    🔹 AWS Route 53 for DNS: Ensuring smooth and efficient routing.
    🔹 Streamlit for Web Development: Crafting an intuitive and user-friendly interface.
    🔹 Putty and WinScp for File Transfer: Handling file transfers with ease.
    🔹 Machine Learning Algorithms/Models: The heart and soul of our platform, bringing intelligence to the forefront.

So, Dive in and explore these models! Links to our models are conveniently placed on the left side panel.  
            
''', True)

st.markdown('''
           Have fun tinkering around with them, and feel free to reach out if you have any questions or feedback..''', True)

st.subheader('''
           Happy exploring!''')