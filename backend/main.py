from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/test")
async def main():
    return {"message": "backend"};


#insted of writing uvicorn main:app --reload in terminal, i initilize the uvicorn server in the main.py file itself, so that i can run the backend server by just running the main.py file.

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload="True")
