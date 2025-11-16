from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class re(BaseModel):
    name : str = Field(..., max_length = 16, description= 'maximum 16 words')
    age : int= Field(..., lt = 70, description = 'it should be below 70')

@app.get('/welcome')
def welcome():
    return {'messge' : 'Hellow world'}
