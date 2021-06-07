######################
# Import libraries
######################
import numpy as np
import pandas as pd
import streamlit as st
import pickle
from PIL import Image

######################
# Page Title
######################

image = Image.open('solubility_logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# Molecular Solubility Prediction Web App
This app predicts the **Solubility (LogS)** values of molecules!
Data obtained from the John S. Delaney. [ESOL:  Estimating Aqueous Solubility Directly from Molecular Structure](https://pubs.acs.org/doi/10.1021/ci034243x). ***J. Chem. Inf. Comput. Sci.*** 2004, 44, 3, 1000-1005.
***
""")
##Uploading the File

uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    # Loading the Pre-trained Model 
    # Reads in saved model
    model = pickle.load(open('solubility_model.pkl', 'rb'))
    X=pd.DataFrame()
    X['MolLogP']=df['MolLogP']
    X['MolWt']=df['MolWt']
    X['NumRotatableBonds']=df['NumRotatableBonds']
    X['AromaticProportion']=df['AromaticProportion']
    # Apply model to make predictions
    prediction = model.predict(X)
    res=pd.DataFrame()
    res['logS']=prediction
    st.header('Predicted LogS values')
    st.write(res)