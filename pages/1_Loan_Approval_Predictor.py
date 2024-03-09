
from models.loanmodel import init, process, getDataFrame
import streamlit as st
st.set_page_config(page_title="Loan_Approval_Predictor")
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

rf = init()

st.title('Loan Approval Prediction Second App')
st.markdown('''<B>DISCLAIMER: THIS IS A MACHINE LEARNING MODEL CREATED FOR LEARNING PURPOSE ONLY,
            DO NOT CONSIDER THIS RESULTS FOR ACTUAL LOAN APPROVAL PREDICTION</B>''', True)
no_of_dependents = st.number_input('Enter the number of dependents', 0, 20)
education = st.selectbox('Choose your education level', ['Graduate','Not Graduate'])
self_employed = st.radio('Are you self-employed?', ['Yes','No'])
income_annum = st.number_input('Enter your Annual Income')
loan_amount = st.number_input('Enter the loan amount', 100000 , 100000000)
loan_term = st.number_input('Enter the Term of Loan', 1,30)
cibil_score =st.number_input('Enter your Cibil Score', 300,900)
residential_assets_value = st.number_input('Enter your residential assets value')
commercial_assets_value =st.number_input('Enter your commercial assets value')
luxury_assets_value = st.number_input('Enter your luxury assets value')
bank_asset_value = st.number_input('Enter your bank asset value')

btn = st.button('Predict')

if btn:
    st.write('Sending Values for Prediction')
    df = process(no_of_dependents, education, self_employed, income_annum, loan_amount, loan_term, cibil_score, residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value)
    result  = rf.predict(df)
    if result[0]==0:
        st.write("Approved")
    else:
        st.write("Rejected")

st.markdown('<B>Note: The data you enter here is not saved nor shared with anyone.</B>', True)
st.markdown('This model is trained on the below test dataset downloaded from Kaggle', True)
st.dataframe(getDataFrame())