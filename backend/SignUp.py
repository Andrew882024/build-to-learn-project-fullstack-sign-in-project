import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

class username_class(BaseModel):
  username:str

class UserNameAndPassword(BaseModel):
  username:str
  password:str

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
  
@app.get("/check_whether_username_and_password_match/{username}/{password}")
def check_whether_username_and_password_match(username:str,password:str):
  if(username_and_passworrd_dictionary[username] == password):
    return "username_and_password_match"
  else:
    return "username_and_password_does_not_match"
  
@app.post("/get_username_and_password")
def get_username_and_password(item:UserNameAndPassword):
  username_and_passworrd_dictionary[item.username] = item.password
  return f"{item.username} and {item.password}"

