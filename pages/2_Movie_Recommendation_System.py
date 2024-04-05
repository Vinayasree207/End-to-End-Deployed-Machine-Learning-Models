from models.movies_recommendation_model import init, calc_cos_sim,recommend,fetch_poster
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

@st.cache_data
def getDataFrame():
    return init()

@st.cache_resource
def getVector(df):
    return calc_cos_sim(df)

df = getDataFrame()
sim = getVector(df)


st.title('Movie Recommendation System')
st.markdown('''<B>DISCLAIMER: THIS IS A RECOMMENDATION MODEL CREATED FOR LEARNING PURPOSE ONLY,
            DO NOT CONSIDER THIS RESULTS FOR ACTUAL LOAN APPROVAL PREDICTION</B>''', True)
movies_list = st.selectbox('Choose a movie', df['title'].values)



if st.button('Recommend'):
    movie_recommendations = recommend(movies_list,dframe=df,sim=sim)
    st.write('Generating movie recommendations')
    for i in movie_recommendations:
        st.success(i)

   
st.markdown('<B>Note: The data you enter here is not saved nor shared with anyone.</B>', True)
st.markdown('This model is trained on the below dataset downloaded from Kaggle', True)
#st.dataframe()
