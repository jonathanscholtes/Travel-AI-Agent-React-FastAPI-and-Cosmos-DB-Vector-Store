from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from web import agent, session

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(agent.router)
app.include_router(session.router)



@app.get("/")
def get() -> str:
    return "running"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)