from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from Schema.schema import User, Bot, Register
from Core.modelo import model

app = FastAPI()

users = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "test@gamil",
        "age": 25,
    },
    {
        "id": 2,
        "name": "John José",
        "email": "test@gamil",
        "age": 25,
    },
    {
        "id": 3,
        "name": "John Tomas",
        "email": "test@gamil",
        "age": 25,
    }
]

@app.get("/users")
def get_all_users() -> dict:
    return {
        "messages": "successfully fetched all users",
        "data": users
    }

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int) -> dict:
    for user in users:
        if user["id"] == user_id:
            return {
                "messages": "successfully fetched user",
                "data": user
            }
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users")
def create_user(user: User) -> dict:
    user_data = user.model_dump()
    return {
        "messages": "user created successfully",
        "data": user_data
    }

history = [
    SystemMessage(content="Eres experto en programación y desarrollo de chatbots"),
]
@app.post("/chatbot")
def chatbot_response(prompt: Bot) -> dict:

      history.append(HumanMessage(content=prompt.prompt))
      response = model.invoke(history)
      history.append(AIMessage(content=response.content))
      last_message = history[-1].content
      return {
        "status": "success",
        #"response": response.content,
        "last_response": last_message,
    }

@app.post("/register")
def register_user(user: Register) -> dict:
    return {
        "message": "user registered successfully",
        "data": f"user {user.name} registered successfully"
    }