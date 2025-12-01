from pydantic import BaseModel, Field, ConfigDict, field_validator

class CustomerChurn(BaseModel):
    # This tells Pydantic to accept field names (like 'id') 
    # as well as alias names ('customerID') when creating the model.
    model_config = ConfigDict(populate_by_name=True)


    id: str = Field(alias='customerID', pattern=r'^\d{4}-[A-Z]{5}$')
    gender: str = Field(max_length=6, min_length=4)
    senior_citizen: bool = Field(alias='SeniorCitizen') 
    partner: bool = Field(alias='Partner')
    dependents: bool = Field(alias='Dependents')
    tenure: int = Field(ge=0)
    phone_service: bool = Field(alias='PhoneService')   
    multiple_lines: str = Field(alias='MultipleLines', max_length=50)
    internet_service: str = Field(alias='InternetService', max_length=50)
    online_security: str = Field(alias='OnlineSecurity', max_length=50)
    online_backup: str = Field(alias='OnlineBackup', max_length=50)
    device_protection: str = Field(alias='DeviceProtection', max_length=50)
    tech_support: str = Field(alias='TechSupport', max_length=50)
    streaming_tv: str = Field(alias='StreamingTV', max_length=50)
    streaming_movies: str = Field(alias='StreamingMovies', max_length=50)
    contract: str = Field(alias='Contract', max_length=50)
    paperless_billing: bool = Field(alias='PaperlessBilling')
    payment_method: str = Field(alias='PaymentMethod', max_length = 255)
    monthly_charges: float = Field(alias='MonthlyCharges')

    total_charges: float | None = Field(alias='TotalCharges')
    @field_validator('total_charges', mode='before')
    @classmethod
    def validate_total_charges(cls,v):
        if v == ' ':
            return None
        return v
    
    churn: bool = Field(alias='Churn')

def main():
    customer = CustomerChurn(
        id="1234-ABCDE",
        gender="Female",
        senior_citizen=False,
        partner=True,
        dependents=False,
        tenure=4,
        phone_service=True,
        multiple_lines="No",
        internet_service="DSL",
        online_security="Yes",
        online_backup="No",
        device_protection="Yes",
        tech_support="No",
        streaming_tv="No",
        streaming_movies="No",
        contract="Month-to-month",
        paperless_billing=True,
        payment_method="Electronic check",
        monthly_charges=29.85,
        total_charges=29.85,    
        churn=False)
    print(customer)


if __name__ == "__main__":
    main()