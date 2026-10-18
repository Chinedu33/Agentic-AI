def add_patient_data(name:str, age:int):
    if type(name) == str and type(age)== int:
        if age >=0:
            print(name)
            print(age)
            print("Data added successfully to the database!")
        else:
            raise ValueError("Age cannot be negative") 
    else: 
        raise TypeError("Invalid data type for name or age. Name should be a string and age should be an integer ") 

def update_patient_data(name:str, age:int):
    if type(name) == str and type(age)== int:
        if age>=0:
            print(name)
            print(age)
            print("Data updated successfully to the database!")  
        else:
            raise ValueError("Age cannot be negative")    
    else: 
        raise TypeError("Invalid data type for name or age. Name should be a string and age should be an integer ")            
            
    
add_patient_data("Bappy", -25)
