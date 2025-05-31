from models import db, JournalEntry, User
from app import app

entries = [
    {"title": "Workout", "content": "Ran 5 miles"},
    {"title": "Daily Notes", "content": "Studied Flask"},
]

with app.app_context():
    db.create_all()
    user = User(username="testuser")
    user.set_password("securepassword")
    db.session.add(user)
    db.session.commit()

    for entry in entries:
        db.session.add(JournalEntry(**entry, user_id=user.id))
    
    db.session.commit()