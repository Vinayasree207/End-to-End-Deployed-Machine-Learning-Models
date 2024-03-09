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
st.write("""
    I am Vinayasree Kalburgi, I am certified Data Scientist. I am very passionate about Data Science, Machine Learning and Artificial Intelligence.
            I can do end to end Model deployments starting from scratch.
    I have solid foundation in Computer Science Engineering coupled with over 5 years of experience in Business Administration, backed by a Masters degree. I am deeply committed to my professional growth, continuously expanding my expertise in Data Science, Machine Learning, and ongoing training in Artificial Intelligence, NLP, and Deep Learning. My aim is to contribute to the advancement of organizations while nurturing my personal development.
    
    ### PROJECTS
    
    **Customer Segmentation Using K Means Clustering:**
    My objective was to minimize advertising costs and maximize revenue by analyzing customer behavior and sentiment towards clothing. Leveraging the elbow method, I identified six clusters that effectively segmented customers. This segmentation enabled prioritization of customers and provided valuable insights for offering discounts and promotional offers.
    
    **Avocado Price Prediction:**
    In this project, I aimed to predict the average price of avocados using various Machine Learning regression models. With a dataset comprising 14 columns and over 14,599 rows, I employed Linear Regression, Decision Tree regressor, and Random Forest regressor models. The prediction accuracy was assessed based on the Root Mean Squared Error (RMSE) value.
    
    **EDA on Facebook Utilization:**
    I conducted Exploratory Data Analysis and Data Storytelling on Facebook usage patterns. Utilizing various visualization libraries such as Matplotlib, Seaborn, Plotly, Pandas, NumPy, and scikit-learn, I explored user behavior based on factors like age group, gender, and activity level.
    
    **Defects and Rejection Analysis of Valves at FMVPL:**
    This project involved a comprehensive analysis of various factors contributing to valve rejection, leading to internal failure costs and operational wastage. I conducted data analysis on a sample size of 5,050 valve units, collected through primary and secondary sources.
    
    ### EDUCATION
    
    - **PGP in Data Science, Machine Learning & Artificial Intelligence:** International School of Artificial Intelligence & Data Science
    - **Master of Business Administration (Operation, HR & IM):** School of Management Studies and Research
    - **Bachelor of Engineering (Computer Science):** KLE Institute of Technology
    
    ### SKILLS
    
    My skillset encompasses a wide range of areas including Statistics & Probability, Data Extraction, Data Mining/Processing, Data Wrangling, Data Visualization, Data Exploration, Data Modeling, Machine Learning, Model Deployment, MySQL, Flask, Power BI, Tableau, Advanced Excel, and Business Understanding. I am proficient in Python, and have basic knowledge in C, C++, Java, with ongoing training in Tensorflow & Keras, Deep Learning, NLP, Computer Vision, Autovision & AutoNLP, Web scraping, and AWS SageMaker.
    
    ### EXPERIENCE
    
    - **Assistant Manager:** SDM University, Hubballi
    - **Assistant Manager (South) - Security:** Delhivery, Bangalore
    - **Operations:** Freshboxx Services Pvt. Ltd., Hubballi
    
    ### ACHIEVEMENTS
    
    - Secured 1st place in YUVA Competition by ITC, 2017.
    - Built a Seed Sowing Robot using Embedded C Language.
    - State Level Shuttle Badminton Player.
    
    ### PASSIONS
    
    My passions lie in ML Ops, Artificial Intelligence, and Data Science.
    
    ### CERTIFICATION
    
    - The Ultimate MySQL Bootcamp: Go from SQL Beginner to Expert, Udemy, 2023
    - Deploying Machine Learning models with Flask, Udemy, 2023
    - Tableau 2022 A-Z: Hands-On Tableau Training for Data Science, Udemy, 2023
    - Microsoft Power BI - Data Modeling & Data Manipulation (Ongoing), Udemy, 2023
    - AWS Certified Machine Learning Specialty 2023 - Hands On! (Ongoing), Udemy, 2023
    
    ### LANGUAGES
    
    - English (Native)
    - Hindi, Kannada, Telegu (Proficient)
    """)

st.markdown("### LINKS")
c1,c2,c3,c4,c5,c6= st.columns(6)
with c1:
# Links to profile
    st.link_button('LinkedIn', "https://www.linkedin.com/in/vinayasree-kalburgi-37580ab7/")
with c2:
    st.link_button('GitHub', "https://github.com/Vinayasree207")


st.markdown("### KEY WORDS")
st.markdown('''
&#x2022; Certified Data Scientist &#x2022; Data Science Enthusiast &#x2022; Machine Learning &#x2022; NLP &#x2022; Computer Vision 
            &#x2022; Deep Learning &#x2022; Python &#x2022; MySQL &#x2022; GitHub &#x2022; Business Administration &#x2022; Computer Science
''',True)


