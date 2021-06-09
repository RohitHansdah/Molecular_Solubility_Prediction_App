# Molecular_Solubility_Prediction_App

![solubility_logo](https://user-images.githubusercontent.com/44118554/121340010-b6fa2680-c93c-11eb-88d8-46021c06f450.jpg)

This app predicts the Solubility (LogS) values of molecules! Data obtained from the John S. Delaney. ESOL:  Estimating Aqueous Solubility Directly from Molecular Structure. J. Chem. Inf. Comput. Sci. 2004, 44, 3, 1000-1005.

### Model Building Steps :

#### Step 1 : Importing Libraries and Dataset : 

Important python libraries used were Scikit-Learn , Pandas , Numpy  and  Streamlit . The Training dataset was obtained from Kaggle website 
Dataset Link : https://www.kaggle.com/kumar012/hypothyroid?select=hypothyroid.csv

#### Step 2 : Data Preprocessing : 

In this step the missing values were handled using KNN imputer and unwanted columns from the dataset were removed.

#### Step 3 : Exploratory Data Analysis :

In this step Feature Scaling , Normalization and Over Sampling(Imbalanced Data) of the data was done.

#### Step 4 : Data Clustering  :

**KNN Clustering algorithm** was used to divide the Data into multiple clusters and the optimal number of clusters was decided using elbow method.

![download (1)](https://user-images.githubusercontent.com/44118554/121291657-43d5bd80-c906-11eb-9caa-dfa7d9bc0c75.png)

![download](https://user-images.githubusercontent.com/44118554/121291553-16890f80-c906-11eb-9e72-7690169d31d9.png)

#### Step 5 : Model Training :

Each Cluster was trained on **K-Nearest Neighbours Classifier , Naive Bayes Classifier and Support Vector Classifier**.The model with better performance was choosen.

#### Step 6 : Model Prediction and Evaluation and Hyper parameter tuning:

The model predictions were made  on the test dataset and  Hyper parameter tuning was done using Grid Search CV .**ROC-AUC** score was used for evaluation of the model.

![Capture](https://user-images.githubusercontent.com/44118554/121318372-d12a0980-c928-11eb-9ba3-6e5336118057.PNG)

### Website Link : https://molecular-solubility-streamlit.herokuapp.com/

