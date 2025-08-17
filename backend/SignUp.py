import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
#for connecting mysql
import mysql.connector


#//////////////////////////////////////////////////////////////////////////////#
#                              database function                               #
#//////////////////////////////////////////////////////////////////////////////#

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="build_to_learn_sign_in_database")

mycursor = mydb.cursor()

def add_new_user_infor(primary_key_column_name:str,other_one_column_name:str,
  primary_key_value:str,other_one_column_value):
  mycursor.execute(f"insert into user_infor({primary_key_column_name},{other_one_column_name}) values('{primary_key_value}','{other_one_column_value}')")
  mydb.commit()
  return

#this thing is working
#add_new_user_infor("username","passwd","a_username","a_password")

def whether_this_item_exist_in_this_column(column_name:str,item:str) ->bool:
  mycursor.execute(f"SELECT EXISTS(SELECT * FROM user_infor WHERE {column_name}='{item}');")
  output = mycursor.fetchone() 
  #print(output[0])
  if(output[0] == 1):
    return True
  else:
    return False



#whether_this_item_exist_in_this_column("username","a_usernam")

def whether_password_match_username(username:str,password:str):
  mycursor.execute(f"SELECT passwd FROM user_infor WHERE username='{username}'")
  output = mycursor.fetchone()
  #print(output[0])
  if(output[0] == password):
    print(1)
    return True
  else:
    print(0)
    return False
  

#whether_password_match_username("a_username","a_passwor")  

#//////////////////////////////////////////////////////////////////////////////#
#                                  api part                                    #
#//////////////////////////////////////////////////////////////////////////////#

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
  #if(username_need_to_check in username_and_passworrd_dictionary):
  if(whether_this_item_exist_in_this_column("username",username_need_to_check)==True):
    return "exist"
  else:
    return "not_exist"
  
@app.get("/check_whether_username_and_password_match/{username}/{password}")
def check_whether_username_and_password_match(username:str,password:str):
  #if(username_and_passworrd_dictionary[username] == password):
  if(whether_password_match_username(username,password) == True):
    return "username_and_password_match"
  else:
    return "username_and_password_does_not_match"
  
@app.post("/get_username_and_password")
def get_username_and_password(item:UserNameAndPassword):
  #username_and_passworrd_dictionary[item.username] = item.password
  add_new_user_infor("username","passwd",item.username,item.password)
  return f"{item.username} and {item.password}"








