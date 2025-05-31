def test_register_user(client):
    response = client.post('/auth/register', json={"username": "testuser", "password": "securepass"})
    assert response.status_code == 201
    assert b"User registered successfully" in response.data

def test_login_user(client):
    client.post('/auth/register', json={"username": "testuser", "password": "securepass"})
    response = client.post('/auth/login', json={"username": "testuser", "password": "securepass"})
    assert response.status_code == 200
    assert b"Login successful" in response.data

def test_login_invalid_user(client):
    response = client.post('/auth/login', json={"username": "wronguser", "password": "wrongpass"})
    assert response.status_code == 401
    assert b"Invalid credentials" in response.data