"""This module is created to process the user input data"""


# Importing the necessaries libraries
import numpy as np
import pickle
import pandas as pd
# import sklearn
from sklearn.preprocessing import StandardScaler
import os

# Create a function for the pre-process data

def preprocess_data(data):

    # Accepting user input in form of a list
    user_input= [data['no_of_dependents'], data['education'], data['self_employed'], data['income_annum'], data['loan_amount'],
                data['loan_term'], data['Assets_value']]
    
    data['debt_to_income'] = int(data['loan_amount']) / int(data['income_annum'])
    data['asset_coverage'] = int(data['Assets_value']) / int(data['loan_amount'])

    final_input= [data['no_of_dependents'], data['education'], data['self_employed'], data['income_annum'], data['loan_amount'],
                data['loan_term'], data['Assets_value'], str(data['debt_to_income']), str(data['asset_coverage'])]
    
    # # Convert user input to 2D array
    input_array= np.array(final_input).reshape(1, -1)

    # Load the scaled trained data
    with open('Loan approval status input scaling.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

    # Transform the input array to standard scaler using the trained scaled
    scaled_input= scaler.transform(input_array)

    return scaled_input

