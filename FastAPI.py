# VIDEO - 1
# API - Frontend and backend ka connector - Waiter in hotel
# Monolithic Architecture - Frontend and backend is connected directly and tightly coupled.But isse mein kisi 3rd party ko mera data nhi de skta so API to make backend publically visible
# Responce from backend is given in json format because json is understood in all languages
# Website frontend, Android frontend, iOS frontend -> same backend this is achievable due to API

# VIDEO - 2
# FastAPI - Python Web Framework for building APIs. FastAPI is created from Starlette(manages recieving request and sending responce) and Pydantic(Checks if data is in right format)
# Fast API's API is fast to run and code

# Structure : Web Server -> SGI -> API code
# Web server (Uvicorn) - Kisi client ka http request process krega, multiple at a time whereas, Gunicorn can process only one at a time also supports async-await feature
# ASGI (Asynchronous Server Gateway Interface) - http reuest ko python readable format mein change krega with multiple requests at a time
# API code - According to parameters response dega like if some f1, f2 parameters is given to ml model it gives predicted value as output as send it as responce
# WSGI (Web server Gateway Interface)(Werkzeug) - Ek time pr ek hi request chalegi, this is used in flask so it is synchronous in nature
# To see details of routing data in home page link add /docs after it to see all routes of get, post, put, delete

from fastapi import FastAPI,Path, HTTPException, Query
from fastapi.responses import JSONResponse

app = FastAPI() #FastAPI ka object

@app.get("/")   #This annotation is called as endpoint
def hello():
    return {"message":"Hello World"}

@app.get("/about")
def about():
    return {"message":"This is about page"}

#To run this file : uvicorn main:app --reload

# VIDEO - 3 - HTTP Methods in FASTAPI
# Software - Static(Less interaction), Dynamic(More interaction)-CRUD operations. CRUD => Create->POST, Read->GET, Update->PUT, Delete->DELETE
# MSExcel software humne install kiya toh bas humari machine pr chalega similarly Website is also a software installed on machine and that machine is called 'server' and the machine which access this server is called client

#Now we are making backend for Patient Management App
@app.get("/")
def hello():
    return {"message":"Patient Management System API"}

import json
def load_data():    #json file ka saara data load karega
    with open('JSON.json','r') as f:
        data=json.load(f)
    return data

def save_data(data):    #Input data is saved in a file
    with open('patient.json','w') as f:
        json.dump(data,f)

@app.get('/view')
def view():
    data=load_data()
    return data

# VIDEO - 4 
# Path Parameters - Dynamic segments of URL path used to identify specific resource
@app.get('/pateint/{patient_id}') #Here patient_id is dynamic segment
def view_patient(patient_id:str=Path(...,description='ID of patient',example='P001')):  #... ka matlab variable arguement and also required
    #Path( ) functions is used to provide metadata, validation rules and documentation hints for path parameters in your API endpoints using => Title, Description, Example, Min_length, Max_length, ge,gt,lt,le
    data=load_data()    # load all patients
    if patient_id in data:
        return data[patient_id]
    else:
        return {'error':'Patient not found'}
    
#HTTP status codes = Indicate 3-digit number as result of clients request returned by web server, ex: status-code=200 (success)
# 2xx-success, 3xx-redirection, 4xx-client error, 5xx-server error
#HTTP Exception - return custom http responce when something goes wrong

@app.get('/pateint/{patient_id}') 
def view_patient(patient_id:str=Path(...,description='ID of patient',example='P001')): 
    data=load_data()    
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail='Patient not found')

#Query Parameter - key-value pair appended to end of url to pass additional data to carry out operations such as sorting, filtering, searching, etc.
#Ex: .../patients?city=Delhi&sort_by=age    #'?' se start hota hai query arguement and & se multiple arguements ko joda jata hai

@app.get('/sort')
def sort_patients(sort_by:str=Query(..., description='Sort by height, weight and bmi'),order:str=Query('asc',description='sort in ascending or descending')): #By default order ascending rahega
    valid_fields=['height','weight','bmi'] #These are some columns of our data in database
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid fields")

    if order not in ['asc','dsc']:
        raise HTTPException(status_code=400, detail="Invalid order")
        
    if order=='dsc':
        sort_order=True
    else:
        sort_order=False
        
    data=load_data()
    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order)

    return sorted_data
#Iska url -> .../patient?sort_by=height&order=dsc

#VIDEO - 5 - Pydantic

#VIDEO - 6 - Post Request
#Request Body - Portion of HTTP request that contains data sent by client to server

from pydantic import BaseModel

class Patient(BaseModel):
    id:str
    name:str


@app.post('/create')
def create_patient(patient:Patient):
    # load existing data
    data = load_data()
    # check if patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient already exist')
    # new patient
    patient.model_dump()    #model_dump() ek pydantic object ko dictionary mein convert karta hai
    data[patient.id]=patient.model_dum(exclude=['id'])
    #save into json file
    save_data(data)
    return JSONResponse(status_code=201,content={'message':'patient created'})

#VIDEO - 7 - PUT and DELETE Requests
class PatientUpdate(BaseModel): #New Pydantic model for update
    id:str
    name:str

patient_update=PatientUpdate()

@app.put('/edit/{patient_id}')
def update_patient(patient_id:str, pateint_update:PatientUpdate):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Patient not found")
    
    data[patient_id]=pateint_update.model_dump(exclude='id')    #Iska new pydantic object banaker firse dump kr skte ho to recalculate all fields of that class 'Patient'
    save_data(data)
    return JSONResponse(status_coe=200,content={'message':'patient updated'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Patient not found")
    
    deleted_patient=data.pop(patient_id)
    save_data(data)
    return JSONResponse(status_coe=200,content={'message':'patient deleted'})

#VIDEO - 8 - Serving ML Models with FastAPI
#Feature engeneering ka mtalb if hamare model ko required parameter bmi hai but hum user se direclty bmi nahi maang sakte nhi toh user ko pen paper pe bmi nikalna padega so hum user se raw data mangenge like weight and height and hum khudse bmi calculate krenge

#VIDEO - 9 - Improving FastAPI - screenshot

#VIDEO - 10 - Docker - Mggie example
# Consistency - Docker container encapsulates all components, ensuring application runs across all environments
# Isolation - Docker provides isolated environments for each application, preventing interference and ensuring stable performance
# Scalability - Docker allows to run multiple containers at same time allowing for scaling
# Container Engine/Docker Engine - Used to create, run and manage docker containers
# CLI(Command Line Interface) - Interface by which user interacts with docker




















