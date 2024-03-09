# importing the required libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

def getDataFrame():
    return pd.read_csv('./data/loan_approval_dataset.csv')

def init():
    
    # loading the Data
    loan_data = pd.read_csv('./data/loan_approval_dataset.csv')

    # removing whitespace in the column_name
    loan_data.columns = loan_data.columns.str.strip()

    # LabelENcoding the categorical variables
    labelencoder = LabelEncoder()
    loan_data['education'] = labelencoder.fit_transform(loan_data['education'])
    loan_data['self_employed'] = labelencoder.fit_transform(loan_data['self_employed'])
    loan_data['loan_status'] = labelencoder.fit_transform(loan_data['loan_status'])
    loan_data.drop('loan_id', axis = 1, inplace = True)

    # splitting data in train and test
    x = loan_data.drop(columns = ['loan_status'])
    y = loan_data['loan_status']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 207)

    # Model Building using Random Forest Algorithm 
    rf = RandomForestClassifier()
    rf.fit(x_train,y_train)
    y_pred_train = rf.predict(x_train)
    y_pred_test = rf.predict(x_test)

    return rf
   
def process(no_of_dependents, education, self_employed, income_annum, loan_amount, loan_term, cibil_score, residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value):
    #data = pd.DataFrame(no_of_dependents, education, self_employed, income_annum, loan_amount, loan_term, cibil_score, residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value)
    user_data = pd.DataFrame(data = [[no_of_dependents, education, self_employed, income_annum, loan_amount, loan_term, cibil_score, residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value]], columns = 'no_of_dependents education self_employed income_annum loan_amount loan_term cibil_score residential_assets_value commercial_assets_value luxury_assets_value bank_asset_value'.split())
 
    labelencoder = LabelEncoder()
    user_data['education'] = labelencoder.fit_transform(user_data['education'])
    user_data['self_employed'] = labelencoder.fit_transform(user_data['self_employed'])
    return user_data