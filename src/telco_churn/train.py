import mlflow
import utils
import pipeline
from schemas import CustomerChurn
from pydantic import ValidationError
import pandas as pd
import joblib   
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

def validate_rawdata(df: pd.DataFrame):
    """Validate raw data against the schema."""
    records = df.to_dict(orient='records')

    try:        
        [CustomerChurn(**r) for r in records]
        print("Data validation successful! Schema is sane.")
    except ValidationError as e:
        print("---")
        print("🚨 RAW DATA IS NOT SANE! Check the schema definition or the input data.")
        # Re-raise the error to stop the script and show the detailed error traceback
        raise e
    return True


df = utils.load_data('data/Telco-Customer-Churn.csv')

validate_rawdata(df)

#Preprocessing binary features
df['gender'] = df['gender'].apply(lambda x: 1 if x == 'Male' else 0)
df['Partner'] = df['Partner'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Dependents'] = df['Dependents'].apply(lambda x: 1 if x == 'Yes' else 0)
df['PhoneService'] = df['PhoneService'].apply(lambda x: 1 if x == 'Yes' else 0)
df['PaperlessBilling'] = df['PaperlessBilling'].apply(lambda x: 1 if x == 'Yes' else 0)

# Preprocessing TotalCharges column
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(0)

# Drop out the output column
X = df.drop('Churn', axis=1)
y = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

# Add this line BEFORE mlflow.start_run() or any other MLflow call
mlflow.set_tracking_uri("http://127.0.0.1:5000")

with mlflow.start_run():
    test_size = 0.6
    random_state = 42
    
    mlflow.log_param("test_size", test_size)
    mlflow.log_param("random_state", random_state)
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Train the model pipeline
    pipeline.model_pipeline.fit(X_train, y_train)
    y_pred = pipeline.model_pipeline.predict(X_test)
    f1 = f1_score(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    mlflow.log_metric("f1_score", f1)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)

    # print(f'F1 Score: {f1:.4f}')
    # print(f'Accuracy: {accuracy:.4f}')
    # print(f'Precision: {precision:.4f}')
    # print(f'Recall: {recall:.4f}')

    # Save the trained model pipeline to a file
    mlflow.sklearn.log_model(pipeline.model_pipeline)
    joblib.dump(pipeline.model_pipeline, 'models/trained_model.joblib')