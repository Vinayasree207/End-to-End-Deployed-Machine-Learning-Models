
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
            Welcome User!
            This website contains few machine learning models. This website is an example of how a end-to-end model deployment application would look like.
            All the data that is used for these models is from Kaggle and does not contain any information about any real user.
            The purpose of this website is to show working Machine Learning Models deployed on AWS EC2 instance, each model uses a different algorithm so solve the problem statement.
            Below are few of the tech stacks used for end-to-end deployment:
            - AWS EC2
            - AWS Route 53 for DNS 
            - Streamlit for Web development
            - Putty,WinScp for file transfer
            - Machine Learning algorithms/models''', True)
st.markdown('''
           Feel free to play around with these models. Links are on the left side panel.''', True)
