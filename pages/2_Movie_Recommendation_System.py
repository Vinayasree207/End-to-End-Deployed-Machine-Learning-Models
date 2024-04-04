
import streamlit as st
st.set_page_config(page_title="Movie_Recommendation_System")
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

st.title('Movie Recommendation System')
st.markdown('''<B>DISCLAIMER: THIS IS A MACHINE LEARNING MODEL CREATED FOR LEARNING PURPOSE ONLY,
            DO NOT CONSIDER THIS RESULTS FOR ACTUAL LOAN APPROVAL PREDICTION</B>''', True)
movies_list = st.selectbox('Choose a movie', ['Batman','Avatar'])

btn = st.button('Recommend')

if btn:
    st.write('Generating movie recommendations')
    st.success("Approved")


st.markdown('<B>Note: The data you enter here is not saved nor shared with anyone.</B>', True)
st.markdown('This model is trained on the below test dataset downloaded from Kaggle', True)
#st.dataframe(getDataFrame())