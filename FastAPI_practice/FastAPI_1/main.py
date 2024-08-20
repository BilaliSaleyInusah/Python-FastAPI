from fastapi import FastAPI

# let import Enum
from enum import Enum

# let import BaseModel from Pydantic
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/")
async def post():
    return {"message": "hello from the post route"}


@app.put("/")
async def put():
    return {"message": "hello from the put route"}

# used to get the user page
@app.get("/user")
async def list_users():
    return {"message": "list users route"}

# used to get a specific user called "me"
@app.get("/user/me")
async def list_users():
    return {"message": "this is the current user"}

# here we are specifing the data type of the user_id
# @app.get("/user/{user_id}")
# async def list_users(user_id: int):
#     return {"message str ": user_id}

# used to get any user entered 
# here it can be any data type
@app.get("/user/{user_id}")
async def list_users(user_id):
    return {"user_id" : user_id}

# here we want to specify the user ids to be entered 


# let creat list of Enum 
class users(str,Enum):
    user1 = "Kojo",
    user2 = "Ama",
    user3 = "Kofi"

@app.get("/enum/user/{user_id}")
async def list_user(user_id: users):
    if user_id == "Ama":
        return "Ama is currently in school"
    elif user_id == "Kojo":
        return "Small Kojo will attend to you"
    else:
        return "Okay i will help you out, Kofi"
    

# in the above we have been using path parameters 
#  now let use query paramters 

@app.get("/school")
async def students():
    return "This is a school page"

# let have a student query
# @app.get("/school/student")
# async def students(name: str | None = None):
#     return {"This is a student page with name query " : name }

# let have a query with dynamic path parameters
# let make it so that we can have page for student and lectures separate

# let have Enum class for the two page 
class school_users(str, Enum):
    page1 = "lecture",
    page2 = "student"



@app.get("/school/{page}")
async def students(

    page: school_users, #path parameter
    name: str,
    level: str,
    age: int | None = None,
    city: str | None = None

    ):
    if page == "lecture":
        if age and city:
            return {
                "page":page,
                "name":name,
                "age":age,
                "level":level,
                "city":city
                }
        return {"welcome to the lectures page age and city not provided"}
    else:
        if age and city:
            return {
                "page":page,
                "name":name,
                "age":age,
                "level":level,
                "city":city
                }
        return {"Our beloved Student we care about you. age and city not provided"}
    

