from pydantic import BaseModel, Field

class CustomerChurn(BaseModel):
    id: str = Field(pattern=r'^\d{4}-[A-Z]{5}$')
    gender: str = Field(max_lenght=6, min_length=4, strip_whitespace=True)
    senior_citizen: bool
    partner: bool
    dependents: bool
    tenure: int = Field(ge=0)
    phone_service: bool
    multiple_lines: str = Field(max_length=50)
    internet_service: str = Field(max_length=50)
    online_security: str = Field(max_length=50)
    online_backup: str = Field(max_length=50)
    device_protection: str = Field(max_length=50)
    tech_support: str = Field(max_length=50)
    streaming_tv: str = Field(max_length=50)
    streaming_movies: str = Field(max_length=50)
    contract: str = Field(max_length=50)
    paperless_billing: bool
    payment_method: str = Field(max_length = 255)
    monthly_charges: float
    total_charges: float
    churn: bool

def main():
    customer = CustomerChurn(
        id="1234-ABCDE",
        gender="Female",
        senior_citizen=False,
        partner=True,
        dependents=False,
        tenure=True,
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