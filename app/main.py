from fastapi import FastAPI

app = FastAPI()

fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "robert_smith", "email": "robert@example.com"},
    3: {"username": "aleksei_smith", "email": "aleksei@example.com"},
    4: {"username": "anna_smith", "email": "anna@example.com"},
    5: {"username": "galina_smith", "email": "galina@example.com"},
    6: {"username": "mad_smith", "email": "mad@example.com"}
}

@app.get("/users")
def read_all_users(limit: int = 5):
    return dict(list(fake_users.items())[:limit])

@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}