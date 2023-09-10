from fastapi import FastAPI
from .models.models import FeedBack

app = FastAPI()

fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "robert_smith", "email": "robert@example.com"},
    3: {"username": "aleksei_smith", "email": "aleksei@example.com"},
    4: {"username": "anna_smith", "email": "anna@example.com"},
    5: {"username": "galina_smith", "email": "galina@example.com"},
    6: {"username": "mad_smith", "email": "mad@example.com"}
}

fake_feedback_lst = [
    {"name": "Alice", "comments": "Great course! I'm learning a lot."}
]

@app.get("/users")
def read_all_users(limit: int = 5):
    return dict(list(fake_users.items())[:limit])

@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}

@app.post("/feedback")
async def send_feedback(feedback: FeedBack):
    fake_feedback_lst.append({"name": feedback.name, "comments": feedback.message})
    return f"Feedback received. Thank you, {feedback.name}!"


@app.get("/comments")
async def show_feedback():
    return fake_feedback_lst
