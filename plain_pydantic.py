from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class PatientData(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies:List[str]
    contact_info: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi

    @model_validator(mode = "after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and "emergency" not in model.contact_info:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return model

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "iciici.com"]
        # abc@gmail.com
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")

        return value

    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("BMI:", patient.bmi)
    print("Data added successfully to the database!")

patient_data = {"name":"Alex", "email": "bappy@hdfc.com","linkedin_url": "https://www.linkedin.com/in/chinedu-chibuzor-b6126319a", "age":"70", "weight": "70.5", "height": 1.75, "married": True, "allergies": ["peanuts", "shellfish"],
                "contact_info": {"phone": "123-456-7890", "emergency": "987-654-3210"}}
patient_1 = PatientData(**patient_data)
add_patient_data(patient_1)