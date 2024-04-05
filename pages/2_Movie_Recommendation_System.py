from models.movies_recommendation_model import init, calc_cos_sim,recommend
import streamlit as st
import time

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

df,rawdf = getDataFrame()
sim = getVector(df)


st.title('Movie Recommendation System')
st.markdown('''<B>DISCLAIMER: THIS IS A RECOMMENDATION MODEL CREATED FOR LEARNING PURPOSE ONLY</B>''', True)
movies_list = st.selectbox('Choose a movie', df['title'].values)

if st.button('Recommend'):
    with st.spinner('Generating movie recommendations...'):
        time.sleep(2)
    movie_recommendations = recommend(movies_list,dframe=df,sim=sim)
    st.balloons()
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.info(movie_recommendations[0])

    with col2:
        st.info(movie_recommendations[1])
      
    with col3:
        st.info(movie_recommendations[2])
       

    with col4:
        st.info(movie_recommendations[3])
       
    with col5:
        st.info(movie_recommendations[4])
       

st.markdown('This model is trained on the below dataset downloaded from Kaggle', True)
st.subheader('Raw Data Frame for reference')
st.dataframe(rawdf)


