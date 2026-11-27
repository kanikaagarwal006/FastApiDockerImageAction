from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/students")
async def get_students():
    return [
        {"id": 1, "name": "Kanika"},
        {"id": 2, "name": "Aman"},
    ]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)