import pytest
from server.models import db, User, JournalEntry
from server.app import app

@pytest.fixture
def setup_database():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield
        db.drop_all()

def test_user_password_hashing(setup_database):
    user = User(username="testuser")
    user.set_password("securepass")
    
    assert user.password_hash is not None
    assert user.check_password("securepass") == True
    assert user.check_password("wrongpass") == False

def test_unique_usernames(setup_database):
    user1 = User(username="testuser", password_hash="hashedpass")
    user2 = User(username="testuser", password_hash="hashedpass")
    
    db.session.add(user1)
    db.session.commit()
    
    with pytest.raises(Exception):  # Expecting a uniqueness violation
        db.session.add(user2)
        db.session.commit()

def test_journal_entry_creation(setup_database):
    user = User(username="testuser")
    user.set_password("securepass")
    db.session.add(user)
    db.session.commit()

    entry = JournalEntry(title="Workout", content="Ran 5 miles", user_id=user.id)
    db.session.add(entry)
    db.session.commit()

    saved_entry = JournalEntry.query.first()
    assert saved_entry is not None
    assert saved_entry.title == "Workout"
    assert saved_entry.user_id == user.id