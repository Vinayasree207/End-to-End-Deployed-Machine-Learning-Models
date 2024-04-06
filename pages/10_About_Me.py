import streamlit as st
st.set_page_config(page_title="About Me")

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


left_co, cent_co, last_co = st.columns(3)
with last_co:
    # Sidebar - Profile photo
    st.image("./resources/Vinayasree Kalburgi.jpg", use_column_width=False, width=250)

# Main content
st.title("About Me")
st.header("Vinayasree Kalburgi")
st.markdown("""<style>.big-font {font-size:20px !important;}</style>""", unsafe_allow_html=True)


c1,c2,c3,c4,c5,c6= st.columns(6)

with c1:
# Links to profile
    st.link_button('LinkedIn', "https://www.linkedin.com/in/vinayasree-kalburgi-37580ab7/")
with c2:
    st.link_button('GitHub', "https://github.com/Vinayasree207")
with c3:
    st.link_button('Resume', "https://drive.google.com/drive/folders/1h2MZVAjXQNg5MJTdkPhdCWiDGbsziUm7")
    
st.write("""
    I'm a **certified Data Scientist**. What gets me excited: Data Science, Machine Learning, and Artificial Intelligence are my absolute passions. From building models to deploying them end-to-end, I thrive on bringing data-driven solutions to life.
    
    With a strong foundation in **Computer Science Engineering** and over 5 years of experience in **Business Administration**, complemented by a Masters degree, I bring a unique blend of **technical expertise and real-world understanding** to the table
    
    I am very passionate about **Data Science, Machine Learning and Artificial Intelligence**. I can do **end to end Model deployments**.
    
    I'm constantly pushing the boundaries of my knowledge, diving deeper into Data Science, Machine Learning, and continually honing my skills in **Artificial Intelligence, NLP, and Deep Learning**.

    My ultimate goal? To not only contribute to the growth and success of organizations but also to embark on a journey of personal development and fulfillment along the way.
    
    ### PROJECTS
         
    **Avocado Price Prediction:**
    
    🔹Leveraged Supervised Learning techniques to build a regression model to predict the average price of a single avocado.
         
    🔹Verified accuracy using different models like Linear Regression, Decision Tree regressor, Random Forest regressor
         
    🔹Random Forest Regressor appeared to be the best regressor,performed Hyperparameter tuning using GridSearchCV to obtain optimal parameters.
         
    🔹Random Forest Regressor achieved an R-Square Score of 0.84 on test Data.
    
    **House Price Prediction using Support Vector Machine**
    
    🔹Started with data understanding, data wrangling, basic EDA, where we found various trend between price range and other 81 independent variable.
         
    🔹Dataset contains 81 features/Columns x 1460 rows both 38 numerical and 43 categorical values
         
    🔹Based on Variance Ratio, Built a PCA model with 10 principal components.
         
    🔹Implemented various regression algorithms, also understood the working and implementation of Support Vector Regressor with RMSE score of 81348
    
    **EDA on Facebook Utilization:**
         
    🔹Performed Exploratory Data Analysis to find out the trend and visualize data with various kinds of plots: Bar chart, Pie chart, Scatter plot , Heat map etc.
    
    🔹Dataset contains 99003 rows x 15 features/Columns both numerical and categorical values.
    
    🔹Conducted Data preprocessing, handled the null values, cleaned the dataset, detected outliers and handled the same.

    🔹Studied the Behavior and pattern of users usage of facebook, based on various factors like Age group, Gender, Tenure, Dormant users etc
         
    **and Many more. Please visit my GitHub Profile to find more projects. Link mentioned above.**

    
    ### EDUCATION
    
    - **PGP in Data Science, Machine Learning & Artificial Intelligence:** International School of Artificial Intelligence & Data Science
    - **Master of Business Administration (Operation, HR & Integrated Marketing):** School of Management Studies and Research
    - **Bachelor of Engineering (Computer Science):** KLE Institute of Technology
    
    ### SKILLS

    Language, Tools and Technologies:   
         
    Python || MySQL || Streamlit || Advanced Excel || GitHub || Git Version Control || WinSCP || PuTTY || Visual Studio || AWS EC2 || Tableau || Jupyter Notebook || Google Colab || MS Office
    
    ML Frameworks:
         
    Scikit-learn || Scipy || Tensorflow || Keras || Pandas || Numpy || Seaborn || Matplotlib || Plotly || Flask
         
    Ongoing Trainings:
         
    Artificial Intelligence || NLP || Computer Vision || PowerBI || Autovision&AutoNLP || Deep Learning || AWS cloud
    
    ### EXPERIENCE
    
    - **Assistant Manager - HR:** SDM University, Hubballi
    - **Assistant Manager (South) - Security:** Delhivery, Bangalore
    - **Operations Manager:** Freshboxx Services Pvt. Ltd., Hubballi
    
    ### PASSIONS
    
    My passions lies in ML_Ops, NLP, LLM, Artificial Intelligence.
    
    ### CERTIFICATIONS
         
    - Global Certificate in Data Science
    - Full Stack in Data Science program
    - Post Graduation Program in Data Science, MachineLearning & Artificial Intelligence.
    - The Ultimate MySQL Bootcamp: Go from SQL Beginner to Expert, Udemy, 2023
    - Deploying Machine Learning models with Flask, Udemy, 2023
    
    ### LANGUAGES
    
    - English (Native)
    - Hindi, Kannada, Telugu (Proficient)
    """)

st.markdown("### KEY WORDS")
st.markdown('''
&#x2022; Certified Data Scientist &#x2022; Data Science Enthusiast &#x2022; Machine Learning &#x2022; ML_Ops &#x2022; NLP &#x2022; LLM &#x2022;  Computer Vision 
            &#x2022; Deep Learning &#x2022; Artificial Intelligence &#x2022; Python &#x2022; MySQL &#x2022; GitHub &#x2022; Business Administration &#x2022; Computer Science Engineering
''',True)


