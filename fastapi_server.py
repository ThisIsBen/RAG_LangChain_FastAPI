from fastapi import FastAPI, Response
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import nest_asyncio
from pyngrok import ngrok


app = FastAPI()
# Allow CORS requests
origins = ["*"]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Message(BaseModel):
    text: str

# This can't catch options request from preflight
# The @app.options("/{path:path}") route is a catch-all route that handles OPTIONS requests for any path.
@app.options("/{path:path}")
async def options_handler(*args):
    for i, arg in enumerate(args):
        print(f"Argument {i+1}: {arg}")
    return Response(headers={"Allow": "OPTIONS, GET, POST"})
 


@app.get("/get")
def read_root():
    return {"Hello": "World"}

@app.post("/send/")
async def send_message(message: Message):
    result = graph.invoke({"question": f"{message.text}"})

    # print(f'Context: {result["context"]}\n\n')
    # print(f'Answer: {result["answer"]}')
    
    # Return the answer from AI
    return {"message": f'{result["answer"]}'}