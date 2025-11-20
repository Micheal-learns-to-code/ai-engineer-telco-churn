# --- 1. Imports ---
# StandardScaler: scale numeric features to zero mean and unit variance
# OneHotEncoder: convert categorical features into one-hot indicator arrays
# ColumnTransformer: apply different transformers to different columns
# Pipeline: chain preprocessing and estimator into a single object
# LogisticRegression: linear classifier for binary classification
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# --- 2. Define the preprocessing and modeling pipeline ---
# List of numeric columns that will be scaled
numerical_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
binary_features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
                   
# List of categorical columns that will be one-hot encoded
categorical_features = ['MultipleLines', 'InternetService', 'OnlineSecurity',
                        'OnlineBackup', 'DeviceProtection', 'TechSupport',
                        'StreamingTV', 'StreamingMovies', 'Contract',
                        'PaymentMethod']

# Transformer for numeric data: standard scaling
numerical_transformer = StandardScaler()

# Transformer for binary data: no transformation, passthrough
binary_transformer = 'passthrough'

# Transformer for categorical data: one-hot encoding, ignore unseen categories at predict time
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# ColumnTransformer to apply the above transformers to the respective columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('bin', binary_transformer, binary_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Classifier: logistic regression with fixed random state and increased max iterations
classifier = LogisticRegression(random_state=42, max_iter=1000)

# Full pipeline: first preprocess data, then fit/predict with the classifier
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', classifier)
])

