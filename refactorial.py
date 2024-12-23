from fastapi import FastAPI, HTTPException

app = FastAPI()

def validate_user_input(email: str, password: str):
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="Password too short")
    if "@" not in email:
        raise HTTPException(status_code=400, detail="Invalid email")

@app.post("/users/")
async def create_user(name: str, email: str, password: str):
    validate_user_input(email, password)
    return {"name": name, "email": email}

@app.put("/users/")
async def update_user(name: str, email: str, password: str):
    validate_user_input(email, password)
    return {"name": name, "email": email}
