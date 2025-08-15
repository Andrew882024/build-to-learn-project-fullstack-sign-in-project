import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

class username_class(BaseModel):
  username:str

username_and_passworrd_dictionary = {
  "test_username":"test_password"
}

# @app.post("/username_sign_up",responce_modal = username_class)
# def username_sign_up():
#   return username

origins = ["http://127.0.0.1:5500"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,  
  allow_credentials=True,
  allow_methods=["*"],   
  allow_headers=["*"],
)

@app.get("/username_check_if_exist/{username_need_to_check}")
def username_check_if_exist(username_need_to_check:str):
  if(username_need_to_check in username_and_passworrd_dictionary):
    return "exist"
  else:
    return "not_exist"