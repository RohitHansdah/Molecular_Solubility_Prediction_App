# Molecular_Solubility_Prediction_App

![solubility_logo](https://user-images.githubusercontent.com/44118554/121340010-b6fa2680-c93c-11eb-88d8-46021c06f450.jpg)

This app predicts the Solubility (LogS) values of molecules! Data obtained from the John S. Delaney. ESOL:  Estimating Aqueous Solubility Directly from Molecular Structure. J. Chem. Inf. Comput. Sci. 2004, 44, 3, 1000-1005.

### Model Building Steps :

#### Step 1 : Importing Libraries and Dataset : 

Important python libraries used were Scikit-Learn , Pandas , Numpy  and  Streamlit . The Training dataset was obtained from the John S. Delaney. ESOL
Dataset Link : https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv

#### Step 2 : Data Preprocessing : 

In this step the missing values in the data were checked.

#### Step 3 : Exploratory Data Analysis :

In this step Feature Scaling of the data was done.

#### Step 4 : Model Training :

A **SVR** model was trained  

#### Step 5 : Model Prediction and Evaluation :

The model predictions were made  on the test dataset and  Hyper parameter tuning was done using Grid Search CV .**ROC-AUC** score was used for evaluation of the model.

![Capture](https://user-images.githubusercontent.com/44118554/121318372-d12a0980-c928-11eb-9ba3-6e5336118057.PNG)

### Website Link : https://molecular-solubility-streamlit.herokuapp.com/

