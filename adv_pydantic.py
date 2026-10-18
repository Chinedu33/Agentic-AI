from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class PatientData(BaseModel):
    name: Annotated[str, Field(max_length=50, title= "Name of the patient", description = "Give the name of the patient in less than 50 chars", examples=["Bappy", "Alex"] )]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt =0, description = "weight of the patient in kg")]
    married: Annotated[bool, Field(default = None, description="Is the patient married or not")]
    allergies: Annotated[Optional[List[str]],Field(default = None, max_length=5) ]
    contact_info: Dict[str, str]


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("Data added successfully to the database!")

patient_data = {"name":"Alex", "email": "bappy@gmail.com","linkedin_url": "https://www.linkedin.com/in/chinedu-chibuzor-b6126319a", "age":"25", "weight": "70.5", "allergies": ["peanuts", "shellfish"],
                "contact_info": {"phone": "123-456-7890"}}
patient_1 = PatientData(**patient_data)
add_patient_data(patient_1)