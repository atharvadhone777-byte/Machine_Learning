#Datatype validation - TypeHinting
def insert(name: str, age: int):    #Type-Hinting - particular datatype shown in its signature while inserting
    if type(name)==str and type(age)==int:
        if age<0:
            raise ValueError("Negative age")
        else:
            print("Accepted")
    else:
        raise TypeError('Incorrect data type')  #Raises manual error

#Datatype Validation - Pydantic
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional, Annotated    #Dict for dictionary

class Patient(BaseModel):   #Each class will inherit BaseModel of Pydantic to become Pydantic class
    name: Annotated[str, Field(max_length=50, title="Name", description='Give name', examples=['Atharva','Nitish'])]    #Annotated is used to include all constraints
    age: int = Field(gt=0, lt=60, strict=True)   #Field is used to check input value should be gretaer than 0 and less than 60
    #Strict=true krne se string mein sirf number aaya fir bhi use string hi samjhega as pydantic is smart ki wo string ke number ko int ki tarah le sakta hai but it may arise problems
    diseases: List[str] = Field(max_length=5)
    contact_details: Optional[Dict[str,str]]=None    #Optional shows that it is not compulsorily required and by default None is shown
    email=EmailStr  #Inbuild dataype to validate email
    url=AnyUrl  #Validates http link format

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):    #Method to validate email
        valid_domains=['hdfc.com','icici.com']
        #abc@hdfc.com
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not valid domain")
        
        return value
    
    @field_validator('name')
    @classmethod
    def upper_name(cls, value): #Uppercase of name
        return value.upper()

    @field_validator('age',mode='before')   #before mode ka matlab automatic type conversion by pydantic se pehele
    @classmethod
    def validate_age(cls,value):    #cls=class, value=given by user
        if 0<value<100:
            return value
        else:
            raise ValueError('Invalid age')
        
    @model_validator(mode='after')      #model_validator -> validates complete model
    def validate_emergnecy_contact(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have emergency contact')
        return model
    
    @computed_field
    @property
    def calculate_bmi(self)->float: #input 'self' model khud hoga and output float hoga
        bmi = round(self.weight/(self.height**2),2)
        return bmi

# nested_models = one model is passed as input to another model for nested methods use in detail
        
#----------------------------------------------------------------------

patient_info = {'name':'nitish','age':30,'diseases':['fever','cold']} #Dictionary format input
patient1 = Patient(**patient_info) #Dictionary is unpacked using ** and inserted inside class name while making object

def insert(patient: Patient): #Object is passed in method and its properties are accessed
    print(patient.name)
    print(patient.age)
    print(patient.calculate_bmi)    #computed_field method call

insert(patient1)
